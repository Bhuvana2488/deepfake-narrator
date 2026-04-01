# 🎙️ AI Web Narrator with Chatbot (RAG Enabled)

## 📌 Overview

The **AI Web Narrator** is a smart web application that can:

* Read webpage content
* Understand it using AI
* Speak it out loud in a natural human voice

It combines **chatbot intelligence + voice narration** to create an interactive and accessible user experience.

---

## 💡 What Problem Does It Solve?

Many users:

* Prefer listening instead of reading
* Want quick summaries of content
* Need interactive explanations

This system solves that by:
👉 Converting webpage content into **speech + intelligent responses**

---

## 🚀 Key Features

* 🔍 Extracts visible text from any webpage
* 🤖 AI chatbot answers user queries
* 📚 Uses RAG (Retrieval-Augmented Generation) for better responses
* 🔊 Converts text into realistic human-like voice
* ⚡ Works in real-time with a simple button click

---

## 🧠 How It Works (Simple Explanation)

### Step-by-step flow:

```text id="4l7h9v"
1. User clicks a button  
2. System extracts visible text from the webpage  
3. Text is sent to an AI chatbot  
4. Relevant information is retrieved from a knowledge file (RAG)  
5. AI generates a meaningful response  
6. Response is converted into speech  
7. Audio is played in the browser
```

---

## 🏗️ System Architecture

```text id="ffj5b9"
Frontend (Browser)
   ↓
Flask Backend (Python)
   ↓
Chatbot API (OpenAI)
   ↓
RAG (knowledge.txt)
   ↓
Text-to-Speech API (ElevenLabs)
   ↓
Audio Output (User hears voice)
```

---

## 🛠️ Technologies Used

* **Python & Flask** → Backend development
* **JavaScript** → Extracting webpage text
* **OpenAI API** → Chatbot responses
* **ElevenLabs API** → Voice generation
* **RAG Concept** → Improves response quality

---

## 📂 Project Structure

```text id="z7bc7u"
project/
│── app.py              # Handles backend + voice generation
│── chatbot.py          # Chatbot + RAG logic
│── knowledge.txt       # Local knowledge base
│── index.html
│── script.js

```

---

## 📸 Results

### 🔹 Figure 1: Chatbot Response + Voice Narration
![Chatbot Response and Voice Narration](Screenshot%202026-04-01%20154855.png)

The chatbot answers user queries related to AI/ML and project context using AI + retrieved knowledge.
The system narrates webpage content (Vision/Mission) when the button is clicked

---

### 🔹 Figure 2: Voice Narration + Error Handling
![Chatbot Response](Screenshot%202026-04-01%20154936.png)
* The chatbot handles unclear queries gracefully by asking for clarification


## 🔥 Key Highlights

* Combines **multiple AI technologies in one system**
* Implements a **complete end-to-end pipeline**
* Uses **real-world APIs instead of just theory**
* Designed for **usability and accessibility**

---

## ⚠️ Limitations

* RAG is basic (keyword-based, not embeddings)
* Works best for project-specific queries
* Can be improved with vector databases

---

## 🚧 Future Improvements

* Use embeddings for better search
* Add multilingual voice support
* Improve chatbot memory
* Stream audio instead of file download


---

## 👩‍💻 Author

**Bhuvana R Raj**
Artificial Intelligence & Machine Learning Engineer
