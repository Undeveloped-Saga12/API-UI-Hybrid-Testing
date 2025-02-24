# API + UI Hybrid Testing 🔄

**Automate end-to-end workflows** by combining API calls (`requests`) and UI actions (Selenium).  
**Example**: Create a user via API, then log in via UI with the same credentials.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue) 
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange) 
![Requests](https://img.shields.io/badge/requests-2.0%2B-lightgrey)

---

## 🚀 Quick Start

1. **Clone & Install**:
   ```bash
   git clone https://github.com/your-username/api-ui-hybrid.git
   cd api-ui-hybrid
   pip install -r requirements.txt  # Selenium, pytest, requests

2. **Run Test**:
   ```bash
   pytest tests/test_hybrid.py -v

3. **🛠️ Project Structure**
   ```bash

    api-ui-hybrid/
    ├── tests/               # Test scripts
    ├── pages/               # UI page classes (e.g., login_page.py)
    ├── utils/               # API client & configs
    └── conftest.py          # Fixtures

4. **🌐 Test Workflow**
      ```bash
    API: Create a user (POST /users via Reqres.in).

    UI: Log in to SauceDemo with credentials.

    Assert: Verify successful login.

5. **Code Snippet**
    ```bash
    python
    def test_hybrid_api_ui_login(browser):
    api.create_user("John", "QA")          # API call
    login_page.login("standard_user", "secret_sauce")  # UI action
    assert login_page.is_dashboard_displayed()        # Assertion
    

6. **Key Features**:
     ```bash
  
    - Concise setup steps.  
    - Minimalist structure overview.  
    - Focused troubleshooting table.  
    - Embedded code snippets.  

Let me know if you need further tweaks! 😊
