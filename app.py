from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logs')
def logs():
    if 'username' not in session:
        return redirect(url_for('login'))
    logs = ["Applied to: Data Analyst @ Google", "Applied to: Business Analyst @ Amazon"]
    return render_template('logs.html', logs=logs)

@app.route('/generate-cover-letter', methods=['GET', 'POST'])
def generate_cover_letter():
    if 'username' not in session:
        return redirect(url_for('login'))

    generated_letter = None
    if request.method == 'POST':
        job_description = request.form['job_description']
        cv_summary = """
Oloruntoba Anate — Business & Financial Analyst with 8+ years experience in ICT system integration, business process optimization, and financial modeling. Proficient in Power BI, ERP systems, and stakeholder collaboration with a track record of reducing reporting time by 30% and increasing efficiency by 20%.
"""

        # Placeholder for real OpenAI integration
        generated_letter = f"""Dear Hiring Manager,\n\nBased on your job description for a {job_description.strip()}, I believe I’m an excellent fit given my 8+ years of experience in financial analysis and ICT systems integration.\n\nI've led Power BI automation projects, reduced costs by 15%, and supported executive decision-making through data.\n\nI'd welcome the opportunity to bring similar value to your team.\n\nSincerely,\nOloruntoba Anate"""

    return render_template('generate_cover_letter.html', generated_letter=generated_letter)

@app.route('/auto-apply', methods=['GET', 'POST'])
def auto_apply():
    if 'username' not in session:
        return redirect(url_for('login'))

    applied_jobs = []
    if request.method == 'POST':
        keywords = request.form['keywords']
        # Simulate job applications (in real use, connect to LinkedIn with Selenium)
        applied_jobs = [f"{keywords} Analyst @ Company {i+1}" for i in range(10)]

    return render_template('auto_apply.html', applied_jobs=applied_jobs)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)