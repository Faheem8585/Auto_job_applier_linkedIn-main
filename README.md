# Automated LinkedIn Job Applier

An intelligent, heavily automated Python application designed to streamline the job hunt by autonomously applying to LinkedIn job listings. This project acts as a smart bot that parses LinkedIn's "Easy Apply" job portal, extracts relevant questions, and autonomously submits personalized applications.

## What This Project Is Used For

The primary work of this project is to save hundreds of hours of manual data-entry during the job application process. It can be used for:
- **Mass Applications**: Programmatically iterating through filtered job searches (e.g. Data Scientist, AI Engineer, ML Engineer).
- **Intelligent Form Filling**: Automatically answering Easy Apply questions utilizing configurable datasets, drop-downs, and file-inputs (such as resumes).
- **Bypassing Bot Detection**: Operating undetected by mimicking human interaction speed and behavior.

---

## Technologies Used & How They Are Implemented

This project relies on several core technologies that communicate together efficiently:

### 1. Python
The foundational programming language used for scripting the application logic, iterating through data, and reading configuration files.

### 2. Selenium & Undetected ChromeDriver
**How it's used**: Standard Selenium automation is natively blocked by LinkedIn and Cloudflare. To bypass this, this project implements an injected, patched `undetected_chromedriver` instance. 
It navigates the DOM, searches elements via XPATH, safely scrolls elements into viewport using JavaScript execution, and isolates the browser process. 

### 3. Artificial Intelligence Modules
**How it's used**: The project integrates LLM SDKs (`openai` for ChatGPT, `google-generativeai` for Gemini). These modular APIs parse complex open-ended job questions (ex: "How many years of database experience do you have?") from the web portal and synthesize intelligent, tailored answers using your resume data.

### 4. Evading Bot Detection (Stealth Behaviors)
**How it's used**: 
- **Human Typing**: Complex text fields are filled out using asynchronous delays (`random.uniform` sleeping intervals) explicitly mimicking human character-by-character typing. 
- **Smooth Scrolling**: Bypasses heuristic checks measuring instant or robotic screen tearing by forcing native, hardware-level smooth scrolling.
- **Minimum Application Timers**: Automatically calculates elapsed time to ensure each application finishes no faster than a genuine human applicant (typically locking rapid submissions behind a 60-120 second random delay buffer).

### 4. PyAutoGUI
**How it's used**: GUI framework utilized to prompt OS-level blocking alerts for interactions. This provides critical stop-points and timeouts so that users can manually intervene during unfamiliar questionnaires before the bot hits auto-submit.

### 5. Flask
**How it's used**: Leveraged as an optional graphical user interface to configure job titles, address parameters, and personal datasets locally (via `app.py`) natively on port `localhost:5000` rather than editing raw python arrays.

---

## How to Use This Project

### 1. Initial Setup
Ensure that you are running within a Python Virtual Environment (`.venv`) to properly sandbox dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuration
Instead of modifying variables blindly, run the local GUI server to manage the bot's behavior seamlessly.
```bash
.venv/bin/python app.py
```
*Visit `http://127.0.0.1:5000` in your browser to configure your details, application tracking, and custom job streams (e.g. AI roles, Software Engineering).*

### 3. Running the Bot
Once the application configuration represents your personal profile accurately, launch the autonomous applier:
```bash
.venv/bin/python runAiBot.py
```
This application works best when the user is already authenticated in Chrome on a guest or personal profile to bypass two-factor authentication restrictions. 
