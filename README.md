A facts-only FAQ assistant that answers common questions about mutual fund schemes using information from official public sources.

Selected Product: Groww
Project Type: Product Management Fellowship – Milestone Project
Focus: Mutual Fund Information, FAQ Automation, Source-Based Answers

1. Project Overview

The Groww Mutual Fund FAQ Assistant is designed to help users find factual information about mutual fund schemes through a simple question-and-answer interface.

Users can ask questions about:

Expense Ratio (TER)

Exit Load

Minimum SIP Amount

ELSS Lock-in Period

Riskometer

Scheme Benchmark

Mutual Fund Statements

Capital Gains Statements

The assistant retrieves answers from a curated collection of official public sources and provides a source link with every factual response.

The project focuses on improving access to reliable mutual fund information while avoiding investment recommendations or personalized financial advice.

2. Problem Statement

Mutual fund investors often need to visit multiple websites and documents to find basic scheme-related information.

This can make it difficult to quickly understand details such as expense ratios, exit loads, SIP requirements, lock-in periods and risk levels.

Proposed Solution:

Build a simple FAQ assistant that provides concise, source-backed answers using official information from Groww, HDFC Mutual Fund, SEBI and AMFI.

3. Project Objectives

Make mutual fund information easier to access.

Reduce the effort required to find scheme-related facts.

Provide reliable answers with official source links.

Avoid unsupported or misleading financial information.

Abstain when the available information is insufficient.

4. Features

Natural-language FAQ interface.

Curated official-source knowledge base.

Source link included with factual answers.

Support for common mutual fund questions.

Basic retrieval-based answer matching.

Fallback response when reliable information is unavailable.

Facts-only approach with no investment advice.

5. Supported Schemes

The initial knowledge base includes these HDFC Mutual Fund schemes:

Scheme

Information covered

HDFC Top 100 Fund

Scheme information and risk disclosures

HDFC Flexi Cap Fund

SIP, TER, exit load, benchmark and riskometer

HDFC Mid Cap Fund

SIP, benchmark, exit load and riskometer

HDFC ELSS Tax Saver Fund

Lock-in, SIP, TER and exit load

Important: Groww is the selected platform for this project. HDFC Mutual Fund schemes are used as the initial sample scheme dataset.

6. Technology Stack

Python

Streamlit

Pandas

Scikit-learn

TF-IDF-based text retrieval

JSON and CSV knowledge-base files

GitHub for version control

7. Project Structure

groww-mutual-fund-faq-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── disclaimer.txt
├── sample_qa.md
│
├── data/
│   ├── corpus.json
│   └── source_list.csv
│
└── tests/
    └── test_cases.md

8. Installation and Execution

Step 1: Clone the repository

git clone https://github.com/Snigdha-raj/groww-mutual-fund-faq-assistant.git

Step 2: Open the project directory

cd groww-mutual-fund-faq-assistant

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Run the application

streamlit run app.py

The application will open in your browser.

9. Sample Questions and Answers

Q1. What is the minimum SIP amount for HDFC Flexi Cap Fund?

Sample Answer: The project snapshot records a minimum SIP amount of ₹100. Please verify the latest amount in the official scheme information before relying on it.

Source: https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/regular

Q2. What is the exit load for HDFC Flexi Cap Fund?

Sample Answer: The project snapshot records an exit load of 1% for redemption or switching within one year, and nil thereafter. Check the latest scheme documents for the applicable terms.

Source: https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/regular

Q3. What is the lock-in period for HDFC ELSS Tax Saver Fund?

Sample Answer: ELSS mutual fund investments have a three-year lock-in period. Each SIP instalment has its own lock-in period calculated from its allotment date.

Source: https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver-fund/regular

Q4. What is the benchmark of HDFC Mid Cap Fund?

Sample Answer: The scheme information page identifies its benchmark. Users should check the latest scheme document for the current benchmark details.

Source: https://www.hdfcfund.com/explore/mutual-funds/hdfc-mid-cap-fund/regular

Q5. How can I download my capital gains statement from Groww?

Sample Answer: Refer to Groww's official help documentation for the current steps to access tax-related reports and statements.

Source: https://groww.in/help/my-account/ma-others/where-can-i-get-the-tax-proof-for-section-80c

Q6. What is a Riskometer?

Sample Answer: A Riskometer is a visual indicator used to communicate the risk level of a mutual fund scheme. It is not a prediction of future returns.

Source: https://investor.sebi.gov.in/hindi/riskometer.html

Q7. Should I invest in HDFC Flexi Cap Fund?

Sample Answer: This assistant does not provide investment recommendations or assess personal suitability. Please consult a SEBI-registered investment adviser for personalized guidance.

