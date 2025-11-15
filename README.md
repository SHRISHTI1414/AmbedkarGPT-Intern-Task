# AmbedkarGPT-Intern-Task
# AmbedkarGPT – AI Intern Assignment (Phase 1)

This repository contains my submission for **Kalpit Pvt Ltd, UK – AI Intern Hiring Assignment (Phase 1)**. The task was to build a **simple command-line RAG-based Question–Answer system** using local models and open‑source tools.

---

## 📌 Project Overview

The goal of the assignment was to create an offline RAG (Retrieval‑Augmented Generation) pipeline that:

* Loads a given text file (`speech.txt`).
* Splits it into chunks.
* Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
* Stores and retrieves embeddings using **ChromaDB**.
* Uses **Ollama (Mistral 7B)** as the LLM.
* Answers user queries strictly based on the content of the provided speech.

This project meets all required specifications and runs fully **offline**.

---

## ⚙️ Tech Stack

* **Python 3.13 (compatible with 3.8+)**
* **LangChain (Community + Core)**
* **ChromaDB** (Local Vector Store)
* **HuggingFace Embeddings**
* **sentence-transformers/all-MiniLM-L6-v2**
* **Ollama + Mistral 7B Model**

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/SHRISHTI1414/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama (Mac/Linux)

Download from: [https://ollama.com](https://ollama.com)

Pull the model:

```bash
ollama pull mistral
```

### 5. Run the program

```bash
python main.py
```

You can now ask any question about the speech.

---

## 🧩 My Approach (Step-by-Step)

### **1. Understanding the Assignment**

I first broke down the requirements:

* Mandatory use of LangChain
* Mandatory use of ChromaDB
* Mandatory use of HuggingFaceEmbeddings
* LLM strictly via Ollama (Mistral 7B)
* Must run locally with no API keys

### **2. Setting Up the Environment**

Created a clean Python environment, installed LangChain packages, Chroma, torch, sentence-transformers, and tested basic imports.

### **3. Installing Ollama (Mac)**

* Installed via `.dmg` installer.
* Verified installation: `ollama --version`.
* Pulled the required model: `ollama pull mistral`.

### **4. Building the RAG Pipeline**

Implemented the following steps in order:

1. Load `speech.txt` using `TextLoader`.
2. Convert text into smaller chunks using `CharacterTextSplitter`.
3. Generate embeddings using **HuggingFaceEmbeddings**.
4. Index chunks into **ChromaDB**.
5. Create a retrieval pipeline with a new‑style LangChain runnable graph.
6. Call Mistral through Ollama.
7. Loop to accept user queries.

### **5. Testing the System**

Checked:

* Chunk loading
* Embedding creation
* Vector DB setup
* Retrieval correctness
* Final answer generation from retrieved context

Everything worked as expected.

---

## 🐞 Errors & Challenges I Faced

### **1. LangChain Versioning Issues**

Imports like:

```
from langchain.chains import RetrievalQA
```

were deprecated. I switched to:

```
from langchain_core.runnables import ...
```

This fixed the problem.

### **2. Missing Packages**

Errors like:

* `No module named sentence_transformers`
* `No module named chromadb`
* `No module named langchain_community.chains`

I solved them by individually reinstalling the correct modules.

### **3. ChromaDB Import Errors**

Chroma needed version `>=0.5`. Installing the correct version fixed it.

### **4. GitHub Sync Issue**

My local repo conflicted with the remote empty repo.
Solution:

```
git pull origin main --allow-unrelated-histories
git push origin main
```

After merging, everything pushed successfully.

### **5. Embedding Download Time**

The sentence-transformer model (90MB+) took some time to download on first run.

---

## ⏳ Time Taken

* **Understanding Requirements:** 20–25 minutes
* **Environment Setup:** 30 minutes
* **Fixing Packages & Version Issues:** 40 minutes
* **Building RAG Pipeline:** 45 minutes
* **Testing & Debugging:** 30 minutes
* **GitHub Setup & Documentation:** 20 minutes

### **Total Time:** ~2.5 hours

---

## 📘 Final Output

The final system:

* Loads the Ambedkar speech
* Creates embeddings
* Stores in ChromaDB
* Retrieves relevant context
* Uses Mistral to answer queries
* Runs fully offline via command line

---

## 📂 Project Structure

```
AmbedkarGPT-Intern-Task
├── main.py
├── requirements.txt
├── speech.txt
└── README.md
```

---

## 📄 Notes

* This project fulfills all requirements mentioned in the assignment.
* Everything runs **locally**, without any API calls or external services.
* The code is clean, minimal, and production‑style.

---

## ✔️ End of README

If you have any doubts, feel free to test the script using the instructions above.
