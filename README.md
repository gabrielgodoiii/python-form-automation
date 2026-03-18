# 🤖 Automated Form Filling with Python

This project demonstrates how to **automatically fill a web form using Python automation**, reading structured product data directly from a cloud spreadsheet.

The automation collects product information submitted through **Google Forms**, stores the responses in **Google Sheets**, and then uses Python to automatically submit this data into a web system.

This project was developed as part of my practical learning journey in **Python, Automation, and Data Handling**.

---

# Automation Demo

![Automation Demo](images/automacao.gif)

---

# Project Overview

Many business workflows require **manually transferring data from spreadsheets into web systems**, which is repetitive and prone to human error.

This project solves that problem by building a **Python automation script** that:

- Reads product data directly from **Google Sheets**
- Iterates through each row of data
- Automatically fills out a web form
- Submits the product information without manual typing

The workflow integrates **form data collection, cloud spreadsheets, and Python automation**.

---

# Data Collection with Google Forms

The first step of the process is collecting product information through **Google Forms**.

Users fill out a form containing fields such as:

- Product Code  
- Product Brand  
- Product Type  
- Product Category  
- Unit Price  
- Product Cost  
- Additional Notes  

All responses are automatically stored in **Google Sheets**, creating a structured dataset ready to be processed by Python.

---

# Data Source: Google Sheets

Instead of using a local CSV file, the automation reads the dataset **directly from Google Sheets**.

This means that:

- The dataset is always **up to date**
- No manual file downloads are required
- The automation can run using the latest data from the spreadsheet

The spreadsheet acts as a **live database for the automation process**.

---

# Python Automation

The automation script was built using **Python** and simulates user interaction with the browser.

The script performs the following actions:

1. Opens the browser  
2. Accesses the target web system  
3. Performs login  
4. Reads product data from Google Sheets  
5. Iterates through each row of the dataset  
6. Automatically fills the form fields  
7. Submits the product information  

This eliminates repetitive manual work and ensures consistent data entry.

---

# Technologies Used

- Python  
- Pandas  
- PyAutoGUI  
- Google Forms  
- Google Sheets  

---

# 📁 Project Structure
```text
python-form-automation
│
├── automacao.py
├── README.md
└── requirements.txt
```
---

# Objective

The goal of this project is to demonstrate practical skills in:

- Python automation  
- Data handling with Pandas  
- Integration with cloud-based data sources  
- Workflow automation  
- Reducing manual repetitive tasks  

This type of automation is commonly used in **business operations, data pipelines, and process automation**.

---

# Future Improvements

Possible improvements include:

- Replacing GUI automation with **browser automation using Selenium**
- Creating a **scheduled automation pipeline**
- Implementing **error handling and logging**
- Deploying the automation as a **background job**

---

# 👨‍💻 Author

**Gabriel Godoi**

🇧🇷 Brasileiro | Analista de Dados em formação

Atualmente, estou desenvolvendo projetos práticos utilizando **Python, Análise de Dados e Automação** para adquirir experiência real na área de dados.

🔗 LinkedIn  
https://www.linkedin.com/in/gabriel-godoi-298005363  

🔗 GitHub  
https://github.com/gabrielgodoiii
