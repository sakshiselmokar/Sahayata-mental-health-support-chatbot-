# **Sahayata: AI-Powered Mental Health Support**  
🚀 **Sahayata** is an AI-driven mental health support system that leverages **Reddit data** to provide **personalized responses** and **real-time Retrieval-Augmented Generation (RAG)**. It is designed to offer guidance, emotional support, and relevant resources to users struggling with mental health challenges.

---

## 🌟 **Key Features**  
✅ **Real-time Reddit Data Fetching** – Extracts mental health-related posts from Reddit in real time.  
✅ **Personalized Responses** – Uses AI to generate empathetic and context-aware responses.  
✅ **Retrieval-Augmented Generation (RAG)** – Enhances AI responses by retrieving relevant Reddit discussions.  
✅ **AI Chatbot Interface** – Interactive chatbot built with **Streamlit** for easy access.  
✅ **Actionable Insights** – Provides insights and recommendations based on user queries.  

---

## 📌 **Workflow**  

### **1️⃣ Data Collection (Real-time Reddit Data Extraction)**  
- Uses **Pushshift API** & **PRAW (Python Reddit API Wrapper)** to fetch **live Reddit posts** from mental health-related subreddits.  
- Filters posts based on relevance (e.g., depression, anxiety, stress support).  

### **2️⃣ Text Preprocessing & Aspect Extraction**  
- Cleans the extracted text (removes noise, handles special characters).  
- Identifies **key aspects** (e.g., emotional distress, suicidal ideation, coping mechanisms).  

### **3️⃣ Retrieval-Augmented Generation (RAG) for Response Generation**  
- Retrieves relevant Reddit discussions using **Vector Search** (FAISS).  
- Generates **personalized AI responses** using **Microsoft Phi-2** or another LLM.  

### **4️⃣ AI Chatbot Interface (Streamlit-based UI)**  
- Users interact with the chatbot for **mental health support**.  
- The chatbot responds based on retrieved information and **LLM-generated responses**.  

---

## 🔧 **Tech Stack**  
- **🧠 AI Model**: Microsoft Phi-2 (LLM for response generation)  
- **📡 Data Fetching**: Pushshift API + PRAW (Reddit API)  
- **🔍 Vector Search**: FAISS (for efficient retrieval)  
- **🖥️ UI**: Streamlit (for chatbot interface)  
- **💾 Storage**: CSV for response logging  

---

## 🎥 **Demo Video**  
📌 **Click below to watch the demo**:  
[click here](https://github.com/sakshiselmokar/Sahayata-mental-health-support-chatbot-/blob/main/demo_video_of_project.mp4)** to view the video directly.

---

## 🚀 **How to Run**  

### **1️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Chatbot**  
```bash
streamlit run streamlit.py
```

---

## 🤝 **Contributing**  
We welcome contributions to **Sahayata**! Feel free to open an issue or submit a pull request.  

---

## 📜 **License**  
This project is licensed under the **MIT License**.  
