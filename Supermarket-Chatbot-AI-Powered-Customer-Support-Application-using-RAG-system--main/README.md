

# 🛒 Supermarket Chatbot

**A Retrieval-Augmented Generation (RAG) based chatbot for supermarket customer support.**

---

## 📜 Overview

The **Supermarket Chatbot** is a web-based application designed to assist supermarket customers by answering queries about:

* ✅ Product availability
* ✅ Prices
* ✅ Stock quantities
* ✅ Categories

It leverages **NLP, Semantic Search, and LLMs** to deliver accurate and friendly responses.
The chatbot uses a **Retrieval-Augmented Generation (RAG) pipeline**, combining **FAISS for semantic retrieval** and the **DeepSeek V3 0324 (free) LLM via OpenRouter** for natural language generation.

---

## 🎯 Purpose

* Improve customer experience with quick, accurate responses.
* Automate repetitive queries to reduce human workload.
* Offer **24/7 smart customer support**.

---

## 🌟 Features

* 🔍 **Semantic product search** using **FAISS** and **Sentence Transformers**.
* 💬 Natural language response generation using **DeepSeek V3 0324**.
* 🔄 **Fuzzy matching** for misspelled queries (`coka cola` → `Coca Cola`).
* ✨ Modern UI with chat bubbles and loading animations.
* 📄 Logging system for debugging and monitoring.

---

## 🛠️ Technologies Used

| Technology               | Usage                                |
| ------------------------ | ------------------------------------ |
| Flask                    | Backend Web Framework                |
| MySQL                    | Product Database                     |
| FAISS                    | Semantic Search Engine               |
| Sentence Transformers    | Embeddings Generation (MiniLM-L6-v2) |
| OpenRouter (DeepSeek V3) | LLM API for response generation      |
| FuzzyWuzzy               | Fuzzy string matching                |
| Python Libraries         | requests, dotenv, numpy, watchdog    |

---

## 📂 Project Structure

```
Supermarket-Chatbot/
├── data/
│   ├── faiss_index/
│   └── mappings/
├── src/
│   ├── app.py
│   ├── build_index.py
│   ├── db_connect.py
│   ├── rag_pipeline.py
│   └── utils.py
├── templates/
│   └── chatbot.html
├── .env
├── supermarket_chatbot.log
├── README.md
└── workflow_diagram.png
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* MySQL installed and configured
* OpenRouter API Key (for **DeepSeek V3 0324 free model**)

---

### 🔧 Installation Steps

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd Supermarket-Chatbot
```

#### 2. Set Up a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install flask mysql-connector-python faiss-cpu sentence-transformers requests fuzzywuzzy python-dotenv watchdog numpy
```

#### 4. Configure MySQL Database

* Start MySQL server.
* Create Database and Table:

```sql
CREATE DATABASE Supermarket;
USE Supermarket;

CREATE TABLE Product_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    category VARCHAR(100),
    description TEXT
);

INSERT INTO Product_details (name, price, stock_quantity, category, description)
VALUES 
    ('Orange (1kg)', 3.50, 40, 'Fruits', 'Fresh oranges, 1kg pack'),
    ('Coca Cola', 1.99, 50, 'Beverages', 'A refreshing cola drink'),
    ('Apple (1kg)', 2.99, 40, 'Fruits', 'Fresh apples, 1kg pack'),
    ('Banana (1 dozen)', 1.50, 60, 'Fruits', 'Fresh bananas, 1 dozen');
```

* Update **`src/db_connect.py`** with your credentials.

#### 5. Configure Environment Variables

Create a `.env` file:

```bash
DEEPSEEK_API_KEY=your_openrouter_api_key
LLM_MODEL=deepseek/deepseek-chat-v3-0324:free
```

#### 6. Build the FAISS Index

```bash
python src/build_index.py
```

#### 7. Run the Application

```bash
python src/app.py
```

#### 8. Access the Chatbot

Visit:

```
http://localhost:5000
```

---

## 🧪 Testing the Chatbot

| Query                                | Expected Response                                                      |
| ------------------------------------ | ---------------------------------------------------------------------- |
| How much is Orange (1kg)?            | The price of Orange (1kg) is \$3.50.                                   |
| Do you have Coca Cola in stock?      | Yes, we have Coca Cola in stock! We have 50 units available at \$1.99. |
| List out the available product list. | Here are some available products: Apple, Banana, Coca Cola, Orange...  |
| How much is coka cola?               | The price of Coca Cola is \$1.99.                                      |

---

## 🛠 Debugging Tips

* Check `supermarket_chatbot.log`.
* Ensure MySQL is running and database is populated.
* Verify your OpenRouter API Key is valid.

---

## 🔮 Future Improvements

* Add support for discounts and offers.
* Expand product database (100+ items).
* Enhance UI with voice input and product images.
* Support complex questions (e.g., price comparisons).

---

## 📞 Contact

Developed by: **Naveen Kumar**
📧 naveenpalani75@gmail.com


