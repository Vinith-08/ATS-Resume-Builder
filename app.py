"""
Flask application - AI-Powered ATS Resume Builder
All routes and backend logic.
"""

import os
import json
from flask import (Flask, render_template, request, redirect,
                   url_for, flash, jsonify, send_file, session)
from io import BytesIO

import database as db
import ats_engine as ats
import resume_generator as rg

from jinja2 import ChoiceLoader, FileSystemLoader, DictLoader

# --- Self-Extracting Frontend Assets (Zero-Folder-Upload Required) ------------
try:
    import templates_bundle
    templates_bundle.extract_all()
    _in_memory_templates = {
        k.replace('templates/', ''): v for k, v in templates_bundle.ASSETS.items() if k.startswith('templates/')
    }
except Exception as _e:
    print(f"Templates bundle notice: {_e}")
    _in_memory_templates = {}

# --- App Setup ----------------------------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

template_paths = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'Templates'),
    BASE_DIR,
]

static_dir = os.path.join(BASE_DIR, 'static')
if not os.path.exists(static_dir) and os.path.exists(os.path.join(BASE_DIR, 'Static')):
    static_dir = os.path.join(BASE_DIR, 'Static')

app = Flask(__name__, static_folder=static_dir)
app.secret_key = 'ats_resume_builder_secret_2024'

# Multi-path Jinja loader: searches memory, 'templates/', 'Templates/', and root
loaders = [DictLoader(_in_memory_templates)]
for p in template_paths:
    if os.path.exists(p):
        loaders.append(FileSystemLoader(p))
app.jinja_loader = ChoiceLoader(loaders)

