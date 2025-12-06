<h1 align="center">📝 AI‑Powered Coding Homework Evaluator</h1>
<p align="center"><em>A Flask web app that automatically tests student Python submissions and provides AI-powered feedback.</em></p>

---

<h2>🔹 Overview</h2>
<p>This project demonstrates an AI-based solution to a real problem at <b>Metropolia</b>: teachers spend significant time manually checking Python assignments.</p>
<p>The system automates <b>test execution</b>, <b>scoring</b>, and <b>feedback generation</b>.</p>

---

<h2>🚀 Features</h2>
<ul>
  <li><b>File Upload Interface</b> – simple form for submitting <code>.py</code> files</li>
  <li><b>Automatic Test Execution</b> – runs instructor-defined test cases</li>
  <li><b>Scoring System</b> – counts passed tests and calculates a final score</li>
  <li><b>AI Feedback (Optional)</b> – integrate OpenAI/LLM feedback for deeper analysis</li>
  <li><b>User-Friendly Templates</b> – clean HTML interface to show results</li>
  <li><b>Safe Execution Wrapper</b> – prevents crashes from invalid student code</li>
</ul>

---

<h2>📂 Project Structure</h2>
<pre>
coding_feedback_app/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── uploads/
├── test_cases/
│   └── sample_tests.py
</pre>

---

<h2>🛠 Installation</h2>

<h3>1️⃣ Clone the repository</h3>
<pre>
git clone &lt;your-repo-url&gt;
cd coding_feedback_app
</pre>

<h3>2️⃣ Create and activate a virtual environment</h3>
<pre>
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
</pre>

<h3>3️⃣ Install dependencies</h3>
<pre>
pip install flask
</pre>

---

<h2>▶️ Running the App</h2>
<pre>
flask --app app run --debug
</pre>
<p>Open your browser at: <b>http://127.0.0.1:5000</b></p>

---

<h2>🧪 How It Evaluates Code</h2>
<ul>
  <li>User uploads a <code>.py</code> file</li>
  <li>System imports it in a controlled environment</li>
  <li>Test functions inside <code>test_cases/</code> are executed</li>
  <li>Score is calculated</li>
  <li>Feedback is generated (<b>AI or rule-based</b>)</li>
</ul>

---

<h2>🤖 AI Feedback (Optional)</h2>
<p>Set your API key:</p>
<pre>
export OPENAI_API_KEY="your-key-here"
</pre>

---

<h2>🔐 Security Notes</h2>
<ul>
  <li>Docker sandboxing</li>
  <li>Time and resource limits</li>
  <li>File system isolation</li>
  <li>Non-root execution environment</li>
</ul>

---

<h2>📚 Extendability to Other Subjects</h2>
<p>Although this demo focuses on Python programming, the concept can be applied to many subjects at <b>Metropolia</b>. By adjusting test logic or using subject-specific AI prompts, the same platform can support:</p>
<ul>
  <li>Other programming languages (Java, JS, C/C++, SQL)</li>
  <li>Written assignments (essays, reports)</li>
  <li>Math and science tasks</li>
  <li>Design and UX evaluations</li>
  <li>Data science notebooks</li>
</ul>

---

<h2>✨ Future Improvements</h2>
<ul>
  <li>Docker sandbox</li>
  <li>Instructor dashboards</li>
  <li>Multi-assignment support</li>
  <li>Hint generation</li>
  <li>Real-time editor</li>
</ul>

---

<h2>📄 License</h2>
<p>This project is part of a <b>recruitment assignment</b> and is <b>not intended for production use</b>.</p>
