# 🛒 MyStoreAPI – Production-Style E-Commerce Backend & API Automation Framework

 [![API Test Automation](https://github.com/Ansi-A/MyStoreAPI-Automation/actions/workflows/api-tests.yml/badge.svg)](https://github.com/Ansi-A/MyStoreAPI-Automation/actions/workflows/api-tests.yml)
 
- Automated regression suite runs on every push using GitHub Actions.


A realistic E-Commerce REST API system built with FastAPI and tested using a scalable, CI/CD-ready API automation framework powered by pytest + Allure.

This project demonstrates backend development, API automation architecture, Docker containerization, and real-world QA engineering practices.

---

## 🚀 Project Overview

This system consists of **two repositories**:

1. **FastAPI E‑Commerce Backend** – The actual backend API
2. **MyStoreAPI Automation Framework** – Automated API testing suite

The backend simulates a **real‑world e‑commerce system** with:

* Users & Authentication
* Products
* Carts
* Orders
* End‑to‑end purchase workflows

---

## 🧠 Architecture (High Level)

```
Test Client (pytest / requests / curl)
        ↓
     REST API (FastAPI)
        ↓
   In-memory / mock data (lists, dicts, JSON)

```

* Backend exposes **REST endpoints**
* Clients interact via **HTTP (JSON)**
* Authentication via **JWT tokens**
* Fully containerized with **Docker**

---

## 📦 Repository 1: FastAPI E‑Commerce API

### 🔗 Clone & Run the API

```bash
git clone https://github.com/salman415-462/dockerAPI
cd dockerAPI
```

### 🐳 Build & Run with Docker

```bash
docker build -t ecommerce-api .
docker run -d -p 9000:8000 --name ecommerce_container ecommerce-api
```

### ✅ Verify API is Running

```bash
curl http://localhost:9000/products/
```

---

## 🌐 API Access

* **Base URL:** [http://localhost:9000](http://localhost:9000)
* **Swagger Docs:** [http://localhost:9000/docs](http://localhost:9000/docs)

### Core Endpoints

* 🛒 Products → `GET /products/`
* 👤 Users → `POST /users/`
* 🧺 Carts → `POST /carts/`
* 📦 Orders → `POST /orders/`

---

## 🧪 Repository 2: API Automation Framework

### 🔗 Clone the Automation Project

```bash
git clone https://github.com/Ansi-A/MyStoreAPI-Automation
cd MyStoreAPI-Automation
```

### 🐍 Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Tests

### Execute All Tests with Allure Reporting

```bash
pytest --alluredir=./allure-results
```

### Generate & Open Report

```bash
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report
```

---

## 📊 Test Coverage

* ✅ **68 automated test cases**
* 🧩 **5 test suites**:

  * Authentication
  * Products
  * Carts
  * Orders
  * Integration workflows

### Testing Includes

* Positive & negative scenarios
* Edge‑case validation
* JSON schema validation
* Dynamic test data generation
* End‑to‑end e‑commerce flows

---

## 🏗️ Automation Project Structure

```
MyStoreAPI-Automation/
├── src/                    # API clients & core utilities
├── tests/                  # Feature‑based test suites
├── logs/                   # Execution logs
├── allure-report/          # Generated test reports
├── requirements.txt        # Dependencies
└── environment.properties  # Environment configuration
```

---

## 🔧 Key Dependencies

```
requests          # HTTP client
pytest            # Test execution framework
allure-pytest     # Reporting integration
jsonschema        # API contract validation
faker             # Test data generation
jsonpath-ng       # JSON parsing & assertions
```

---

## ⭐ Key Features

* Modular & scalable test architecture
* Clean separation of concerns
* Professional Allure reports
* Structured logging per module
* CI/CD‑ready design
* Covers CRUD + complex workflows

📸 Allure Reporting (Sample)


  -1-
  
  <img width="1920" height="895" alt="image" src="https://github.com/user-attachments/assets/66f32225-0a55-4f63-b594-694250dd8f90" />

  -2-

  <img width="1920" height="895" alt="image" src="https://github.com/user-attachments/assets/eb25f0c0-759a-4370-a718-f512ba98988f" />

  -3-

  <img width="1920" height="895" alt="image" src="https://github.com/user-attachments/assets/0adb7240-1ab9-4441-8142-a3311e118672" />



---

## 🐳 Docker Command Reference

```bash
# Start container
docker run -d -p 9000:8000 --name ecommerce_container ecommerce-api

# Stop container
docker stop ecommerce_container

# Restart container
docker start ecommerce_container

# View logs
docker logs ecommerce_container

# List running containers
docker ps
```
---

This project demonstrates:


* ✅ Dockerized production setup
* ✅ Professional API automation
* ✅ CI/CD‑ready testing strategy
  
  

---

## 📫 Contact

**Salman**
QA Automation

* GitHub (Automation): [https://github.com/Ansi-A/MyStoreAPI-Automation](https://github.com/Ansi-A/MyStoreAPI-Automation)
* GitHub (API): [https://github.com/salman415-462/dockerAPI](https://github.com/salman415-462/dockerAPI)

---

> *“This project is not just API testing — it is testing a complete system.”*