Source: https://investor.sebi.gov.in/

Q8. What is an expense ratio?

Sample Answer: The Total Expense Ratio (TER) represents the expenses charged to a mutual fund scheme for managing and operating it, expressed as a percentage of the scheme's assets.

Source: https://www.amfiindia.com/investor/knowledge-center-info?zoneName=expenseRatio

10. Official Source List

The assistant uses official public information from the following sources.

HDFC Mutual Fund

HDFC Flexi Cap Fund
https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/regular

HDFC Mid Cap Fund
https://www.hdfcfund.com/explore/mutual-funds/hdfc-mid-cap-fund/regular

HDFC ELSS Tax Saver Fund
https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver-fund/regular

HDFC Top 100 Fund Scheme Summary Document
https://files.hdfcfund.com/s3fs-public/2024-11/HDFC%20Top%20100%20Fund.pdf

HDFC Factsheets
https://www.hdfcfund.com/mutual-funds/factsheets

HDFC SIP FAQs
https://www.hdfcfund.com/services/faqs/systematic-investment-plan

HDFC ELSS Information
https://www.hdfcfund.com/learners-corner/elss

HDFC ELSS Scheme Summary Document
https://files.hdfcfund.com/s3fs-public/scheme_summary/2026-04/HDFCTS_1776085358.pdf

HDFC Flexi Cap Fund Key Information Memorandum
https://files.hdfcfund.com/s3fs-public/KIM/2025-11/KIM%20-%20HDFC%20Flexi%20Cap%20Fund%20dated%20November%2021%2C%202025_1.pdf

Groww

Groww Tax Proof and Statement Help
https://groww.in/help/my-account/ma-others/where-can-i-get-the-tax-proof-for-section-80c

Groww Mutual Fund Charges
https://groww.in/help/mutual-funds/searchable/what-are-the-charges-for-mutual-fund-investments--93

Groww Mutual Funds
https://groww.in/mutual-funds

Groww Mutual Fund Help Centre
https://groww.in/help/mutual-funds

AMFI

AMFI Investor Service FAQs
https://www.amfiindia.com/investor/become-mf-distributor?zoneName=InvestorService

AMFI Consolidated Account Statement Information
https://www.amfiindia.com/investor/become-mf-distributor?zoneName=consolidatedAcct

SEBI

SEBI Riskometer Information
https://investor.sebi.gov.in/hindi/riskometer.html

SEBI Riskometer, Benchmark and Portfolio Disclosure Circular
https://www.sebi.gov.in/legal/circulars/aug-2021/disclosure-of-risk-o-meter-of-scheme-benchmark-and-portfolio-details-to-the-investors_52262.html

SEBI Master Circular for Mutual Funds – March 2026
https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html

SEBI Mutual Fund Filings
https://www.sebi.gov.in/filings/mutual-funds.html

SEBI Expense and Riskometer Disclosure Circular
https://www.sebi.gov.in/legal/circulars/nov-2024/disclosure-of-expenses-half-yearly-returns-yield-and-risk-o-meter-of-schemes-of-mutual-funds_88230.html

11. Answer Validation and Limitations

Answers should be based only on the curated knowledge base.

Every factual answer must include at least one relevant official source link.

If a matching source is unavailable, the assistant should abstain rather than invent an answer.

Scheme information may change over time.

Historical sample answers must not be treated as live financial data.

The source list should be reviewed periodically.

12. Disclaimer

Facts-only project. No investment advice.

This assistant provides limited factual information from selected official public sources.

It does not:

Recommend mutual funds.

Predict investment returns.

Compare schemes to recommend one over another.

Assess individual financial suitability.

Provide personalized investment or tax advice.

Expense ratios, exit loads, minimum SIP amounts, risk labels and scheme information may change. Users should verify the latest information using the linked official documents and websites.

The assistant does not need or request sensitive personal information. Users should never enter PAN, Aadhaar, bank account details, OTPs, passwords or other confidential information.

13. Future Improvements

Potential future enhancements include:

Expanding the scheme knowledge base.

Adding automated source freshness checks.

Improving question matching and retrieval accuracy.

Adding more test cases for unsupported questions.

Improving the user interface.

Adding source-level update timestamps.

Deploying the assistant for public access.

14. Project Outcome

This project demonstrates how product thinking and basic AI-powered retrieval can be used to solve an information-discovery problem.

The focus is on accessibility, factual accuracy, source transparency, user trust and responsible product design.

Created as part of the NextLeap Product Management Fellowship.

GitHub Repository:
https://github.com/Snigdha-raj/groww-mutual-fund-faq-assistant
