# 🚀 Project Name - Gen AI-Based Data profiling challenge

## 📌 Table of Contents
- [Team](#team)
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)

---
## 👥 Team
- Managers - M Kumaraswamy, Santosh Sutar
- Team members - Rahul Sur, Sandeep Amin, Anil BL

## 🎯 Introduction
In banking domain involves manually defining profiling rules based on the underlying data and regulatory requirements. This challenge aims to automate data profiling using Generative AI (LLMs) and unsupervised machine learning techniques. We have developed a solution that can generate data profiling rules, perform adaptive risk scoring, and suggest remediation actions.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone -b main https://github.com/ewfx/gaidp-gen-ai-dudes.git
   ```
2. Install dependencies  
   ```sh
   pip3 install openapi pandas
   ```
3. Run the project  
   ```sh
   npm start  # or python app.py
   1. Input files = customer.csv and 01_instructions_prompt.txt
   2. Generate your own openAPI key and replace "api-key" wwith your key in 02_code_gen.py.
   3. Run the 02_code_gen.py on command prompt. It will prompt to enter the above instructions.
   4. The 02_code_gen.py will generate the python code to validate the data
   5. Copy the content and run it in cmd prompt. eg. 03_python_code_generated.py
   6. The 03_python_code_generated.py code will generate the validation_transactions.csv as output in the same directory.   
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: N/A
- 🔹 Backend: Python - run in mini conda prompt
- 🔹 Database: N/A
- 🔹 Other: OpenAI API (LLM)
