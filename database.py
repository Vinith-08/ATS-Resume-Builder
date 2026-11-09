import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'ats_resume.db')

def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db()
    c = conn.cursor()

    # Resumes table
    c.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            phone TEXT,
            location TEXT,
            linkedin TEXT,
            portfolio TEXT,
            summary TEXT,
            skills TEXT,
            education TEXT,
            experience TEXT,
            projects TEXT,
            certifications TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Job Applications table
    c.execute('''
        CREATE TABLE IF NOT EXISTS job_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT,
            status TEXT DEFAULT 'Applied',
            location TEXT,
            salary TEXT,
            job_url TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# ─── Resume CRUD ─────────────────────────────────────────────────────────────

def save_resume(data):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO resumes (full_name, email, phone, location, linkedin, portfolio,
            summary, skills, education, experience, projects, certifications)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('full_name'), data.get('email'), data.get('phone'),
        data.get('location'), data.get('linkedin'), data.get('portfolio'),
        data.get('summary'), data.get('skills'), data.get('education'),
        data.get('experience'), data.get('projects'), data.get('certifications')
    ))
    resume_id = c.lastrowid
    conn.commit()
    conn.close()
    return resume_id

def get_resume(resume_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM resumes WHERE id = ?', (resume_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def get_all_resumes():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, full_name, email, created_at FROM resumes ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def update_resume(resume_id, data):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        UPDATE resumes SET full_name=?, email=?, phone=?, location=?, linkedin=?,
        portfolio=?, summary=?, skills=?, education=?, experience=?, projects=?, certifications=?
        WHERE id=?
    ''', (
        data.get('full_name'), data.get('email'), data.get('phone'),
        data.get('location'), data.get('linkedin'), data.get('portfolio'),
        data.get('summary'), data.get('skills'), data.get('education'),
        data.get('experience'), data.get('projects'), data.get('certifications'),
        resume_id
    ))
    conn.commit()
    conn.close()

def delete_resume(resume_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM resumes WHERE id = ?', (resume_id,))
    conn.commit()
    conn.close()

# ─── Job Application CRUD ─────────────────────────────────────────────────────

def add_application(data):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO job_applications (company, role, date_applied, status, location, salary, job_url, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('company'), data.get('role'), data.get('date_applied'),
        data.get('status', 'Applied'), data.get('location'), data.get('salary'),
        data.get('job_url'), data.get('notes')
    ))
    app_id = c.lastrowid
    conn.commit()
    conn.close()
    return app_id

def get_all_applications():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM job_applications ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_application(app_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM job_applications WHERE id = ?', (app_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def update_application(app_id, data):
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        UPDATE job_applications SET company=?, role=?, date_applied=?, status=?,
        location=?, salary=?, job_url=?, notes=? WHERE id=?
    ''', (
        data.get('company'), data.get('role'), data.get('date_applied'),
        data.get('status', 'Applied'), data.get('location'), data.get('salary'),
        data.get('job_url'), data.get('notes'), app_id
    ))
    conn.commit()
    conn.close()

def delete_application(app_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM job_applications WHERE id = ?', (app_id,))
    conn.commit()
    conn.close()

def get_stats():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT status, COUNT(*) as count FROM job_applications GROUP BY status')
    rows = c.fetchall()
    conn.close()
    stats = {r['status']: r['count'] for r in rows}
    total = sum(stats.values())
    return {'total': total, 'by_status': stats}
