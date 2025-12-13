# MyStoreAPI-Automation
# 🧪 E-commerce API Test Automation Framework

A professional-grade test automation framework for the FastAPI E-Commerce API. Features 68+ test cases with modular architecture, Allure reporting, and comprehensive coverage of authentication, products, carts, orders, and end-to-end workflows.

## 📋 Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Git

## 🚀 Quick Setup

### Step 1: Set Up the E-Commerce API

```bash
# Clone and run the FastAPI E-Commerce API
git clone https://github.com/salman415-462/dockerAPI
cd dockerAPI
docker build -t ecommerce-api .
docker run -d -p 9000:8000 --name ecommerce_container ecommerce-api

# Verify the API is running
curl http://localhost:9000/products/
API Access:

🌐 Main URL: http://localhost:9000

📄 API Docs: http://localhost:9000/docs

🛒 Products: http://localhost:9000/products/

Step 2: Set Up the Test Framework
bash
# Clone this test automation framework
git clone https://github.com/Ansi-A/MyStoreAPI-Automation
cd MyStoreAPI-Automation

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Step 3: Run the Tests
bash
# Run all tests with Allure reporting
pytest --alluredir=./allure-results

# Generate and view the test report
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report
📊 Test Coverage
68 test cases with 100% pass rate

5 test suites: Authentication, Products, Carts, Orders, Integration

Positive & negative testing with edge case coverage

JSON schema validation for API contracts

Dynamic test data generation

🏗️ Project Structure
text
MyStoreApi/
├── src/                    # Source modules (API clients, utilities)
├── tests/                  # Test suites organized by feature
├── logs/                   # Execution logs
├── allure-report/          # Generated Allure reports
├── requirements.txt        # Python dependencies
└── environment.properties  # Test environment configuration
🔧 Dependencies
text
requests          # HTTP client for API calls
pytest            # Test framework
allure-pytest     # Allure reporting integration
jsonschema        # JSON schema validation
faker             # Dynamic test data generation
jsonpath-ng       # JSON path parsing
📈 Features
Modular architecture with separated concerns

Professional Allure reporting with environment tracking

Structured logging per test module

Ready for CI/CD integration

Comprehensive API testing (authentication, CRUD, workflows)

🐳 Docker Commands Reference
bash
# Start the API
docker run -d -p 9000:8000 --name ecommerce_container ecommerce-api

# Stop the API
docker stop ecommerce_container

# Restart
docker start ecommerce_container

# View logs
docker logs ecommerce_container

# Check running containers
docker ps
📫 Contact
Salman - QA Automation Specialist
GitHub: github.com/Ansi-A
Project: github.com/Ansi-A/MyStoreAPI-Automation
Target API: github.com/salman415-462/dockerAPI
