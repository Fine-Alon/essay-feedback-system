# 📝 CyberPro Essay Feedback System

A server-side application built with **FastAPI**, featuring a client interface for the automated checking and analysis of English-language essays. The system allows users to register, upload their texts (either directly or via `.txt` files), and receive a detailed structural analysis of their writing.

## ✨ Key Features

* **User Authorization:** Registration, secure login, and session management.
* **Essay Uploads:** Support for direct text input and `.txt` file uploads.
* **Local Data Storage:** Utilizes `pathlib` for the reliable storage of user profiles and essay texts in JSON format.
* **In-depth Text Analysis:**
  * Calculation of general metrics (word count, paragraph count).
  * Verification of minimum length requirements.
  * Identification of structural formatting issues (double spaces, missing punctuation at the end of paragraphs, incorrect spacing around punctuation marks).
  * Detection and counting of frequently repeated words.
* **Client Interface (UI):** A lightweight frontend built with vanilla HTML/JS/CSS (`index.html`) that interacts with the API via asynchronous `fetch` requests.

---

## 🛠 Tech Stack

* **Backend:** Python 3, FastAPI, Uvicorn
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Storage:** Local file system (JSON)

---

## 📂 Project Structure

The project is divided into logical modules corresponding to the development team's areas of responsibility:

```text
essay-feedback-system/
├── data/                  # Local "database" (JSON)
│   ├── essays/            # Saved texts and analysis reports
│   └── users/             # User profiles
├── models/                # Any models
│   ├── users.py           # User profile model (Omri)
├── routers/               # API Routes (Endpoints)
│   ├── analysis.py        # Essay analysis logic (Oren)
│   ├── essays.py          # Upload and storage logic (Alon)
│   └── users.py           # Registration and authorization (Omri)
├── services/              # Business logic and storage operations
│   ├── storage.py         # CRUD operations with files (pathlib)
│   └── text_checker.py    # Text validation and analysis algorithms
├── utils/                 # Helpers
│   ├── id_generator.py    # Reusable ID generator 
├── constants.py           # Important constants 
├── index.html             # Client application (Frontend)
├── main.py                # FastAPI entry point
└── requirements.txt       # Python dependencies
```

---

## 🚀 API Endpoints

Ниже представлен список основных маршрутов для взаимодействия с системой.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/users/register` | Register a new user |
| `POST` | `/users/login` | Log into the system |
| `GET`  | `/users/profile/{username}` | profile dashboard route |
| `POST` | `/essays/upload/file` | Upload an essay file (.txt) |
| `POST` | `/essays/upload/text` | Upload an essay text |
| `GET`  | `/{essay_id}` | Retrieve the essay record |
| `GET`  | `/api/analysis/essay/{essay_id}` | Retrieve the analysis report |

---

## 👥 Development Team

This project was built collaboratively, with responsibilities divided across core domains:

* 🔐 **Users API** *Registration and authorization infrastructure.*
* 💻 **Essays API & Client UI** *File storage, routing, and frontend interface development.*
* ⚙️ **Analysis API** *Text validation and parsing algorithms.*


