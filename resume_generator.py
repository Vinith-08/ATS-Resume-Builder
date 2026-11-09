"""
Resume PDF Generator — 3 templates using fpdf2.
Compatible with Python 3.12+
"""

import json
from io import BytesIO

try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False


TEMPLATES = {
    'modern': {
        'name': 'Modern',
        'description': 'Clean layout with royal purple accent header. High ATS ranking.',
        'primary': (124, 58, 237),    # Royal Violet #7c3aed
        'heading': (88, 28, 135),     # Deep Plum #581c87
        'light': (245, 237, 255),
    },
    'classic': {
        'name': 'Classic',
        'description': 'Traditional format with dark plum accents, ideal for all industries.',
        'primary': (88, 28, 135),     # Deep Velvet Plum
        'heading': (60, 15, 95),      # Midnight Purple
        'light': (243, 232, 255),
    },
    'minimal': {
        'name': 'Minimal',
        'description': 'Ultra-clean minimalist design with sleek violet accents. ATS-friendly.',
        'primary': (147, 51, 234),    # Electric Amethyst #9333ea
        'heading': (107, 33, 168),    # Royal Purple
        'light': (248, 240, 255),
    },
}


def safe(text):
    """
    Remove / replace characters not supported by Helvetica (latin-1).
    Replaces bullet variants and other unicode chars with ASCII equivalents.
    """
    if not text:
        return ''
    replacements = {
        '\u2022': '-',   # •  bullet
        '\u2023': '-',   # ‣  triangular bullet
        '\u25cf': '-',   # ●  black circle
        '\u25e6': '-',   # ◦  white bullet
        '\u2013': '-',   # –  en dash
        '\u2014': '-',   # —  em dash  (keep plain -)
        '\u2018': "'",   # '  left single quote
        '\u2019': "'",   # '  right single quote
        '\u201c': '"',   # "  left double quote
        '\u201d': '"',   # "  right double quote
        '\u2026': '...', # …  ellipsis
        '\u00b7': '-',   # ·  middle dot
        '\u2012': '-',   # ‒  figure dash
        '\u2015': '-',   # ― horizontal bar
    }
    for ch, rep in replacements.items():
        text = text.replace(ch, rep)
    # Final fallback: drop any remaining non-latin-1 chars
    return text.encode('latin-1', errors='ignore').decode('latin-1')


BULLET = '>>'   # ASCII-safe bullet used in PDF


def get_template_list():
    return [
        {'id': k, 'name': v['name'], 'description': v['description']}
        for k, v in TEMPLATES.items()
    ]


