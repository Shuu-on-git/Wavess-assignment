# Wavess 1.0 & 2.0: LinkedIn & GTM Intelligence Prototypes

This repository contains the code and results for a two-part technical prototype demonstrating data analysis and AI-powered GTM intelligence. The project is presented as an interactive Streamlit dashboard.

---

## 🚀 Task 1: LinkedIn Post & Audience Analysis

This prototype analyzes the performance and audience of a specific LinkedIn post to determine audience relevance against a defined Ideal Customer Profile (ICP).

### Features:
- **Post Analysis:** Calculates sentiment, engagement metrics, and key text features.
- **Audience Analysis:** Ingests data from post reactions, comments, and reshares.
- **ICP Scoring:** Ranks the audience based on a relevance score derived from keywords in their professional headlines (e.g., roles, seniority).
- **Interactive Dashboard:** Allows filtering and exploring the ranked audience list.

---

## 🧠 Task 2: GTM Intelligence Platform

This prototype acts as an automated Go-To-Market research agent. It was tasked with researching **Stripe** to identify recent strategic shifts and provide actionable recommendations for a sales or marketing team.

### Features:
- **RAG Architecture:** Utilizes a Retrieval-Augmented Generation (RAG) pipeline to ensure accuracy and prevent AI hallucinations.
- **Targeted Intelligence:** Runs focused searches for high-value GTM signals (funding, partnerships, key hires, product launches).
- **Automated Synthesis:** The agent drafts a comprehensive GTM report, including an executive summary and actionable recommendations.
- **Self-Verification (Conceptual):** The architecture includes a final verification step where an AI fact-checker validates the drafted report against the source material.

---

## 🛠️ Tech Stack

- **Data Collection:** Apify API, Tavily Search API
- **AI & Orchestration:** OpenRouter (for access to various LLMs), LangChain (for RAG pipeline)
- **Data Manipulation:** Pandas
- **Dashboard:** Streamlit
- **Core Language:** Python

---

## 🏃‍♀️ How to Run the Dashboard

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shuu-on-git/Wavess-assignment.git
    cd your-project-name
    ```

2.  **Set up environment variables:**
    - Create a file named `.env` in the root of the project.
    - Add your API keys to this file:
      ```
      OPENROUTER_API_KEY=your_key_here
      TAVILY_API_KEY=your_key_here
      APIFY_API_TOKEN=your_key_here
      ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run dashboard.py
    ```
    The dashboard will open in your web browser.