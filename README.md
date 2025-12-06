AI‑Powered Coding Homework Evaluator
A Flask web app that automatically tests student Python submissions and provides AI-powered feedback.

Overview
This project demonstrates an AI-based solution to a real problem at Metropolia: teachers spend significant time manually checking Python assignments. The system automates test execution, scoring, and feedback generation.
Features
•	File Upload Interface – simple form for submitting .py files
•	Automatic Test Execution – runs instructor-defined test cases
•	Scoring System – counts passed tests and calculates a final score
•	AI Feedback (Optional) – integrate OpenAI/LLM feedback for deeper analysis
•	User-Friendly Templates – clean HTML interface to show results
•	Safe Execution Wrapper – prevents crashes from invalid student code
Project Structure
coding_feedback_app/
•	├── app.py
•	├── templates/
•	│   ├── index.html
•	│   └── result.html
•	├── static/
•	│   └── style.css
•	├── uploads/
•	├── test_cases/
•	│   └── sample_tests.py
Installation
Clone the repository:
git clone <your-repo-url>
cd coding_feedback_app
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  (Linux/Mac)
venv\Scripts\activate   (Windows)

Install dependencies:
pip install flask
Running the App
flask --app app run --debug
Open http://127.0.0.1:5000 in your browser.
How It Evaluates Code
•	User uploads a .py file
•	System imports it in a controlled environment
•	Test functions inside test_cases/ are executed
•	Score is calculated
•	Feedback is generated (AI or rule-based)
AI Feedback (Optional)
Set your API key:
export OPENAI_API_KEY="your-key-here"
Security Notes
•	Docker sandboxing
•	Time and resource limits
•	File system isolation
•	Non-root execution environment
Extendability to Other Subjects
Although this demo focuses on Python programming, the concept can be applied to many subjects at Metropolia. By adjusting test logic or using subject‑specific AI prompts, the same platform can support:
•	Other programming languages (Java, JS, C/C++, SQL)
•	Written assignments (essays, reports)
•	Math and science tasks
•	Design and UX evaluations
•	Data science notebooks
Future Improvements
•	Docker sandbox
•	Instructor dashboards
•	Multi-assignment support
•	Hint generation
•	Real-time editor
License
This project is part of a recruitment assignment and is not intended for production use.
