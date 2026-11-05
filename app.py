import json
import re
from datetime import date
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).parent
CORPUS = json.loads((ROOT / "data" / "corpus.json").read_text(encoding="utf-8"))
SOURCES = {}
with (ROOT / "data" / "source_list.csv").open(encoding="utf-8") as f:
    import csv
    for row in csv.DictReader(f):
        SOURCES[row["source_id"]] = row

st.set_page_config(page_title="Groww Mutual Fund FAQ", page_icon="🌱", layout="centered")

st.markdown("""
<style>
.main {max-width: 900px; padding-top: 2rem;}
.hero {padding: 1.2rem 1.4rem; border-radius: 16px; background: linear-gradient(120deg,#e9f8ef,#f5fbf7); border:1px solid #cfe9d7;}
.small-muted {color:#64748b; font-size:0.86rem;}
.stChatMessage {border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🌱 Mutual Fund FAQ Assistant</h1><p>Groww product study · HDFC Mutual Fund scheme facts</p><b>Facts-only. No investment advice.</b></div>', unsafe_allow_html=True)
st.caption("Ask about expense ratio, exit load, minimum SIP, ELSS lock-in, riskometer, benchmark or statement downloads. Every supported answer includes one official source link.")

EXAMPLES = [
    "What is the minimum SIP for HDFC Flexi Cap Fund?",
    "What is the lock-in period for HDFC ELSS Tax Saver Fund?",
    "How do I download my capital-gains statement on Groww?"
]
cols = st.columns(3)
for col, q in zip(cols, EXAMPLES):
    if col.button(q, use_container_width=True):
        st.session_state.pending_question = q

# Sensitive identifiers are never needed; reject rather than process/store them.
PII_PATTERNS = [
    r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",       # PAN-like token
    r"\b\d{12}\b",                       # Aadhaar-like 12 digits
    r"\b\d{10}\b",                       # phone-like 10 digits
    r"\b\d{6}\b",                        # OTP-like 6 digits
    r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"
]
ADVICE_TERMS = [
    "should i buy", "should i sell", "should i invest", "which fund should",
    "best mutual fund", "best fund", "recommend", "recommendation",
    "where should i invest", "portfolio", "asset allocation", "switch my",
    "will it give", "highest return", "compare returns", "expected return",
    "good to invest", "worth investing"
]
TOPIC_HINTS = {
    "expense ratio": ["expense ratio", "ter", "charges", "fee"],
    "exit load": ["exit load", "redeem", "switch out"],
    "minimum SIP": ["minimum sip", "min sip", "sip amount", "minimum investment"],
    "lock-in": ["lock in", "lock-in", "elss", "tax saver"],
    "riskometer": ["riskometer", "risk level", "risk category"],
    "benchmark": ["benchmark", "index"],
    "statement": ["statement", "capital gains", "tax proof", "download", "cas"]
}
def has_pii(q):
    return any(re.search(p, q, flags=re.I) for p in PII_PATTERNS)

def is_advice(q):
    ql = q.lower()
    return any(x in ql for x in ADVICE_TERMS)

def detect_topic(q):
    ql = q.lower()
    for topic, terms in TOPIC_HINTS.items():
        if any(t in ql for t in terms):
            return topic
    return None

def detect_scheme(q):
    ql = q.lower()
    if any(x in ql for x in ["flexi", "flexicap", "flexi cap"]):
        return "HDFC Flexi Cap Fund"
    if any(x in ql for x in ["mid cap", "midcap"]):
        return "HDFC Mid Cap Fund"
    if any(x in ql for x in ["elss", "tax saver", "tax-saver"]):
        return "HDFC ELSS Tax Saver Fund"
    if any(x in ql for x in ["top 100", "top100", "large cap"]):
        return "HDFC Top 100 Fund"
    return None

@st.cache_resource
def make_index():
    texts = [f"{d['scheme']} {d['topic']} {d['text']}" for d in CORPUS]
    vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix

VECTORIZER, MATRIX = make_index()

def retrieve(q, scheme, topic):
    query = f"{scheme or ''} {topic or ''} {q}"
    qv = VECTORIZER.transform([query])
    sims = cosine_similarity(qv, MATRIX).ravel()
    ranked = sims.argsort()[::-1]
    for idx in ranked:
        d = CORPUS[int(idx)]
        if scheme and d["scheme"] not in (scheme, "General"):
            continue
        if topic and topic not in d["topic"].lower() and not (topic == "statement" and d["topic"] in ("account statement","CAS download","Groww statement download")):
            continue
        if sims[idx] < 0.04:
            continue
        return d, float(sims[idx])
    return None, 0.0

def answer(q):
    if has_pii(q):
        return ("For your privacy, please do not enter PAN, Aadhaar, phone numbers, email addresses, account numbers or OTPs. "
                "This assistant does not collect or store personal identifiers. You can ask a general question without personal details.",
                "https://www.amfiindia.com/investor/become-mf-distributor?zoneName=InvestorService", "Privacy safeguard")
    if is_advice(q):
        return ("I can provide official scheme facts, but I cannot recommend buying, selling or selecting a mutual fund. "
                "Please consult a SEBI-registered investment adviser for personal advice.",
                "https://investor.sebi.gov.in/", "SEBI Investor education")
    topic = detect_topic(q)
    scheme = detect_scheme(q)
    if not topic:
        return ("I can answer factual questions about expense ratio, exit load, minimum SIP, ELSS lock-in, riskometer, benchmark and statement downloads. "
                "Please ask one of these facts and name the scheme where relevant.",
                "https://www.hdfcfund.com/mutual-funds/factsheets", "HDFC Mutual Fund factsheets")
    doc, score = retrieve(q, scheme, topic)
    if not doc:
        if topic == "statement":
            doc = next(d for d in CORPUS if d["id"] == "D16")
        elif topic == "riskometer":
            doc = next(d for d in CORPUS if d["id"] == "D19")
        elif topic == "expense ratio":
            doc = next(d for d in CORPUS if d["id"] == "D20")
        else:
            return ("I could not verify that exact scheme fact in the current curated corpus. Please check the latest official scheme page or Scheme Information Document; I will not guess.",
                    "https://www.hdfcfund.com/mutual-funds/factsheets", "Official HDFC factsheets")
    src = SOURCES[doc["source_id"]]
    msg = doc["text"]
    if doc["topic"] == "expense ratio":
        msg += " This is a time-sensitive figure; recheck the live AMC page."
    return (msg, src["url"], src["title"])

if "messages" not in st.session_state:
    st.session_state.messages = []
for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

pending = st.session_state.pop("pending_question", None)
prompt = st.chat_input("Ask a factual mutual-fund question…")
if pending:
    prompt = pending

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    text, url, title = answer(prompt)
    response = f"{text}\n\n**Source:** [{title}]({url})\n\n_Last updated from sources: 2026-11-01._"
    st.session_state.messages.append({"role":"assistant","content":response})
    with st.chat_message("assistant"):
        st.markdown(response)

with st.expander("Scope, sources and limitations"):
    st.markdown("""
    **Product:** Groww (platform UX reference).  
    **AMC:** HDFC Mutual Fund.  
    **Schemes:** HDFC Top 100 Fund, HDFC Flexi Cap Fund, HDFC Mid Cap Fund and HDFC ELSS Tax Saver Fund.  
    **Retrieval:** Local TF-IDF retrieval over a small, curated corpus. The assistant does not browse live pages at question time and does not calculate returns.  
    **Freshness:** The source review date is shown on each answer. Expense ratios, riskometers, minimum amounts and scheme terms can change; verify on the linked live official source.  
    **Privacy:** Do not enter personal identifiers. The prototype does not write chat history to a database, but the hosting provider may have its own infrastructure logs.  
    **Not advice:** No buy/sell/portfolio recommendations.
    """)
