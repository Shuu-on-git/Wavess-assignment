# Wavess 1.0 & 2.0: LinkedIn & GTM Intelligence Prototypes

This repository contains the code and results for a two-part technical prototype demonstrating data analysis and AI-powered GTM intelligence. The project is presented as an interactive Streamlit dashboard.

---

## 🚀 How to View the Dashboard

The repository includes the pre-generated data files, so **no API keys are needed** to run and view the final dashboard.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shuu-on-git/Wavess-assignment.git
    cd Wavess-assignment
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run dashboard.py
    ```
    The interactive dashboard will open in your web browser, showcasing the results of both tasks.

---

## 🛠️ Project Overview & Tech Stack

### Task 1: LinkedIn Post & Audience Analysis
This prototype analyzes the performance and audience of a specific LinkedIn post to determine audience relevance against a defined Ideal Customer Profile (ICP).

- **Features:** Post sentiment analysis, audience engagement tracking, and ICP relevance scoring.

### Task 2: GTM Intelligence Platform
This prototype acts as an automated Go-To-Market research agent that researches **Stripe** to identify strategic shifts and provide actionable recommendations.

- **Features:** A robust RAG (Retrieval-Augmented Generation) pipeline ensures accuracy and prevents AI hallucinations by grounding all claims in verifiable source data.

### Tech Stack
- **Data Collection:** Apify API, Tavily Search API
- **AI & Orchestration:** OpenRouter (for LLMs), LangChain (for RAG)
- **Data & Dashboard:** Pandas, Streamlit
- **Core Language:** Python

---

## 👨‍💻 For Developers: How to Regenerate the Data (Optional)

This section is for developers who wish to re-run the entire data collection and analysis pipeline. **This requires API keys.**

1.  **Set up environment variables:**
    - Create a file named `.env` in the root of the project.
    - Add your secret API keys to this file:
      ```
      OPENROUTER_API_KEY=your_key_here
      TAVILY_API_KEY=your_key_here
      APIFY_API_TOKEN=your_key_here
      ```

2.  **Run the Jupyter Notebooks:**
    - The data for Task 1 was generated using a Jupyter Notebook that calls the Apify API.
    - The data for Task 2 was generated using a Jupyter Notebook that runs the RAG agent.
    - Executing the cells in these notebooks sequentially will regenerate the `.csv` and `.md` files in the `data/` directory.