def generate_resume_pdf(resume_data, template_name='modern'):
    """Generate a PDF resume and return (bytes, error_string)."""
    if not FPDF_AVAILABLE:
        return None, 'fpdf2 is not installed. Run: pip install fpdf2'

    tpl = TEMPLATES.get(template_name, TEMPLATES['modern'])
    pdf = ResumePDF(tpl)
    pdf.add_page()

    # ── Header ────────────────────────────────────────────────────────
    name      = safe(resume_data.get('full_name', 'Your Name'))
    email     = safe(resume_data.get('email', ''))
    phone     = safe(resume_data.get('phone', ''))
    location  = safe(resume_data.get('location', ''))
    linkedin  = safe(resume_data.get('linkedin', ''))
    portfolio = safe(resume_data.get('portfolio', ''))

    pr, pg, pb = tpl['primary']
    pdf.set_fill_color(pr, pg, pb)
    pdf.rect(0, 0, 210, 38, 'F')

    pdf.set_xy(10, 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 20)
    pdf.cell(0, 10, name, ln=True)

    contact_parts = [x for x in [email, phone, location, linkedin, portfolio] if x]
    pdf.set_font('Helvetica', '', 9)
    pdf.set_x(10)
    pdf.cell(0, 8, '  |  '.join(contact_parts), ln=True)

    pdf.set_xy(10, 42)
    pdf.set_text_color(30, 30, 30)

    # ── Summary ───────────────────────────────────────────────────────
    summary = safe(resume_data.get('summary', ''))
    if summary:
        pdf.section_heading('PROFESSIONAL SUMMARY', tpl)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 5, summary)
        pdf.ln(3)

    # ── Skills ────────────────────────────────────────────────────────
    skills_raw = safe(resume_data.get('skills', ''))
    if skills_raw:
        pdf.section_heading('SKILLS', tpl)
        skills_list = [s.strip() for s in skills_raw.replace('\n', ',').split(',') if s.strip()]
        # Join with ASCII separator that Helvetica can render
        skills_text = '  |  '.join(skills_list)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 5, skills_text)
        pdf.ln(3)

    # ── Experience ────────────────────────────────────────────────────
    exp_raw = resume_data.get('experience', '')
    if exp_raw:
        pdf.section_heading('WORK EXPERIENCE', tpl)
        try:
            exp_list = json.loads(exp_raw)
        except Exception:
            exp_list = [{'role': '', 'company': exp_raw, 'duration': '', 'description': ''}]

        for exp in exp_list:
            role     = safe(exp.get('role', ''))
            company  = safe(exp.get('company', ''))
            duration = safe(exp.get('duration', ''))
            desc     = safe(exp.get('description', ''))

            pr2, pg2, pb2 = tpl['heading']
            pdf.set_text_color(pr2, pg2, pb2)
            pdf.set_font('Helvetica', 'B', 11)
            pdf.cell(130, 6, f"{role}  -  {company}", ln=False)
            pdf.set_font('Helvetica', 'I', 9)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(0, 6, duration, ln=True, align='R')

            if desc:
                pdf.set_font('Helvetica', '', 10)
                pdf.set_text_color(50, 50, 50)
                for line in desc.split('\n'):
                    line = line.strip().lstrip('->*').strip()
                    if line:
                        pdf.set_x(14)
                        pdf.multi_cell(0, 5, f'{BULLET} {line}')
            pdf.ln(2)

    # ── Education ─────────────────────────────────────────────────────
    edu_raw = resume_data.get('education', '')
    if edu_raw:
        pdf.section_heading('EDUCATION', tpl)
        try:
            edu_list = json.loads(edu_raw)
        except Exception:
            edu_list = [{'degree': edu_raw, 'institution': '', 'year': '', 'grade': ''}]

        for edu in edu_list:
            degree      = safe(edu.get('degree', ''))
            institution = safe(edu.get('institution', ''))
            year        = safe(edu.get('year', ''))
            grade       = safe(edu.get('grade', ''))

            pr2, pg2, pb2 = tpl['heading']
            pdf.set_text_color(pr2, pg2, pb2)
            pdf.set_font('Helvetica', 'B', 10)
            pdf.cell(130, 6, f"{degree}  -  {institution}", ln=False)
            pdf.set_font('Helvetica', 'I', 9)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(0, 6, year, ln=True, align='R')

            if grade:
                pdf.set_font('Helvetica', '', 9)
                pdf.set_text_color(80, 80, 80)
                pdf.set_x(14)
                pdf.cell(0, 5, f'Grade / CGPA: {grade}', ln=True)
            pdf.ln(2)

    # ── Projects ──────────────────────────────────────────────────────
    proj_raw = resume_data.get('projects', '')
    if proj_raw:
        pdf.section_heading('PROJECTS', tpl)
        try:
            proj_list = json.loads(proj_raw)
        except Exception:
            proj_list = [{'title': proj_raw, 'tech': '', 'description': ''}]

        for proj in proj_list:
            title = safe(proj.get('title', ''))
            tech  = safe(proj.get('tech', ''))
            desc  = safe(proj.get('description', ''))

            pr2, pg2, pb2 = tpl['heading']
            pdf.set_text_color(pr2, pg2, pb2)
            pdf.set_font('Helvetica', 'B', 10)
            label = f"{title}  ({tech})" if tech else title
            pdf.cell(0, 6, label, ln=True)

            if desc:
                pdf.set_font('Helvetica', '', 10)
                pdf.set_text_color(50, 50, 50)
                for line in desc.split('\n'):
                    line = line.strip().lstrip('->*').strip()
                    if line:
                        pdf.set_x(14)
                        pdf.multi_cell(0, 5, f'{BULLET} {line}')
            pdf.ln(2)

    # ── Certifications ────────────────────────────────────────────────
    cert_raw = resume_data.get('certifications', '')
    if cert_raw:
        pdf.section_heading('CERTIFICATIONS', tpl)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(50, 50, 50)
        for cert in cert_raw.split('\n'):
            cert = safe(cert.strip().lstrip('->*').strip())
            if cert:
                pdf.set_x(14)
                pdf.cell(0, 5, f'{BULLET} {cert}', ln=True)

    # ── Return bytes ──────────────────────────────────────────────────
    buf = BytesIO()
    buf.write(pdf.output())
    return buf.getvalue(), None


class ResumePDF(FPDF):
    """Custom FPDF subclass with helper methods."""

    def __init__(self, tpl):
        super().__init__()
        self.tpl = tpl
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(10, 10, 10)

    def section_heading(self, title, tpl):
        pr, pg, pb = tpl['primary']
        self.set_draw_color(pr, pg, pb)
        self.set_text_color(pr, pg, pb)
        self.set_font('Helvetica', 'B', 11)
        self.set_x(10)
        self.cell(0, 7, title, ln=True, border='B')
        self.ln(1)
