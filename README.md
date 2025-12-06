<h1 align="center">🚀 AI Homework Evaluator (Manual + Test-Based Auto Evaluation)</h1>

<p align="center">
  <b>A Python homework checking system that evaluates code, runs test cases, scores students, and provides helpful feedback — no AI cost required.</b>
  <br>
  <sub>Flask • Python • Auto Testing • Feedback Generator</sub>
</p>

<hr>

<h2>📌 Overview</h2>

<p>
This tool allows students to upload their Python <b>.py</b> solutions.  
The system automatically tests the code against predefined test cases and generates structured feedback without requiring paid AI APIs.  

AI-integration support (OpenAI) is present in the code but disabled/commented —  
You can enable it anytime for AI-based evaluation.
</p>

<ul>
  <li>📁 Upload homework (.py file)</li>
  <li>🧪 Auto test execution + scoring</li>
  <li>📝 Manual rule-based feedback system </li>
  <li>🔒 No API key required (Free to use!)</li>
  <li>⚡ Optional AI mode already included in comments</li>
</ul>

<hr>

<h2>🛠 Tech Stack</h2>

<table>
<tr><td>⚙ Backend Framework</td><td><b>Flask</b></td></tr>
<tr><td>💻 Language</td><td><b>Python</b></td></tr>
<tr><td>🎨 UI</td><td><b>HTML + CSS</b></td></tr>
<tr><td>🧪 Testing Engine</td><td><b>Dynamic Python Test Execution</b></td></tr>
</table>

<hr>

<h2>📂 Project Structure</h2>

<pre>
📦 AI-Homework-Evaluator
├── app.py                     # Main Flask backend (Manual evaluation active)
│
├── templates/                 # Frontend pages
│   ├── index.html             # File upload interface
│   └── result.html            # Score + feedback output
│
├── static/
│   └── style.css              # Styling file for UI
│
├── test_cases/
│   └── sample_tests.py        # Test case logic (editable)
│
├── uploads/                   # Uploaded .py assignments (auto generated)
│
├── assets/                    # Images used in README (screenshots)
│   ├── home.png
│   └── result.png
│
├── README.md                  # Project Documentation
└── requirements.txt           # Python dependencies
</pre>

<hr>

<h2>⚙ Installation & Setup</h2>

<pre>
git clone https://github.com/your-username/repository-name.git
cd repository-name

# Create virtual environment
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Mac/Linux)

# Install dependencies
pip install -r requirements.txt

# Run Application
python app.py
</pre>

<p>Then open in browser:</p>

<pre>http://127.0.0.1:5000/</pre>

<hr>

<h2>📥 How it Works</h2>

<ol>
  <li>Upload your Python <code>.py</code> file</li>
  <li>App runs test cases automatically</li>
  <li>Score generated based on correctness</li>
  <li>Feedback shown instantly 🚀</li>
</ol>

<hr>

<h2>🖼 Screenshots</h2>

<p align="center">
  <img src="assets/home.png" width="650"><br>
  <b>📌 Home Upload Page</b>
</p>
<br>
<p align="center">
  <img src="assets/result.png" width="650"><br>
  <b>📌 Evaluation Result Output</b>
</p>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Enable AI feedback mode again (Gemini / OpenAI / Local LLM)</li>
  <li>Allow multiple functions & bigger projects</li>
  <li>Export evaluation report as PDF</li>
  <li>Leaderboard for classroom competition mode</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>
Contributions are welcome! Fork the repo, make improvements, and submit a pull request.
</p>

<hr>

<h3 align="center">Made with ❤️ for Students & Learning</h3>
