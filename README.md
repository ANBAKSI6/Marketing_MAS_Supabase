# Marketing AI Agent
Run using: streamlit run app.py
# 🚀 AI Marketing Assistant (Supabase + LangGraph)

## 📌 Overview

The **AI Marketing Assistant** is a full-stack intelligent application designed to automate marketing workflows such as:

* Logo generation 🎨
* Ad copy creation ✍️
* SEO keyword generation 🔍
* Email campaigns 📧
* Social media content 📱
* Marketing strategy planning 📊

The system leverages **AI agents orchestrated via LangGraph**, with **Supabase** for backend storage and authentication, and **Streamlit** for the user interface.

---

## 🏗️ Architecture

### 🔹 Frontend

* **Streamlit**

  * Multi-page UI (Home, Login, Chatbot)
  * Real-time chat interface

### 🔹 Backend

* **LangGraph**

  * Controls agent workflow
  * Routes user queries to appropriate tools

* **Agents**

  * Logo Agent (AWS Bedrock - Titan Image Generator)
  * Ad Copy Agent
  * SEO Agent
  * Marketing Strategy Agent
  * Email Campaign Agent

### 🔹 Database & Storage

* **Supabase**

  * Authentication (login/signup)
  * PostgreSQL database
  * Object storage (logos)

---

## 🔄 Data Flow

1. User logs in via **Supabase Auth**
2. User sends a query in chatbot
3. Query is passed to **LangGraph**
4. LangGraph decides which agent to trigger
5. Agent processes request:

   * Text → LLM (Bedrock)
   * Image → Titan Image Generator
6. Output is:

   * Displayed in UI (Streamlit)
   * Stored in Supabase (messages/logos)
7. Conversation history is maintained per user

---

## 📂 Project Structure

```
Marketing_MAS_Supabase/
│
├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_Login.py
│   ├── 3_Chatbot.py
│
├── agents/
│   ├── logo_agent.py
│   ├── ad_copy_agent.py
│   ├── seo_agent.py
│   ├── marketing_agent.py
│
├── graph/
│   └── graph.py
│
├── supabase_client.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ANBAKSI6/Marketing_MAS_Supabase.git
cd Marketing_MAS_Supabase
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🔐 Supabase Configuration

### Tables Used:

* **users** (managed by Supabase Auth)
* **conversations**
* **messages**

### Storage:

* Bucket: `logos`

### Row Level Security (RLS):

* Enabled for secure user-based data access

---

## 🤖 Key Features

✔ Multi-agent AI system
✔ Real-time chat interface
✔ Secure authentication
✔ Conversation history tracking
✔ AI-generated logos stored in cloud
✔ Modular and scalable architecture

---

## ⚠️ Known Challenges

* Image models may generate inconsistent text in logos
* API limits (AWS Bedrock / Supabase)
* Network-related errors during upload

---

## 🚀 Future Enhancements

* Better logo text rendering (vector-based)
* Dashboard analytics
* Multi-user collaboration
* Deployment on cloud (AWS/GCP)

---

## 👨‍💻 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python, LangGraph
* **AI Models:** AWS Bedrock (Titan, LLMs)
* **Database:** Supabase (PostgreSQL)
* **Storage:** Supabase Storage

---

## 📌 Author

**Anasua Baksi**
GitHub: https://github.com/ANBAKSI6

---

## ⭐ Conclusion

This project demonstrates how **AI agents + cloud backend + modern UI** can be combined to build a scalable **marketing automation platform**.

---
