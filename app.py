import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import importlib.util

# ===============================
#  ⚠ AI SECTION DISABLED BY DEFAULT
# ===============================
# from dotenv import load_dotenv
# import openai
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# from openai import OpenAI
# client = OpenAI()
# def ai_feedback(student_code):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful coding tutor."},
#                 {"role": "user", "content": f"Analyze this Python code and suggest improvements:\n{student_code}"}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"AI feedback error: {e}"
# ===============================
#  End of AI Block (Manual Mode)
# ===============================

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["UPLOAD_FOLDER"] = "uploads"
ALLOWED_EXTENSIONS = {"py"}

# Validate file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------------- MANUAL FEEDBACK ENGINE ----------------------
def rule_based_feedback(code_text):
    feedback = ["=== Manual Feedback Without AI ===\n"]

    # Check function existence
    if "def add(" not in code_text:
        feedback.append("❗ Missing function: add()")
    else:
        feedback.append("✔ Function add() exists")

    # Check for return
    if "return" not in code_text:
        feedback.append("⚠ No return statement found — function may output nothing")

    # Check for docstring (optional improvement)
    if '"""' not in code_text:
        feedback.append("💡 Add a docstring for better documentation")

    # Check naming conventions
    if "add" in code_text and "def add(" in code_text:
        feedback.append("💡 Optional: Validate input type inside add(x, y)")

    return feedback

# Read uploaded code
def read_student_code(filepath):
    with open(filepath, "r") as f:
        return f.read()

# Run test suite
def run_tests(filepath):
    import test_cases.sample_tests as tests   # your original import fixed to stable import
    results = {"passed": 0, "failed": 0, "total": 0, "errors": []}
    module_name = "student"
    spec = importlib.util.spec_from_file_location(module_name, filepath)

    try:
        student = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student)
    except Exception as e:
        results.update(total=1, failed=1)
        results["errors"].append(f"Import failed — code error: {e}")
        return results

    test_functions = [
        func for func in dir(tests)
        if callable(getattr(tests, func)) and func.startswith("test_")
    ]

    results["total"] = len(test_functions)

    for test in test_functions:
        try:
            if getattr(tests, test)(student):
                results["passed"] += 1
            else:
                results["failed"] += 1
        except Exception as e:
            results["failed"] += 1
            results["errors"].append(f"{test} crashed: {e}")

    return results

# ================= ROUTES =================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file or file.filename == "":
        flash("Upload a .py file first!", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Only Python (.py) files allowed!", "error")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    
    return redirect(url_for("result", filename=filename))

@app.route("/result")
def result():
    filename = request.args.get("filename")
    if not filename:
        return redirect(url_for("index"))

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    test_results = run_tests(filepath)
    code_text = read_student_code(filepath)

    feedback = rule_based_feedback(code_text)

    # Uncomment if you re-enable GPT later:
    # feedback.append("\n--- AI Suggestions ---\n")
    # feedback.append(ai_feedback(code_text))

    score = int((test_results["passed"]/test_results["total"])*100) if test_results["total"] > 0 else 0

    return render_template("result.html", filename=filename, score=score, test_results=test_results, feedback=feedback)

if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    app.run(debug=True)