# Ensure upload folder exists
UPLOAD_FOLDER = os.path.join(static_dir, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Init database on startup
with app.app_context():
    db.init_db()

# --- Helpers -----------------------------------------------------------------

def extract_text_from_file(file):
    """Extract text from uploaded PDF or DOCX file."""
    filename = file.filename.lower()
    try:
        if filename.endswith('.pdf'):
            try:
                from pypdf import PdfReader
                from io import BytesIO
                reader = PdfReader(BytesIO(file.read()))
                text = '\n'.join(
                    page.extract_text() or '' for page in reader.pages
                )
                return text
            except ImportError:
                return '[PDF reading not available - paste your resume text manually]'
        elif filename.endswith('.docx'):
            try:
                from docx import Document
                from io import BytesIO
                doc = Document(BytesIO(file.read()))
                text = '\n'.join(para.text for para in doc.paragraphs)
                return text
            except ImportError:
                return ''
    except Exception:
        return ''
    return ''

# --- Routes -------------------------------------------------------------------

@app.route('/')
def dashboard():
    """Landing dashboard with stats."""
    try:
        resumes = db.get_all_resumes()
        stats = db.get_stats()
        return render_template('index.html', resumes=resumes, stats=stats)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return render_template('index.html', resumes=[], stats={'total': 0, 'by_status': {}})


# -- Resume Builder ------------------------------------------------------------

@app.route('/resume/new', methods=['GET', 'POST'])
def resume_builder():
    if request.method == 'POST':
        # Collect education (dynamic rows)
        edu_list = []
        edu_degrees = request.form.getlist('edu_degree')
        edu_institutions = request.form.getlist('edu_institution')
        edu_years = request.form.getlist('edu_year')
        edu_grades = request.form.getlist('edu_grade')
        for i in range(len(edu_degrees)):
            if edu_degrees[i].strip():
                edu_list.append({
                    'degree': edu_degrees[i],
                    'institution': edu_institutions[i] if i < len(edu_institutions) else '',
                    'year': edu_years[i] if i < len(edu_years) else '',
                    'grade': edu_grades[i] if i < len(edu_grades) else '',
                })

        # Collect experience
        exp_list = []
        exp_roles = request.form.getlist('exp_role')
        exp_companies = request.form.getlist('exp_company')
        exp_durations = request.form.getlist('exp_duration')
        exp_descs = request.form.getlist('exp_description')
        for i in range(len(exp_roles)):
            if exp_roles[i].strip():
                exp_list.append({
                    'role': exp_roles[i],
                    'company': exp_companies[i] if i < len(exp_companies) else '',
                    'duration': exp_durations[i] if i < len(exp_durations) else '',
                    'description': exp_descs[i] if i < len(exp_descs) else '',
                })

        # Collect projects
        proj_list = []
        proj_titles = request.form.getlist('proj_title')
        proj_techs = request.form.getlist('proj_tech')
        proj_descs = request.form.getlist('proj_description')
        for i in range(len(proj_titles)):
            if proj_titles[i].strip():
                proj_list.append({
                    'title': proj_titles[i],
                    'tech': proj_techs[i] if i < len(proj_techs) else '',
                    'description': proj_descs[i] if i < len(proj_descs) else '',
                })

        resume_data = {
            'full_name': request.form.get('full_name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'location': request.form.get('location', ''),
            'linkedin': request.form.get('linkedin', ''),
            'portfolio': request.form.get('portfolio', ''),
            'summary': request.form.get('summary', ''),
            'skills': request.form.get('skills', ''),
            'education': json.dumps(edu_list),
            'experience': json.dumps(exp_list),
            'projects': json.dumps(proj_list),
            'certifications': request.form.get('certifications', ''),
        }

        resume_id = db.save_resume(resume_data)
        flash('Resume saved successfully!', 'success')
        return redirect(url_for('view_resume', resume_id=resume_id))

    return render_template('resume_builder.html', resume=None, edit=False)


@app.route('/resume/<int:resume_id>')
def view_resume(resume_id):
    resume = db.get_resume(resume_id)
    if not resume:
        flash('Resume not found.', 'error')
        return redirect(url_for('dashboard'))
    # Parse JSON fields
    for field in ('education', 'experience', 'projects'):
        try:
            resume[field] = json.loads(resume[field]) if resume[field] else []
        except Exception:
            resume[field] = []
    return render_template('view_resume.html', resume=resume)


@app.route('/resume/<int:resume_id>/edit', methods=['GET', 'POST'])
def edit_resume(resume_id):
    resume = db.get_resume(resume_id)
    if not resume:
        flash('Resume not found.', 'error')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        edu_list = []
        edu_degrees = request.form.getlist('edu_degree')
        edu_institutions = request.form.getlist('edu_institution')
        edu_years = request.form.getlist('edu_year')
        edu_grades = request.form.getlist('edu_grade')
        for i in range(len(edu_degrees)):
            if edu_degrees[i].strip():
                edu_list.append({
                    'degree': edu_degrees[i],
                    'institution': edu_institutions[i] if i < len(edu_institutions) else '',
                    'year': edu_years[i] if i < len(edu_years) else '',
                    'grade': edu_grades[i] if i < len(edu_grades) else '',
                })

        exp_list = []
        exp_roles = request.form.getlist('exp_role')
        exp_companies = request.form.getlist('exp_company')
        exp_durations = request.form.getlist('exp_duration')
        exp_descs = request.form.getlist('exp_description')
        for i in range(len(exp_roles)):
            if exp_roles[i].strip():
                exp_list.append({
                    'role': exp_roles[i],
                    'company': exp_companies[i] if i < len(exp_companies) else '',
                    'duration': exp_durations[i] if i < len(exp_durations) else '',
                    'description': exp_descs[i] if i < len(exp_descs) else '',
                })

        proj_list = []
        proj_titles = request.form.getlist('proj_title')
        proj_techs = request.form.getlist('proj_tech')
        proj_descs = request.form.getlist('proj_description')
        for i in range(len(proj_titles)):
            if proj_titles[i].strip():
                proj_list.append({
                    'title': proj_titles[i],
                    'tech': proj_techs[i] if i < len(proj_techs) else '',
                    'description': proj_descs[i] if i < len(proj_descs) else '',
                })

        updated_data = {
            'full_name': request.form.get('full_name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'location': request.form.get('location', ''),
            'linkedin': request.form.get('linkedin', ''),
            'portfolio': request.form.get('portfolio', ''),
            'summary': request.form.get('summary', ''),
            'skills': request.form.get('skills', ''),
            'education': json.dumps(edu_list),
            'experience': json.dumps(exp_list),
            'projects': json.dumps(proj_list),
            'certifications': request.form.get('certifications', ''),
        }
        db.update_resume(resume_id, updated_data)
        flash('Resume updated successfully!', 'success')
        return redirect(url_for('view_resume', resume_id=resume_id))

    # Parse JSON for form pre-fill
    for field in ('education', 'experience', 'projects'):
        try:
            resume[field] = json.loads(resume[field]) if resume[field] else []
        except Exception:
            resume[field] = []

    return render_template('resume_builder.html', resume=resume, edit=True)


@app.route('/resume/<int:resume_id>/delete', methods=['POST'])
def delete_resume(resume_id):
    db.delete_resume(resume_id)
    flash('Resume deleted.', 'info')
    return redirect(url_for('dashboard'))


# -- Resume Upload -------------------------------------------------------------

@app.route('/upload', methods=['GET', 'POST'])
def upload_resume():
    extracted_text = None
    if request.method == 'POST':
        f = request.files.get('resume_file')
        if f and f.filename:
            text = extract_text_from_file(f)
            if text:
                extracted_text = text
            else:
                flash('Could not extract text from the file. Please paste the text manually.', 'warning')
    return render_template('upload.html', extracted_text=extracted_text)


# -- ATS Analyzer -------------------------------------------------------------

@app.route('/ats', methods=['GET', 'POST'])
def ats_analyzer():
    result = None
    resume_list = db.get_all_resumes()

    if request.method == 'POST':
        resume_id = request.form.get('resume_id')
        resume_text = request.form.get('resume_text', '')
        jd_text = request.form.get('job_description', '')

        # If user selected a saved resume, load its text
        if resume_id and resume_id != '':
            saved = db.get_resume(int(resume_id))
            if saved:
                parts = [
                    saved.get('summary', ''), saved.get('skills', ''),
                    saved.get('certifications', ''),
                ]
                # Flatten experience / projects
                for field in ('experience', 'projects'):
                    try:
                        items = json.loads(saved[field]) if saved[field] else []
                        for item in items:
                            parts.append(' '.join(str(v) for v in item.values()))
                    except Exception:
                        pass
                resume_text = ' '.join(filter(None, parts))

        result = ats.calculate_ats_score(resume_text, jd_text)
        result['gap_analysis'] = ats.analyze_skill_gaps(result['missing'])

    return render_template('ats_analyzer.html', result=result, resume_list=resume_list)


# -- Resume Templates & PDF Download ------------------------------------------

@app.route('/templates')
def templates_page():
    resume_list = db.get_all_resumes()
    template_list = rg.get_template_list()
    return render_template('templates_page.html',
                           template_list=template_list,
                           resume_list=resume_list)


@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    resume_id = request.form.get('resume_id')
    template_name = request.form.get('template_name', 'modern')

    if not resume_id:
        flash('Please select a resume first.', 'error')
        return redirect(url_for('templates_page'))

    resume = db.get_resume(int(resume_id))
    if not resume:
        flash('Resume not found.', 'error')
        return redirect(url_for('templates_page'))

    pdf_bytes, error = rg.generate_resume_pdf(resume, template_name)
    if error:
        flash(f'PDF generation error: {error}', 'error')
        return redirect(url_for('templates_page'))

    safe_name = (resume.get('full_name') or 'Resume').replace(' ', '_')
    filename = f'{safe_name}_{template_name}_resume.pdf'

    return send_file(
        BytesIO(pdf_bytes),
        download_name=filename,
        mimetype='application/pdf',
        as_attachment=True
    )


# -- PDF Resume Rebuilder (Style Cloner) --------------------------------------

@app.route('/resume/rebuilder', methods=['GET', 'POST'])
def pdf_rebuilder():
    """Extract sections and match style of an uploaded or existing resume."""
    parsed_data = None
    resume_list = db.get_all_resumes()
    uploaded_text = ''

    if request.method == 'POST':
        file = request.files.get('resume_file')
        if file and file.filename:
            uploaded_text = extract_text_from_file(file)
        if not uploaded_text:
            uploaded_text = request.form.get('resume_text', '').strip()

        if not uploaded_text:
            flash('Please select a PDF/DOCX file or paste resume text.', 'warning')
            return redirect(url_for('pdf_rebuilder'))

        parsed_data = ats.parse_resume_data(uploaded_text)
        flash(f"Resume parsed! Matched style: {parsed_data.get('detected_style', 'modern').upper()}", 'success')

    elif request.method == 'GET':
        resume_id = request.args.get('resume_id')
        if resume_id:
            try:
                saved = db.get_resume(int(resume_id))
                if saved:
                    exp_items = []
                    if saved.get('experience'):
                        try:
                            exp_items = json.loads(saved['experience'])
                        except Exception:
                            exp_items = [{'role': '', 'company': saved['experience'], 'duration': '', 'description': ''}]

                    edu_items = []
                    if saved.get('education'):
                        try:
                            edu_items = json.loads(saved['education'])
                        except Exception:
                            edu_items = [{'degree': saved['education'], 'institution': '', 'year': '', 'grade': ''}]

                    proj_items = []
                    if saved.get('projects'):
                        try:
                            proj_items = json.loads(saved['projects'])
                        except Exception:
                            proj_items = [{'title': saved['projects'], 'tech': '', 'description': ''}]

                    parsed_data = {
                        'full_name': saved.get('full_name', ''),
                        'email': saved.get('email', ''),
                        'phone': saved.get('phone', ''),
                        'location': saved.get('location', ''),
                        'linkedin': saved.get('linkedin', ''),
                        'portfolio': saved.get('portfolio', ''),
                        'summary': saved.get('summary', ''),
                        'skills': saved.get('skills', ''),
                        'experience': exp_items,
                        'education': edu_items,
                        'projects': proj_items,
                        'certifications': saved.get('certifications', ''),
                        'detected_style': 'modern',
                        'sections_found': ['contact', 'summary', 'skills', 'experience', 'education', 'projects', 'certifications']
                    }
            except Exception as e:
                flash(f"Could not load selected resume: {e}", 'warning')

    return render_template(
        'pdf_rebuilder.html',
        parsed=parsed_data,
        resume_list=resume_list,
        uploaded_text=uploaded_text
    )


@app.route('/resume/rebuilder/export', methods=['POST'])
def export_rebuilt_pdf():
    """Generate and download rebuilt PDF with cloned styling."""
    try:
        full_name = request.form.get('full_name', '').strip() or 'Resume'
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        location = request.form.get('location', '').strip()
        linkedin = request.form.get('linkedin', '').strip()
        portfolio = request.form.get('portfolio', '').strip()
        summary = request.form.get('summary', '').strip()
        skills = request.form.get('skills', '').strip()
        template_name = request.form.get('template_name', 'cloned_style').strip()
        certifications = request.form.get('certifications', '').strip()

        # Reconstruct experience list
        roles = request.form.getlist('exp_role')
        companies = request.form.getlist('exp_company')
        durations = request.form.getlist('exp_duration')
        descriptions = request.form.getlist('exp_description')
        exp_list = []
        for i in range(len(roles)):
            if roles[i].strip() or (i < len(companies) and companies[i].strip()):
                exp_list.append({
                    'role': roles[i].strip(),
                    'company': companies[i].strip() if i < len(companies) else '',
                    'duration': durations[i].strip() if i < len(durations) else '',
                    'description': descriptions[i].strip() if i < len(descriptions) else ''
                })

        # Reconstruct education list
        degrees = request.form.getlist('edu_degree')
        institutions = request.form.getlist('edu_institution')
        years = request.form.getlist('edu_year')
        grades = request.form.getlist('edu_grade')
        edu_list = []
        for i in range(len(degrees)):
            if degrees[i].strip() or (i < len(institutions) and institutions[i].strip()):
                edu_list.append({
                    'degree': degrees[i].strip(),
                    'institution': institutions[i].strip() if i < len(institutions) else '',
                    'year': years[i].strip() if i < len(years) else '',
                    'grade': grades[i].strip() if i < len(grades) else ''
                })

        # Reconstruct projects list
        proj_titles = request.form.getlist('proj_title')
        proj_techs = request.form.getlist('proj_tech')
        proj_descs = request.form.getlist('proj_description')
        proj_list = []
        for i in range(len(proj_titles)):
            if proj_titles[i].strip():
                proj_list.append({
                    'title': proj_titles[i].strip(),
                    'tech': proj_techs[i].strip() if i < len(proj_techs) else '',
                    'description': proj_descs[i].strip() if i < len(proj_descs) else ''
                })

        resume_dict = {
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'location': location,
            'linkedin': linkedin,
            'portfolio': portfolio,
            'summary': summary,
            'skills': skills,
            'experience': json.dumps(exp_list),
            'education': json.dumps(edu_list),
            'projects': json.dumps(proj_list),
            'certifications': certifications
        }

        # Optional save to DB
        if request.form.get('save_to_db') == '1':
            try:
                db.save_resume(resume_dict)
            except Exception as dbe:
                print(f"Error saving rebuilt resume: {dbe}")

        pdf_bytes, err = rg.generate_resume_pdf(resume_dict, template_name=template_name)
        if err or not pdf_bytes:
            flash(f"Error creating PDF: {err or 'Unknown error'}", 'error')
            return redirect(url_for('pdf_rebuilder'))

        safe_name = "".join([c if c.isalnum() or c in "._-" else "_" for c in full_name])
        return send_file(
            BytesIO(pdf_bytes),
            download_name=f"{safe_name}_ClonedStyle_Resume.pdf",
            mimetype='application/pdf',
            as_attachment=True
        )
    except Exception as ex:
        flash(f"Export error: {ex}", 'error')
        return redirect(url_for('pdf_rebuilder'))


# -- Interview Prep ------------------------------------------------------------

@app.route('/interview', methods=['GET', 'POST'])
def interview_prep():
    questions = None
    resume_list = db.get_all_resumes()

    if request.method == 'POST':
        jd_text = request.form.get('job_description', '')
        resume_id = request.form.get('resume_id', '')
        resume_text = ''

        if resume_id:
            saved = db.get_resume(int(resume_id))
            if saved:
                resume_text = ' '.join(filter(None, [
                    saved.get('summary', ''), saved.get('skills', '')
                ]))

        if jd_text:
            questions = ats.generate_interview_questions(jd_text, resume_text)
        else:
            flash('Please paste a job description to generate questions.', 'warning')

    return render_template('interview_prep.html', questions=questions, resume_list=resume_list)


# -- Job Tracker ---------------------------------------------------------------

@app.route('/tracker')
def tracker():
    apps = db.get_all_applications()
    stats = db.get_stats()
    return render_template('tracker.html', applications=apps, stats=stats)


@app.route('/tracker/add', methods=['POST'])
def add_application():
    data = {
        'company': request.form.get('company', ''),
        'role': request.form.get('role', ''),
        'date_applied': request.form.get('date_applied', ''),
        'status': request.form.get('status', 'Applied'),
        'location': request.form.get('location', ''),
        'salary': request.form.get('salary', ''),
        'job_url': request.form.get('job_url', ''),
        'notes': request.form.get('notes', ''),
    }
    db.add_application(data)
    flash('Application added successfully!', 'success')
    return redirect(url_for('tracker'))


@app.route('/tracker/<int:app_id>/update', methods=['POST'])
def update_application(app_id):
    data = {
        'company': request.form.get('company', ''),
        'role': request.form.get('role', ''),
        'date_applied': request.form.get('date_applied', ''),
        'status': request.form.get('status', 'Applied'),
        'location': request.form.get('location', ''),
        'salary': request.form.get('salary', ''),
        'job_url': request.form.get('job_url', ''),
        'notes': request.form.get('notes', ''),
    }
    db.update_application(app_id, data)
    flash('Application updated successfully!', 'success')
    return redirect(url_for('tracker'))


@app.route('/tracker/<int:app_id>/delete', methods=['POST'])
def delete_application(app_id):
    db.delete_application(app_id)
    flash('Application deleted.', 'info')
    return redirect(url_for('tracker'))


# -- API endpoints -------------------------------------------------------------

@app.route('/api/resume/<int:resume_id>')
def api_resume(resume_id):
    resume = db.get_resume(resume_id)
    if not resume:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(resume)


@app.route('/api/stats')
def api_stats():
    return jsonify(db.get_stats())


# --- Run ----------------------------------------------------------------------

if __name__ == '__main__':
    import socket
    # Get local IP so user knows the mobile URL
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "YOUR_LAPTOP_IP"

    print("\n" + "="*55)
    print("  ATS Resume Builder is running!")
    print("="*55)
    print(f"  On this laptop  - http://127.0.0.1:5000")
    print(f"  On your MOBILE  - http://{local_ip}:5000")
    print("  (Both devices must be on the SAME Wi-Fi)")
    print("="*55 + "\n")

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
