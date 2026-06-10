#  Solaris AI Financial Advisor

Solaris is a personal finance management application built using Streamlit, Gemini, LangChain, FAISS, SQLite, and OCR technologies. The platform helps users track expenses, manage financial goals, analyze spending habits, and receive personalized financial recommendations. By combining traditional financial management features with Generative AI and Retrieval-Augmented Generation (RAG), the application provides intelligent and context-aware financial guidance.

The system is designed as an end-to-end solution where users can upload expenses, import bank statements, maintain a financial profile, build a custom financial knowledge base, and generate AI-powered insights from their financial data.

---

##  Features

###  Interactive Dashboard
- Displays monthly income, expenses, savings, and savings percentage.
- Shows goal progress with completion tracking.
- Provides recent transaction history and expense summaries.
- Gives users a quick overview of their financial health.

###  Expense Screenshot Upload
- Upload payment screenshots or receipts.
- Extract transaction details using OCR.
- Automatically identify merchant names and amounts.
- Categorize expenses before storing them in the database.

###  Bank Statement Analysis
- Import bank statements in CSV format.
- Automatically process and store transactions.
- Categorize spending into meaningful groups.
- Analyze spending patterns across categories.

###  Goal Management
- Create and manage financial goals.
- Track target amounts, savings progress, and deadlines.
- Monitor goal completion through progress indicators.
- Receive AI recommendations related to financial objectives.

###  User Profile Management
- Store personal and financial details.
- Maintain income, occupation, age, risk appetite, and goals.
- Use profile information to generate personalized advice.

###  AI Financial Advisor
- Analyze expenses, income, savings, and goals.
- Generate personalized recommendations using Gemini.
- Suggest saving strategies and spending improvements.
- Provide investment suggestions based on risk tolerance.

###  Financial Knowledge Base
- Upload finance-related PDF documents.
- Build a searchable knowledge repository.
- Support investment guides, tax resources, finance books, and planning documents.
- Enhance AI responses using user-provided financial knowledge.

###  Finance Chat (RAG)
- Ask questions about budgeting, saving, investing, and personal finance.
- Retrieve relevant information from uploaded documents.
- Generate context-aware responses using Gemini and FAISS retrieval.

###  PDF Report Generation
- Generate downloadable financial reports.
- Summarize expenses, savings, and goals.
- Include AI-generated recommendations and insights.
- Provide a professional overview of financial performance.

---

##  System Architecture

The application integrates multiple AI and data-processing components into a unified workflow. Expense screenshots are processed through OCR, bank statements are imported through CSV processing, and uploaded financial documents are converted into vector embeddings for semantic retrieval. User profiles, expenses, and goals are stored in SQLite, while Gemini generates recommendations and answers based on both financial data and retrieved knowledge.

```text
User Input
     │
     ├── Expense Screenshots
     ├── Bank Statements
     ├── Financial Documents
     │
     ▼
Data Processing Layer
(OCR, CSV Parsing, PDF Processing)
     │
     ▼
SQLite Database + FAISS Vector Store
     │
     ▼
AI Financial Advisor & Finance Chat
     │
     ▼
Insights, Recommendations & Reports
```

---

##  Technology Stack

Frontend : Streamlit 
Database : SQLite 
AI Model : Gemini 2.5 Flash 
RAG : LangChain, FAISS 
Embeddings : Sentence Transformers (all-MiniLM-L6-v2) 
OCR : Tesseract, OpenCV, Pillow 
Data Processing : Pandas, NumPy 
Reporting : ReportLab 

---

##  Project Structure

```text
Solaris/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── database/
├── modules/
├── pages/
├── rag/
│
├── uploads/
├── reports/
└── data/
```

---

##  Installation

Clone the repository and create a virtual environment.

```bash
git clone <repository-url>
cd Solaris

python -m venv venv
venv\Scripts\activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Install Tesseract OCR and ensure it is available in your system PATH.

Run the application:

```bash
streamlit run app.py
```

---

##  Future Improvements

Future enhancements may include user authentication, real-time bank integrations, portfolio tracking, budget alerts, predictive financial analytics, and cloud deployment. Additional AI capabilities such as voice-based assistance and automated financial planning can further improve the platform.

---

##  Learning Outcomes

This project demonstrates practical implementation of OCR, database management, financial analytics, vector databases, Retrieval-Augmented Generation (RAG), prompt engineering, and Generative AI integration. It showcases how modern AI technologies can be combined with traditional software engineering practices to build a complete intelligent financial assistant.