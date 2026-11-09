# -*- coding: utf-8 -*-
"""
Embedded Frontend Assets Bundle
Automatically self-extracts templates and static files on boot.
100% Clean ASCII with SVG vector graphics - Zero Mojibake Guarantee.
"""
import os

ASSETS = {
    'templates/base.html': r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <meta name="theme-color" content="#08001a">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="description" content="AI-Powered ATS Resume Builder - Create ATS-optimized resumes, analyze job matches, and prepare for interviews.">
    <title>{% block title %}ATS Resume Builder{% endblock %} - AI-Powered</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block head %}{% endblock %}
</head>
<body>
    <!-- Sidebar Navigation -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-brand">
            <div class="brand-icon">
                <svg width="30" height="30" viewBox="0 0 28 28" fill="none">
                    <rect width="28" height="28" rx="8" fill="url(#gradPurpleBrand)"/>
                    <path d="M7 8h14M7 12h10M7 16h12M7 20h8" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
                    <circle cx="21" cy="19" r="4.5" fill="#ffffff" opacity="0.95"/>
                    <path d="M19.2 19l1.2 1.2 2.4-2.4" stroke="#7c3aed" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                    <defs>
                        <linearGradient id="gradPurpleBrand" x1="0" y1="0" x2="28" y2="28" gradientUnits="userSpaceOnUse">
                            <stop stop-color="#9333ea"/>
                            <stop offset="0.5" stop-color="#a855f7"/>
                            <stop offset="1" stop-color="#c084fc"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>
            <div class="brand-text">
                <span class="brand-name">ATS Builder</span>
                <span class="brand-sub">AI-Powered</span>
            </div>
            <button class="sidebar-close-btn" onclick="toggleSidebar()" aria-label="Close menu">&times;</button>
        </div>

        <nav class="sidebar-nav">
            <div class="nav-section-label">Main</div>
            <a href="{{ url_for('dashboard') }}" class="nav-item {% if request.endpoint == 'dashboard' %}active{% endif %}" id="nav-dashboard">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/>
                        <rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>
                    </svg>
                </span>
                <span class="nav-label">Dashboard</span>
            </a>
            <a href="{{ url_for('resume_builder') }}" class="nav-item {% if request.endpoint in ['resume_builder', 'view_resume', 'edit_resume'] %}active{% endif %}" id="nav-resume">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>
                    </svg>
                </span>
                <span class="nav-label">Resume Builder</span>
                <span class="nav-badge">New</span>
            </a>

            <div class="nav-section-label">Tools</div>
            <a href="{{ url_for('pdf_rebuilder') }}" class="nav-item {% if request.endpoint == 'pdf_rebuilder' %}active{% endif %}" id="nav-rebuilder">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <path d="M12 18v-6M9 15l3-3 3 3"/>
                    </svg>
                </span>
                <span class="nav-label">PDF Rebuilder</span>
                <span class="nav-badge" style="background: rgba(147, 51, 234, 0.4); color: #e9d5ff; border: 1px solid rgba(192, 132, 252, 0.4);">New</span>
            </a>
            <a href="{{ url_for('ats_analyzer') }}" class="nav-item {% if request.endpoint == 'ats_analyzer' %}active{% endif %}" id="nav-ats">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12 6 12 12 16 14"/>
                    </svg>
                </span>
                <span class="nav-label">ATS Analyzer</span>
            </a>
            <a href="{{ url_for('templates_page') }}" class="nav-item {% if request.endpoint == 'templates_page' %}active{% endif %}" id="nav-templates">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
                    </svg>
                </span>
                <span class="nav-label">Resume Templates</span>
            </a>
            <a href="{{ url_for('interview_prep') }}" class="nav-item {% if request.endpoint == 'interview_prep' %}active{% endif %}" id="nav-interview">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                    </svg>
                </span>
                <span class="nav-label">Interview Prep</span>
            </a>
            <a href="{{ url_for('tracker') }}" class="nav-item {% if request.endpoint == 'tracker' %}active{% endif %}" id="nav-tracker">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                    </svg>
                </span>
                <span class="nav-label">Job Tracker</span>
            </a>
            <a href="{{ url_for('upload_resume') }}" class="nav-item {% if request.endpoint == 'upload_resume' %}active{% endif %}" id="nav-upload">
                <span class="nav-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>
                    </svg>
                </span>
                <span class="nav-label">Upload Resume</span>
            </a>
        </nav>

        <div class="sidebar-footer">
            <div class="sidebar-footer-card">
                <div class="footer-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                    </svg>
                </div>
                <div>
                    <div class="footer-title">MCA Mini Project</div>
                    <div class="footer-sub">AI-Powered ATS System</div>
                </div>
            </div>
        </div>
    </aside>

    <!-- Mobile Overlay -->
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>

    <!-- Main Content -->
    <div class="main-wrapper">
        <!-- Top Bar -->
        <header class="topbar">
            <button class="menu-btn" id="menuBtn" onclick="toggleSidebar()" aria-label="Toggle menu">
                <span></span><span></span><span></span>
            </button>
            <div class="topbar-title">{% block page_title %}Dashboard{% endblock %}</div>
            <div class="topbar-right">
                <div class="topbar-chip">
                    <span class="chip-dot"></span>
                    <span>Live</span>
                </div>
            </div>
        </header>

        <!-- Flash Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="flash-container" id="flashContainer">
            {% for category, message in messages %}
            <div class="flash flash-{{ category }}">
                <span>{{ message }}</span>
                <button onclick="this.parentElement.remove()" class="flash-close">&times;</button>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}

        <!-- Page Content -->
        <main class="page-content">
            {% block content %}{% endblock %}
        </main>
    </div>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
""",
    'templates/index.html': r"""
{% extends "base.html" %}
{% block title %}Dashboard{% endblock %}
{% block page_title %}Dashboard{% endblock %}

{% block content %}
<div class="dashboard-hero">
    <div class="hero-content">
        <div class="hero-badge">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>
            </svg>
            AI-Powered ATS
        </div>
        <h1 class="hero-title">Build Resumes That Beat the ATS</h1>
        <p class="hero-subtitle">Create tailored resumes, analyze your job match score, identify skill gaps, and prepare for interviews - all in one place.</p>
        <div class="hero-actions">
            <a href="{{ url_for('resume_builder') }}" class="btn btn-primary btn-lg">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                </svg>
                Build Resume
            </a>
            <a href="{{ url_for('pdf_rebuilder') }}" class="btn btn-secondary btn-lg" style="background: rgba(147, 51, 234, 0.35); border: 1px solid rgba(192, 132, 252, 0.45); color: #f3e8ff;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <path d="M12 18v-6M9 15l3-3 3 3"/>
                </svg>
                PDF Style Rebuilder
            </a>
            <a href="{{ url_for('ats_analyzer') }}" class="btn btn-outline btn-lg">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
                Analyze ATS Score
            </a>
        </div>
    </div>
    <div class="hero-illustration">
        <div class="hero-score-card">
            <div class="score-ring-demo">
                <svg width="120" height="120" viewBox="0 0 120 120">
                    <circle cx="60" cy="60" r="50" fill="none" stroke="rgba(168, 85, 247, 0.2)" stroke-width="10"/>
                    <circle cx="60" cy="60" r="50" fill="none" stroke="url(#scoreGradPurple)" stroke-width="10"
                        stroke-dasharray="251" stroke-dashoffset="63" stroke-linecap="round"
                        transform="rotate(-90 60 60)"/>
                    <defs>
                        <linearGradient id="scoreGradPurple" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#9333ea"/>
                            <stop offset="50%" stop-color="#c084fc"/>
                            <stop offset="100%" stop-color="#e9d5ff"/>
                        </linearGradient>
                    </defs>
                </svg>
                <div class="score-ring-label">75%</div>
            </div>
            <div class="score-card-label">ATS Match Score</div>
        </div>
    </div>
</div>

<!-- Stats Row -->
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-icon stat-icon-purple">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ resumes|length }}</div>
            <div class="stat-label">Resumes Created</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-blue">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.total }}</div>
            <div class="stat-label">Jobs Tracked</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-green">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.by_status.get('Interview', 0) }}</div>
            <div class="stat-label">Interviews</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-amber">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.by_status.get('Offer', 0) }}</div>
            <div class="stat-label">Offers Received</div>
        </div>
    </div>
</div>

<!-- Feature Cards -->
<div class="section-header">
    <h2 class="section-title">All Features</h2>
    <p class="section-sub">Everything you need to land your dream job</p>
</div>

<div class="feature-grid">
    <a href="{{ url_for('pdf_rebuilder') }}" class="feature-card feature-card-rebuilder" style="border: 1px solid rgba(192, 132, 252, 0.45); background: linear-gradient(135deg, rgba(46, 16, 101, 0.6) 0%, rgba(20, 3, 40, 0.8) 100%);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div class="feature-icon" style="background: rgba(147, 51, 234, 0.25); border: 1px solid rgba(192, 132, 252, 0.35);">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <path d="M12 18v-6M9 15l3-3 3 3"/>
                </svg>
            </div>
            <span class="badge" style="background: linear-gradient(135deg, #7c3aed, #c084fc); color: #fff; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.5px;">New AI Tool</span>
        </div>
        <h3 style="color: #f5f3ff;">PDF Resume Rebuilder</h3>
        <p>Upload any PDF/DOCX resume. AI detects sections and layout archetype to build a fresh, ATS-compliant PDF in the exact matching style!</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('resume_builder') }}" class="feature-card feature-card-1">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="16" y1="13" x2="8" y2="13"/>
                <line x1="16" y1="17" x2="8" y2="17"/>
                <polyline points="10 9 9 9 8 9"/>
            </svg>
        </div>
        <h3>Resume Builder</h3>
        <p>Create structured resumes with education, experience, skills, and projects. Save and manage multiple resumes.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('ats_analyzer') }}" class="feature-card feature-card-2">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <circle cx="12" cy="12" r="6"/>
                <circle cx="12" cy="12" r="2"/>
            </svg>
        </div>
        <h3>ATS Match Analyzer</h3>
        <p>Paste a job description and instantly see your match score, matched skills, and missing skills.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('ats_analyzer') }}" class="feature-card feature-card-3">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"/>
                <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                <line x1="11" y1="8" x2="11" y2="14"/>
                <line x1="8" y1="11" x2="14" y2="11"/>
            </svg>
        </div>
        <h3>Skill Gap Analyzer</h3>
        <p>Discover exactly which skills you are missing with curated learning resources for each gap.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('templates_page') }}" class="feature-card feature-card-4">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2"/>
                <path d="M3 9h18M9 21V9"/>
            </svg>
        </div>
        <h3>Resume Templates</h3>
        <p>Choose from Modern, Classic, or Minimal templates and download a professional PDF instantly.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('interview_prep') }}" class="feature-card feature-card-5">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
        </div>
        <h3>Interview Prep</h3>
        <p>Generate HR, technical, and situational interview questions based on the job description.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
    <a href="{{ url_for('tracker') }}" class="feature-card feature-card-6">
        <div class="feature-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 11l3 3L22 4"/>
                <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
            </svg>
        </div>
        <h3>Job Tracker</h3>
        <p>Track every application - company, role, status, dates, and notes in one organized place.</p>
        <div class="feature-arrow">&rarr;</div>
    </a>
</div>

<!-- Recent Resumes -->
{% if resumes %}
<div class="section-header">
    <h2 class="section-title">Recent Resumes</h2>
    <a href="{{ url_for('resume_builder') }}" class="btn btn-sm btn-outline">+ New Resume</a>
</div>
<div class="resume-list">
    {% for r in resumes[:5] %}
    <div class="resume-list-item">
        <div class="resume-avatar">{{ r.full_name[0].upper() if r.full_name else '?' }}</div>
        <div class="resume-info">
            <div class="resume-name">{{ r.full_name or 'Unnamed Resume' }}</div>
            <div class="resume-email">{{ r.email or '' }}</div>
        </div>
        <div class="resume-date">{{ r.created_at[:10] if r.created_at else '' }}</div>
        <div class="resume-actions">
            <a href="{{ url_for('view_resume', resume_id=r.id) }}" class="btn btn-sm btn-ghost">View</a>
            <a href="{{ url_for('edit_resume', resume_id=r.id) }}" class="btn btn-sm btn-ghost">Edit</a>
        </div>
    </div>
    {% endfor %}
</div>
{% endif %}
{% endblock %}
""",
    'templates/pdf_rebuilder.html': r"""
{% extends "base.html" %}
{% block title %}PDF Resume Rebuilder{% endblock %}
{% block page_title %}PDF Resume Style Rebuilder{% endblock %}

{% block content %}
<!-- Tool Header -->
<div class="dashboard-hero" style="margin-bottom: 24px; padding: 32px 36px;">
    <div class="hero-content">
        <div class="hero-badge">AI Style Matcher &amp; PDF Cloner</div>
        <h1 class="hero-title" style="font-size: 30px;">Clone &amp; Rebuild Your Resume in PDF</h1>
        <p class="hero-subtitle" style="max-width: 620px; font-size: 14.5px;">
            Upload your existing PDF or DOCX resume. Our AI automatically extracts every section, analyzes the formatting layout, and generates a fresh, perfectly aligned ATS-friendly PDF in matching style!
        </p>
    </div>
    <div class="hero-illustration">
        <div class="stat-card" style="background: rgba(45, 12, 95, 0.75); border: 1px solid var(--border-glow); padding: 18px 24px;">
            <div class="stat-icon stat-icon-purple" style="width: 50px; height: 50px; font-size: 24px;">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <path d="M12 18v-6M9 15l3-3 3 3"/>
                </svg>
            </div>
            <div>
                <div class="stat-value" style="font-size: 22px;">100% Match</div>
                <div class="stat-label">Style Preservation</div>
            </div>
        </div>
    </div>
</div>

<!-- Step 1: Upload Existing Resume Card -->
<div class="form-card" style="margin-bottom: 24px;">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="17 8 12 3 7 8"/>
                <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Step 1: Upload or Choose Resume</h2>
            <p class="form-card-sub">Upload your PDF/Word resume to auto-parse its content and structure</p>
        </div>
    </div>

    <form method="POST" enctype="multipart/form-data" action="{{ url_for('pdf_rebuilder') }}">
        <div class="form-grid form-grid-2">
            <!-- File Upload -->
            <div>
                <div class="upload-dropzone" onclick="document.getElementById('rebuilder_file').click()" style="padding: 30px 20px;">
                    <div class="dropzone-icon">
                        <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                            <line x1="12" y1="18" x2="12" y2="12"/>
                            <polyline points="9 15 12 12 15 15"/>
                        </svg>
                    </div>
                    <div class="dropzone-text" style="font-size: 14px;">Select PDF or DOCX Resume</div>
                    <div class="dropzone-sub">Click here to browse your device files</div>
                    <input type="file" id="rebuilder_file" name="resume_file" accept=".pdf,.docx" style="display:none" onchange="document.getElementById('fileNameDisplay').textContent = this.files[0] ? this.files[0].name : ''; document.getElementById('fileNameDisplay').style.display = 'block';">
                    <div class="dropzone-filename" id="fileNameDisplay"></div>
                </div>
            </div>

            <!-- Alternative: Paste Text or Pick Saved -->
            <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 12px;">
                <div class="form-group">
                    <label for="existing_resume">Or Pick from Saved Resumes</label>
                    <select id="existing_resume" class="form-select" onchange="if(this.value) window.location.href='{{ url_for('pdf_rebuilder') }}?resume_id=' + this.value">
                        <option value="">-- Choose saved resume --</option>
                        {% for r in resume_list %}
                        <option value="{{ r.id }}">{{ r.full_name }} ({{ r.created_at[:10] }})</option>
                        {% endfor %}
                    </select>
                </div>

                <div class="form-group" style="flex: 1;">
                    <label for="resume_text">Or Paste Resume Content</label>
                    <textarea id="resume_text" name="resume_text" class="form-textarea" rows="3" placeholder="Paste your resume text here if you don't have the PDF file handy..."></textarea>
                </div>
            </div>
        </div>

        <div style="margin-top: 18px; display: flex; justify-content: flex-end;">
            <button type="submit" class="btn btn-primary btn-lg" style="width: auto;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                </svg>
                Auto-Parse &amp; Match Style
            </button>
        </div>

        <!-- JD Optimization Textarea -->
        <div class="form-card" style="margin-top: 20px; border: 1.5px solid rgba(147,51,234,0.5); background: rgba(30,10,70,0.6);">
            <div class="form-card-header">
                <div class="form-card-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                    </svg>
                </div>
                <div>
                    <h3 class="form-card-title">Job Description Optimization <span style="background: linear-gradient(90deg,#7c3aed,#a855f7); color:#fff; font-size:11px; padding:2px 10px; border-radius:20px; font-weight:600; vertical-align: middle;">AI Feature</span></h3>
                    <p class="form-card-sub">Paste the job description - AI tailors your resume keywords and summary to match the role</p>
                </div>
            </div>
            <div class="form-group" style="margin-top: 0;">
                <textarea name="job_description" class="form-textarea" rows="5"
                    placeholder="Paste the full job description here (optional). AI will: 1) Reorder skills to put JD-matching ones first. 2) Enhance summary with JD keywords. 3) Show ATS match score report."
                    style="font-size: 13.5px; line-height: 1.6;"></textarea>
                <p style="margin-top: 6px; font-size: 12px; color: var(--purple-pale); opacity: 0.75;">
                    Tip: The more of the actual JD you paste, the more accurately the AI can optimize your resume.
                </p>
            </div>
        </div>
    </form>
</div>

<!-- Step 2: Interactive Editor & Cloned PDF Generator -->
{% if parsed %}
<div class="section-header">
    <div>
        <h2 class="section-title">Step 2: Refine &amp; Generate Cloned PDF</h2>
        <p class="section-sub">
            Detected Style Archetype: <strong style="color: var(--purple-neon); text-transform: uppercase;">{{ parsed.detected_style }}</strong>
            &nbsp;|&nbsp; Found Sections: <strong>{{ parsed.sections_found|join(', ')|title }}</strong>
        </p>
    </div>
</div>

<form method="POST" action="{{ url_for('export_rebuilt_pdf') }}" id="cloneExportForm">
    <!-- Style Template Selector -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="2"/>
                    <path d="M3 9h18M9 21V9"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Choose Output Visual Style</h3>
                <p class="form-card-sub">Select the styling for your generated PDF</p>
            </div>
        </div>

        <div class="template-cards" style="grid-template-columns: repeat(4, 1fr);">
            <!-- Cloned Match -->
            <div class="template-card {% if parsed.detected_style not in ['classic', 'minimal', 'executive'] %}active{% endif %}" onclick="selectRebuilderTemplate('cloned_style', this)">
                <div class="template-preview modern-preview" style="height: 110px;">
                    <div class="tpl-header-bar"></div>
                    <div class="tpl-name-block"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                </div>
                <div class="template-card-info" style="padding: 10px 12px;">
                    <div class="template-name" style="font-size: 13px;">Exact Cloned Match</div>
                    <span class="template-badge tpl-badge-modern">Recommended</span>
                </div>
            </div>

            <!-- Modern Purple -->
            <div class="template-card {% if parsed.detected_style == 'modern' %}active{% endif %}" onclick="selectRebuilderTemplate('modern', this)">
                <div class="template-preview modern-preview" style="height: 110px;">
                    <div class="tpl-header-bar" style="background: linear-gradient(90deg, #9333ea, #c084fc);"></div>
                    <div class="tpl-name-block"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                </div>
                <div class="template-card-info" style="padding: 10px 12px;">
                    <div class="template-name" style="font-size: 13px;">Modern Purple</div>
                    <span class="template-badge tpl-badge-modern">Tech Roles</span>
                </div>
            </div>

            <!-- Executive Cloned -->
            <div class="template-card {% if parsed.detected_style == 'executive' %}active{% endif %}" onclick="selectRebuilderTemplate('executive', this)">
                <div class="template-preview classic-preview" style="height: 110px;">
                    <div class="tpl-classic-header"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-classic-rule"></div>
                </div>
                <div class="template-card-info" style="padding: 10px 12px;">
                    <div class="template-name" style="font-size: 13px;">Executive Plum</div>
                    <span class="template-badge tpl-badge-classic">Leadership</span>
                </div>
            </div>

            <!-- Minimal ATS -->
            <div class="template-card {% if parsed.detected_style == 'minimal' %}active{% endif %}" onclick="selectRebuilderTemplate('minimal', this)">
                <div class="template-preview minimal-preview" style="height: 110px;">
                    <div class="tpl-min-name"></div>
                    <div class="tpl-min-section"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                </div>
                <div class="template-card-info" style="padding: 10px 12px;">
                    <div class="template-name" style="font-size: 13px;">Minimal ATS</div>
                    <span class="template-badge tpl-badge-minimal">Clean ATS</span>
                </div>
            </div>
        </div>
        <input type="hidden" name="template_name" id="selectedTemplateInput" value="{{ parsed.detected_style if parsed.detected_style in ['modern', 'classic', 'minimal', 'executive'] else 'cloned_style' }}">
    </div>

    <!-- AI Optimization Report (shown if JD was provided) -->
    {% if opt_report %}
    <div class="form-card" style="border: 1.5px solid rgba(124,58,237,0.6); background: rgba(20,5,55,0.7); margin-bottom: 20px;">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#a855f7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">AI Optimization Report</h3>
                <p class="form-card-sub">Your resume was automatically tailored to the job description</p>
            </div>
        </div>

        <!-- ATS Score Before / After -->
        <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 18px;">
            <div style="flex: 1; min-width: 180px;">
                <div style="font-size: 12px; color: var(--purple-pale); margin-bottom: 6px; font-weight: 600; text-transform: uppercase; letter-spacing: .05em;">ATS Score Before</div>
                <div style="background: rgba(255,255,255,0.07); border-radius: 8px; overflow: hidden; height: 10px; margin-bottom: 4px;">
                    <div style="width: {{ opt_report.score_before }}%; height: 10px; background: rgba(192,132,252,0.4); border-radius: 8px; transition: width 0.6s;"></div>
                </div>
                <div style="font-size: 20px; font-weight: 700; color: #c084fc;">{{ opt_report.score_before }}%</div>
            </div>
            <div style="display: flex; align-items: center; padding-top: 10px; color: #a855f7; font-size: 24px; font-weight: 700;">-&gt;</div>
            <div style="flex: 1; min-width: 180px;">
                <div style="font-size: 12px; color: var(--purple-pale); margin-bottom: 6px; font-weight: 600; text-transform: uppercase; letter-spacing: .05em;">ATS Score After</div>
                <div style="background: rgba(255,255,255,0.07); border-radius: 8px; overflow: hidden; height: 10px; margin-bottom: 4px;">
                    <div style="width: {{ opt_report.score_after }}%; height: 10px; background: linear-gradient(90deg,#7c3aed,#a855f7); border-radius: 8px; transition: width 0.6s;"></div>
                </div>
                <div style="font-size: 20px; font-weight: 700; color: #a855f7;">{{ opt_report.score_after }}%</div>
            </div>
        </div>

        {% if opt_report.matched_skills %}
        <div style="margin-bottom: 14px;">
            <div style="font-size: 12px; font-weight: 600; color: #86efac; margin-bottom: 8px; text-transform: uppercase; letter-spacing: .05em;">Matched Skills (Already In Resume)</div>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {% for sk in opt_report.matched_skills %}
                <span style="background: rgba(34,197,94,0.15); border: 1px solid rgba(34,197,94,0.35); color: #86efac; border-radius: 20px; padding: 3px 11px; font-size: 12px; font-weight: 500;">{{ sk }}</span>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if opt_report.suggested_skills %}
        <div style="margin-bottom: 14px;">
            <div style="font-size: 12px; font-weight: 600; color: #c084fc; margin-bottom: 8px; text-transform: uppercase; letter-spacing: .05em;">Suggested Skills to Add</div>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {% for sk in opt_report.suggested_skills %}
                <span style="background: rgba(168,85,247,0.15); border: 1px solid rgba(168,85,247,0.4); color: #c084fc; border-radius: 20px; padding: 3px 11px; font-size: 12px; font-weight: 500;">+ {{ sk }}</span>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if opt_report.missing_skills %}
        <div style="margin-bottom: 14px;">
            <div style="font-size: 12px; font-weight: 600; color: #fca5a5; margin-bottom: 8px; text-transform: uppercase; letter-spacing: .05em;">Skills Gap (Missing from Resume)</div>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {% for sk in opt_report.missing_skills %}
                <span style="background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.3); color: #fca5a5; border-radius: 20px; padding: 3px 11px; font-size: 12px; font-weight: 500;">{{ sk }}</span>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if opt_report.summary_changed %}
        <div style="background: rgba(124,58,237,0.15); border: 1px solid rgba(124,58,237,0.4); border-radius: 10px; padding: 12px 16px; margin-top: 6px;">
            <div style="font-size: 12px; font-weight: 600; color: #c084fc; margin-bottom: 4px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2.5" style="vertical-align: middle; margin-right: 4px;"><polyline points="20 6 9 17 4 12"/></svg>
                AI Summary Optimization Applied
            </div>
            <div style="font-size: 12.5px; color: var(--purple-pale); line-height: 1.6;">Your Professional Summary was enhanced with JD-relevant keywords. Review and edit it in the form below before downloading.</div>
        </div>
        {% endif %}
    </div>
    {% endif %}

    <!-- Hidden: preserve JD for export -->
    <input type="hidden" name="job_description" value="{{ jd_text|e }}">

    <!-- Personal Information -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Personal Contact Info</h3>
                <p class="form-card-sub">Parsed from your uploaded resume</p>
            </div>
        </div>

        <div class="form-grid form-grid-3">
            <div class="form-group">
                <label>Full Name <span class="required">*</span></label>
                <input type="text" name="full_name" class="form-input" value="{{ parsed.full_name }}" required>
            </div>
            <div class="form-group">
                <label>Email Address <span class="required">*</span></label>
                <input type="email" name="email" class="form-input" value="{{ parsed.email }}" required>
            </div>
            <div class="form-group">
                <label>Phone Number</label>
                <input type="text" name="phone" class="form-input" value="{{ parsed.phone }}">
            </div>
            <div class="form-group">
                <label>Location</label>
                <input type="text" name="location" class="form-input" value="{{ parsed.location }}">
            </div>
            <div class="form-group">
                <label>LinkedIn URL</label>
                <input type="url" name="linkedin" class="form-input" value="{{ parsed.linkedin }}">
            </div>
            <div class="form-group">
                <label>GitHub / Portfolio URL</label>
                <input type="url" name="portfolio" class="form-input" value="{{ parsed.portfolio }}">
            </div>
        </div>

        <div class="form-group" style="margin-top: 14px;">
            <label>Professional Summary</label>
            <textarea name="summary" class="form-textarea" rows="3">{{ parsed.summary }}</textarea>
        </div>
    </div>

    <!-- Skills -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Skills &amp; Competencies</h3>
                <p class="form-card-sub">Comma-separated skills extracted from your resume</p>
            </div>
        </div>
        <div class="form-group">
            <textarea name="skills" class="form-textarea" rows="3">{{ parsed.skills }}</textarea>
        </div>
    </div>

    <!-- Experience -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Work Experience</h3>
                <p class="form-card-sub">Positions, company names, durations, and accomplishment bullets</p>
            </div>
        </div>

        <div id="experienceList">
            {% for exp in parsed.experience %}
            <div class="dynamic-row" data-row="experience">
                <div class="form-grid form-grid-3">
                    <div class="form-group">
                        <label>Job Title / Role</label>
                        <input type="text" name="exp_role" class="form-input" value="{{ exp.role }}">
                    </div>
                    <div class="form-group">
                        <label>Company</label>
                        <input type="text" name="exp_company" class="form-input" value="{{ exp.company }}">
                    </div>
                    <div class="form-group">
                        <label>Duration</label>
                        <input type="text" name="exp_duration" class="form-input" value="{{ exp.duration }}">
                    </div>
                </div>
                <div class="form-group" style="margin-top: 10px;">
                    <label>Achievements &amp; Responsibilities</label>
                    <textarea name="exp_description" class="form-textarea" rows="3">{{ exp.description }}</textarea>
                </div>
                <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
            </div>
            {% endfor %}
        </div>
        <button type="button" class="btn btn-ghost btn-sm" onclick="addExperienceRow()">+ Add Experience</button>
    </div>

    <!-- Education -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                    <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Education</h3>
                <p class="form-card-sub">Academic degrees and qualifications</p>
            </div>
        </div>

        <div id="educationList">
            {% for edu in parsed.education %}
            <div class="dynamic-row" data-row="education">
                <div class="form-grid form-grid-4">
                    <div class="form-group">
                        <label>Degree</label>
                        <input type="text" name="edu_degree" class="form-input" value="{{ edu.degree }}">
                    </div>
                    <div class="form-group">
                        <label>Institution</label>
                        <input type="text" name="edu_institution" class="form-input" value="{{ edu.institution }}">
                    </div>
                    <div class="form-group">
                        <label>Year</label>
                        <input type="text" name="edu_year" class="form-input" value="{{ edu.year }}">
                    </div>
                    <div class="form-group">
                        <label>Grade / CGPA</label>
                        <input type="text" name="edu_grade" class="form-input" value="{{ edu.grade }}">
                    </div>
                </div>
                <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
            </div>
            {% endfor %}
        </div>
        <button type="button" class="btn btn-ghost btn-sm" onclick="addEducationRow()">+ Add Education</button>
    </div>

    <!-- Projects -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
                    <path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Projects</h3>
                <p class="form-card-sub">Key projects mentioned in your resume</p>
            </div>
        </div>

        <div id="projectList">
            {% for proj in parsed.projects %}
            <div class="dynamic-row" data-row="project">
                <div class="form-grid form-grid-2">
                    <div class="form-group">
                        <label>Project Title</label>
                        <input type="text" name="proj_title" class="form-input" value="{{ proj.title }}">
                    </div>
                    <div class="form-group">
                        <label>Technologies</label>
                        <input type="text" name="proj_tech" class="form-input" value="{{ proj.tech }}">
                    </div>
                </div>
                <div class="form-group" style="margin-top: 10px;">
                    <label>Description</label>
                    <textarea name="proj_description" class="form-textarea" rows="2">{{ proj.description }}</textarea>
                </div>
                <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
            </div>
            {% endfor %}
        </div>
        <button type="button" class="btn btn-ghost btn-sm" onclick="addProjectRow()">+ Add Project</button>
    </div>

    <!-- Certifications -->
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="8" r="7"/>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
                </svg>
            </div>
            <div>
                <h3 class="form-card-title">Certifications &amp; Awards</h3>
                <p class="form-card-sub">One per line</p>
            </div>
        </div>
        <div class="form-group">
            <textarea name="certifications" class="form-textarea" rows="3">{{ parsed.certifications }}</textarea>
        </div>
    </div>

    <!-- Action Bar -->
    <div class="form-actions" style="justify-content: space-between; align-items: center;">
        <label style="display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--purple-pale); cursor: pointer;">
            <input type="checkbox" name="save_to_db" value="1" checked style="accent-color: var(--purple-bright); width: 16px; height: 16px;">
            Save this rebuilt resume to my dashboard resumes
        </label>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="{{ url_for('dashboard') }}" class="btn btn-ghost">Cancel</a>
            <button type="submit" class="btn btn-primary btn-lg">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    <polyline points="7 10 12 15 17 10"/>
                    <line x1="12" y1="15" x2="12" y2="3"/>
                </svg>
                Download Cloned PDF Resume
            </button>
        </div>
    </div>
</form>
{% endif %}

<script>
function selectRebuilderTemplate(tplId, cardEl) {
    document.querySelectorAll('.template-card').forEach(c => c.classList.remove('active'));
    cardEl.classList.add('active');
    document.getElementById('selectedTemplateInput').value = tplId;
}

function addExperienceRow() {
    const list = document.getElementById('experienceList');
    const div = document.createElement('div');
    div.className = 'dynamic-row';
    div.innerHTML = `
        <div class="form-grid form-grid-3">
            <div class="form-group"><label>Job Title / Role</label><input type="text" name="exp_role" class="form-input" placeholder="e.g. QA Engineer"></div>
            <div class="form-group"><label>Company</label><input type="text" name="exp_company" class="form-input" placeholder="e.g. Tech Corp"></div>
            <div class="form-group"><label>Duration</label><input type="text" name="exp_duration" class="form-input" placeholder="2022 - Present"></div>
        </div>
        <div class="form-group" style="margin-top:10px;"><label>Achievements &amp; Responsibilities</label><textarea name="exp_description" class="form-textarea" rows="2" placeholder="Responsibilities..."></textarea></div>
        <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
    `;
    list.appendChild(div);
}

function addEducationRow() {
    const list = document.getElementById('educationList');
    const div = document.createElement('div');
    div.className = 'dynamic-row';
    div.innerHTML = `
        <div class="form-grid form-grid-4">
            <div class="form-group"><label>Degree</label><input type="text" name="edu_degree" class="form-input" placeholder="e.g. MCA"></div>
            <div class="form-group"><label>Institution</label><input type="text" name="edu_institution" class="form-input" placeholder="University"></div>
            <div class="form-group"><label>Year</label><input type="text" name="edu_year" class="form-input" placeholder="2022 - 2024"></div>
            <div class="form-group"><label>Grade / CGPA</label><input type="text" name="edu_grade" class="form-input" placeholder="8.5 CGPA"></div>
        </div>
        <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
    `;
    list.appendChild(div);
}

function addProjectRow() {
    const list = document.getElementById('projectList');
    const div = document.createElement('div');
    div.className = 'dynamic-row';
    div.innerHTML = `
        <div class="form-grid form-grid-2">
            <div class="form-group"><label>Project Title</label><input type="text" name="proj_title" class="form-input" placeholder="Project Name"></div>
            <div class="form-group"><label>Technologies</label><input type="text" name="proj_tech" class="form-input" placeholder="Python, SQL, etc."></div>
        </div>
        <div class="form-group" style="margin-top:10px;"><label>Description</label><textarea name="proj_description" class="form-textarea" rows="2" placeholder="Project details..."></textarea></div>
        <button type="button" class="btn-remove" onclick="this.closest('.dynamic-row').remove()">&times; Remove</button>
    `;
    list.appendChild(div);
}
</script>
{% endblock %}
""",
    'templates/ats_analyzer.html': r"""
{% extends "base.html" %}
{% block title %}ATS Analyzer{% endblock %}
{% block page_title %}ATS Match Analyzer{% endblock %}

{% block content %}
<div class="ats-layout">
    <!-- Input Panel -->
    <div class="ats-input-panel">
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <circle cx="12" cy="12" r="6"/>
                        <circle cx="12" cy="12" r="2"/>
                    </svg>
                </div>
                <div>
                    <h2 class="form-card-title">Analyze Your Resume</h2>
                    <p class="form-card-sub">Compare your resume against a job description</p>
                </div>
            </div>

            <form method="POST" id="atsForm">
                <!-- Resume Source Toggle -->
                <div class="toggle-group">
                    <button type="button" class="toggle-btn active" id="btnPaste" onclick="switchMode('paste')">Paste Text</button>
                    <button type="button" class="toggle-btn" id="btnSaved" onclick="switchMode('saved')">Use Saved Resume</button>
                </div>

                <!-- Paste Mode -->
                <div id="pasteMode">
                    <div class="form-group">
                        <label for="resume_text">Your Resume Text</label>
                        <textarea id="resume_text" name="resume_text" class="form-textarea" rows="8"
                            placeholder="Paste your full resume text here...&#10;&#10;Example:&#10;Software Tester with 2 years of experience in manual testing, Selenium, Java, SQL, and API testing. Proficient in Jira, Agile methodology, and functional testing. Experience with Python scripting for test automation."></textarea>
                    </div>
                </div>

                <!-- Saved Resume Mode -->
                <div id="savedMode" style="display:none;">
                    <div class="form-group">
                        <label for="resume_id">Select a Saved Resume</label>
                        <select id="resume_id" name="resume_id" class="form-select">
                            <option value="">-- Select Resume --</option>
                            {% for r in resume_list %}
                            <option value="{{ r.id }}">{{ r.full_name }} ({{ r.email }})</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label for="job_description">Job Description <span class="required">*</span></label>
                    <textarea id="job_description" name="job_description" class="form-textarea" rows="10"
                        placeholder="Paste the complete job description here...&#10;&#10;Example:&#10;We are looking for a Software Test Engineer with experience in manual testing, Selenium, Java, SQL, Python, API testing, and JIRA. The candidate should have knowledge of Agile methodology and regression testing." required></textarea>
                </div>

                <button type="submit" class="btn btn-primary btn-lg w-full" id="analyzeBtn">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                    </svg>
                    Analyze ATS Match
                </button>
            </form>
        </div>
    </div>

    <!-- Results Panel -->
    <div class="ats-results-panel">
        {% if result %}
            {% if result.error %}
            <div class="alert alert-warning">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                    <line x1="12" y1="9" x2="12" y2="13"/>
                    <line x1="12" y1="17" x2="12.01" y2="17"/>
                </svg>
                <span>{{ result.error }}</span>
            </div>
            {% else %}
            <!-- Score Card -->
            <div class="score-card-main">
                <div class="score-label">ATS Match Score</div>
                <div class="score-ring-container" id="scoreRingContainer">
                    <svg class="score-ring" width="160" height="160" viewBox="0 0 160 160">
                        <defs>
                            <linearGradient id="purpleRingGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#9333ea"/>
                                <stop offset="60%" stop-color="#c084fc"/>
                                <stop offset="100%" stop-color="#f3e8ff"/>
                            </linearGradient>
                            <filter id="purpleRingGlow" x="-20%" y="-20%" width="140%" height="140%">
                                <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#a855f7" flood-opacity="0.6"/>
                            </filter>
                        </defs>
                        <circle cx="80" cy="80" r="66" fill="none" stroke="rgba(168, 85, 247, 0.2)" stroke-width="12"/>
                        <circle cx="80" cy="80" r="66" fill="none"
                            stroke="url(#purpleRingGrad)"
                            stroke-width="12"
                            filter="url(#purpleRingGlow)"
                            stroke-dasharray="{{ (result.score / 100 * 414.69)|round|int }} 414"
                            stroke-linecap="round"
                            transform="rotate(-90 80 80)"
                            class="score-circle"
                            id="scoreCircle"/>
                    </svg>
                    <div class="score-ring-center">
                        <div class="score-number" id="scoreNumber">{{ result.score }}%</div>
                        <div class="score-status {{ 'good' if result.score >= 70 else 'ok' if result.score >= 40 else 'low' }}">
                            {{ 'Excellent' if result.score >= 70 else 'Good' if result.score >= 40 else 'Low' }}
                        </div>
                    </div>
                </div>
                <div class="score-meta">
                    Matched <strong>{{ result.matched|length }}</strong> of <strong>{{ result.jd_skills|length }}</strong> skills
                    &nbsp;|&nbsp; Keyword Density: <strong>{{ result.keyword_density }}%</strong>
                </div>
            </div>

            <!-- Tips -->
            {% if result.tips %}
            <div class="tips-card">
                <h3 class="tips-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 6px;">
                        <line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/>
                        <path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>
                    </svg>
                    Improvement Tips
                </h3>
                <ul class="tips-list">
                    {% for tip in result.tips %}
                    <li>{{ tip }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endif %}

            <!-- Matched Skills -->
            <div class="skills-section">
                <h3 class="skills-section-title skills-matched-title">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="vertical-align: middle; margin-right: 4px;">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                    Matched Skills ({{ result.matched|length }})
                </h3>
                <div class="skills-cloud">
                    {% for skill, cat in result.matched.items() %}
                    <span class="skill-badge skill-matched" title="{{ cat.replace('_',' ').title() }}">{{ skill }}</span>
                    {% endfor %}
                    {% if not result.matched %}
                    <span class="skills-empty">No matched skills found</span>
                    {% endif %}
                </div>
            </div>

            <!-- Missing Skills -->
            <div class="skills-section">
                <h3 class="skills-section-title skills-missing-title">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="vertical-align: middle; margin-right: 4px;">
                        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
                    </svg>
                    Missing Skills ({{ result.missing|length }})
                </h3>
                <div class="skills-cloud">
                    {% for skill, cat in result.missing.items() %}
                    <span class="skill-badge skill-missing" title="{{ cat.replace('_',' ').title() }}">{{ skill }}</span>
                    {% endfor %}
                    {% if not result.missing %}
                    <span class="skills-empty">All required skills matched!</span>
                    {% endif %}
                </div>
            </div>

            <!-- Skill Gap Analysis with Resources -->
            {% if result.gap_analysis %}
            <div class="gap-card">
                <h3 class="gap-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 6px;">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    </svg>
                    Skill Gap - Learning Resources
                </h3>
                <div class="gap-list">
                    {% for gap in result.gap_analysis %}
                    <div class="gap-item">
                        <div class="gap-item-info">
                            <span class="gap-skill">{{ gap.skill }}</span>
                            <span class="gap-category">{{ gap.category }}</span>
                        </div>
                        <a href="{{ gap.resource }}" target="_blank" rel="noopener" class="btn btn-sm btn-outline">Learn &rarr;</a>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endif %}

            <!-- Actions -->
            <div class="ats-actions">
                <a href="{{ url_for('interview_prep') }}" class="btn btn-primary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 6px;">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                    </svg>
                    Generate Interview Questions
                </a>
                <a href="{{ url_for('templates_page') }}" class="btn btn-outline">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 6px;">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                    </svg>
                    Download Resume PDF
                </a>
            </div>
            {% endif %}
        {% else %}
        <!-- Placeholder when no result -->
        <div class="ats-placeholder">
            <div class="placeholder-icon">
                <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <circle cx="12" cy="12" r="6"/>
                    <circle cx="12" cy="12" r="2"/>
                </svg>
            </div>
            <h3>Ready to Analyze</h3>
            <p>Paste your resume text and a job description, then click <strong>Analyze ATS Match</strong> to see your score, matched skills, missing skills, and personalized improvement tips.</p>
            <div class="placeholder-steps">
                <div class="p-step"><span class="p-step-num">1</span> Paste resume or select saved</div>
                <div class="p-step"><span class="p-step-num">2</span> Paste job description</div>
                <div class="p-step"><span class="p-step-num">3</span> See your ATS match score</div>
            </div>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
function switchMode(mode) {
    document.getElementById('pasteMode').style.display = mode === 'paste' ? 'block' : 'none';
    document.getElementById('savedMode').style.display = mode === 'saved' ? 'block' : 'none';
    document.getElementById('resume_id').disabled = mode === 'paste';
    document.getElementById('resume_text').disabled = mode === 'saved';
    document.getElementById('btnPaste').classList.toggle('active', mode === 'paste');
    document.getElementById('btnSaved').classList.toggle('active', mode === 'saved');
}

// Animate score ring on load
window.addEventListener('load', () => {
    const circle = document.getElementById('scoreCircle');
    if (circle) {
        circle.style.transition = 'stroke-dasharray 1.5s ease-in-out';
    }
});
</script>
{% endblock %}
""",
    'templates/interview_prep.html': r"""
{% extends "base.html" %}
{% block title %}Interview Preparation{% endblock %}
{% block page_title %}Interview Question Generator{% endblock %}

{% block content %}
<div class="interview-layout">
    <!-- Input Panel -->
    <div class="interview-input">
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                    </svg>
                </div>
                <div>
                    <h2 class="form-card-title">Generate Questions</h2>
                    <p class="form-card-sub">AI-powered from your job description</p>
                </div>
            </div>
            <form method="POST">
                <div class="form-group">
                    <label for="resume_id">Reference Resume (optional)</label>
                    <select id="resume_id" name="resume_id" class="form-select">
                        <option value="">-- None --</option>
                        {% for r in resume_list %}
                        <option value="{{ r.id }}">{{ r.full_name }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="form-group">
                    <label for="job_description">Job Description <span class="required">*</span></label>
                    <textarea id="job_description" name="job_description" class="form-textarea" rows="12"
                        placeholder="Paste the job description here...&#10;&#10;The more detailed, the more relevant questions you'll get!" required>{{ request.form.get('job_description', '') }}</textarea>
                </div>
                <button type="submit" class="btn btn-primary btn-lg w-full">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                    </svg>
                    Generate Questions
                </button>
            </form>

            {% if not questions %}
            <div class="interview-tips-box">
                <h4>Pro Tips:</h4>
                <ol>
                    <li>Paste the job description</li>
                    <li>Get HR, technical &amp; situational questions</li>
                    <li>Expand each question to see a model answer</li>
                    <li>Practice out loud before your interview!</li>
                </ol>
            </div>
            {% endif %}
        </div>
    </div>

    <!-- Questions Panel -->
    <div class="interview-questions">
        {% if questions %}
        <div class="questions-header">
            <div class="questions-count-chips">
                <span class="count-chip chip-hr">{{ questions.hr|length }} HR</span>
                <span class="count-chip chip-tech">{{ questions.technical|length }} Technical</span>
                <span class="count-chip chip-sit">{{ questions.situational|length }} Situational</span>
            </div>
            {% if questions.role_hints %}
            <div class="role-hints">
                Role detected: {% for r in questions.role_hints %}<span class="role-tag">{{ r }}</span>{% endfor %}
            </div>
            {% endif %}
        </div>

        <!-- Technical Questions -->
        <div class="q-section">
            <h3 class="q-section-title">
                <span class="q-section-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                    </svg>
                </span>
                Technical Questions
                <span class="q-count">{{ questions.technical|length }}</span>
            </h3>
            <div class="q-list">
                {% for q in questions.technical %}
                <div class="q-item" onclick="toggleAnswer(this)">
                    <div class="q-header">
                        <div class="q-skill-tag">{{ q.skill }}</div>
                        <div class="q-text">{{ q.question }}</div>
                        <div class="q-toggle">+</div>
                    </div>
                    <div class="q-answer">
                        <div class="q-answer-label">Model Answer</div>
                        <p>{{ q.answer }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <!-- HR Questions -->
        <div class="q-section">
            <h3 class="q-section-title">
                <span class="q-section-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                        <circle cx="12" cy="7" r="4"/>
                    </svg>
                </span>
                HR &amp; Behavioral Questions
                <span class="q-count">{{ questions.hr|length }}</span>
            </h3>
            <div class="q-list">
                {% for q, a in questions.hr %}
                <div class="q-item" onclick="toggleAnswer(this)">
                    <div class="q-header">
                        <div class="q-skill-tag">HR</div>
                        <div class="q-text">{{ q }}</div>
                        <div class="q-toggle">+</div>
                    </div>
                    <div class="q-answer">
                        <div class="q-answer-label">How to Answer</div>
                        <p>{{ a }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <!-- Situational Questions -->
        <div class="q-section">
            <h3 class="q-section-title">
                <span class="q-section-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="3" width="18" height="18" rx="2"/>
                        <line x1="3" y1="9" x2="21" y2="9"/>
                        <line x1="9" y1="21" x2="9" y2="9"/>
                    </svg>
                </span>
                Situational Questions
                <span class="q-count">{{ questions.situational|length }}</span>
            </h3>
            <div class="q-list">
                {% for q, a in questions.situational %}
                <div class="q-item" onclick="toggleAnswer(this)">
                    <div class="q-header">
                        <div class="q-skill-tag">Situational</div>
                        <div class="q-text">{{ q }}</div>
                        <div class="q-toggle">+</div>
                    </div>
                    <div class="q-answer">
                        <div class="q-answer-label">How to Approach</div>
                        <p>{{ a }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>

        <div class="interview-actions">
            <button onclick="expandAll()" class="btn btn-ghost btn-sm">Expand All Answers</button>
            <button onclick="collapseAll()" class="btn btn-ghost btn-sm">Collapse All</button>
        </div>

        {% else %}
        <!-- Placeholder -->
        <div class="ats-placeholder">
            <div class="placeholder-icon">
                <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                    <line x1="12" y1="17" x2="12.01" y2="17"/>
                </svg>
            </div>
            <h3>Questions will appear here</h3>
            <p>Paste a job description and click <strong>Generate Questions</strong> to get personalized interview questions organized by category, with model answers to help you practice.</p>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
function toggleAnswer(item) {
    item.classList.toggle('open');
    const toggle = item.querySelector('.q-toggle');
    toggle.textContent = item.classList.contains('open') ? '-' : '+';
}

function expandAll() {
    document.querySelectorAll('.q-item').forEach(item => {
        item.classList.add('open');
        item.querySelector('.q-toggle').textContent = '-';
    });
}

function collapseAll() {
    document.querySelectorAll('.q-item').forEach(item => {
        item.classList.remove('open');
        item.querySelector('.q-toggle').textContent = '+';
    });
}
</script>
{% endblock %}
""",
    'templates/tracker.html': r"""
{% extends "base.html" %}
{% block title %}Job Application Tracker{% endblock %}
{% block page_title %}Job Application Tracker{% endblock %}

{% block content %}
<!-- Stats Row -->
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-icon stat-icon-purple">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.total }}</div>
            <div class="stat-label">Total Applied</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-blue">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.by_status.get('Interview', 0) }}</div>
            <div class="stat-label">Interviews</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-green">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.by_status.get('Offer', 0) }}</div>
            <div class="stat-label">Offers</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-icon stat-icon-red">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <line x1="15" y1="9" x2="9" y2="15"/>
                <line x1="9" y1="9" x2="15" y2="15"/>
            </svg>
        </div>
        <div class="stat-info">
            <div class="stat-value">{{ stats.by_status.get('Rejected', 0) }}</div>
            <div class="stat-label">Rejected</div>
        </div>
    </div>
</div>

<div class="tracker-layout">
    <!-- Add Application Form -->
    <div class="tracker-form-panel">
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="12" y1="5" x2="12" y2="19"/>
                        <line x1="5" y1="12" x2="19" y2="12"/>
                    </svg>
                </div>
                <div>
                    <h2 class="form-card-title">Add Application</h2>
                    <p class="form-card-sub">Track a new job application</p>
                </div>
            </div>
            <form method="POST" action="{{ url_for('add_application') }}" id="addAppForm">
                <div class="form-group">
                    <label for="company">Company Name <span class="required">*</span></label>
                    <input type="text" id="company" name="company" class="form-input" placeholder="e.g., TCS, Infosys, Google" required>
                </div>
                <div class="form-group">
                    <label for="role">Job Role <span class="required">*</span></label>
                    <input type="text" id="role" name="role" class="form-input" placeholder="e.g., Software Test Engineer" required>
                </div>
                <div class="form-grid form-grid-2">
                    <div class="form-group">
                        <label for="date_applied">Date Applied</label>
                        <input type="date" id="date_applied" name="date_applied" class="form-input">
                    </div>
                    <div class="form-group">
                        <label for="status">Status</label>
                        <select id="status" name="status" class="form-select">
                            <option value="Applied">Applied</option>
                            <option value="Interview">Interview</option>
                            <option value="Offer">Offer</option>
                            <option value="Rejected">Rejected</option>
                            <option value="Withdrawn">Withdrawn</option>
                        </select>
                    </div>
                </div>
                <div class="form-grid form-grid-2">
                    <div class="form-group">
                        <label for="location">Location</label>
                        <input type="text" id="location" name="location" class="form-input" placeholder="Chennai / Remote">
                    </div>
                    <div class="form-group">
                        <label for="salary">Salary (LPA)</label>
                        <input type="text" id="salary" name="salary" class="form-input" placeholder="e.g., 6 LPA">
                    </div>
                </div>
                <div class="form-group">
                    <label for="job_url">Job URL</label>
                    <input type="url" id="job_url" name="job_url" class="form-input" placeholder="https://...">
                </div>
                <div class="form-group">
                    <label for="notes">Notes</label>
                    <textarea id="notes" name="notes" class="form-textarea" rows="3" placeholder="Referral, recruiter name, follow-up date..."></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-full">Add Application</button>
            </form>
        </div>
    </div>

    <!-- Applications Table -->
    <div class="tracker-table-panel">
        <!-- Filters -->
        <div class="tracker-filters">
            <input type="text" id="filterSearch" class="form-input" placeholder="Search company or role..." oninput="filterTable()">
            <select id="filterStatus" class="form-select" onchange="filterTable()">
                <option value="">All Statuses</option>
                <option value="Applied">Applied</option>
                <option value="Interview">Interview</option>
                <option value="Offer">Offer</option>
                <option value="Rejected">Rejected</option>
                <option value="Withdrawn">Withdrawn</option>
            </select>
        </div>

        {% if applications %}
        <div class="tracker-table-wrapper">
            <table class="tracker-table" id="appTable">
                <thead>
                    <tr>
                        <th>Company</th>
                        <th>Role</th>
                        <th>Date</th>
                        <th>Status</th>
                        <th>Location</th>
                        <th>Notes</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for app in applications %}
                    <tr class="app-row" data-company="{{ app.company|lower }}" data-role="{{ app.role|lower }}" data-status="{{ app.status }}">
                        <td class="app-company">
                            <div class="company-avatar">{{ app.company[0].upper() }}</div>
                            <div>
                                <div class="company-name">{{ app.company }}</div>
                                {% if app.job_url %}<a href="{{ app.job_url }}" target="_blank" class="job-link">View Job &nearr;</a>{% endif %}
                            </div>
                        </td>
                        <td class="app-role">{{ app.role }}</td>
                        <td>{{ app.date_applied or '-' }}</td>
                        <td>
                            <span class="status-badge status-{{ app.status|lower }}">
                                {{ app.status }}
                            </span>
                        </td>
                        <td>{{ app.location or '-' }}</td>
                        <td class="app-notes">{{ app.notes or '-' }}</td>
                        <td class="app-actions">
                            <button class="btn btn-sm btn-ghost" onclick="openEditModal({{ app.id }}, '{{ app.company }}', '{{ app.role }}', '{{ app.date_applied }}', '{{ app.status }}', '{{ app.location }}', '{{ app.salary }}', '{{ app.job_url }}', {{ ('`' + app.notes + '`') if app.notes else 'null' }})">Edit</button>
                            <form method="POST" action="{{ url_for('delete_application', app_id=app.id) }}" style="display:inline" onsubmit="return confirm('Delete this application?')">
                                <button type="submit" class="btn btn-sm btn-danger">Delete</button>
                            </form>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="ats-placeholder">
            <div class="placeholder-icon">
                <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>
                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"/>
                </svg>
            </div>
            <h3>No Applications Yet</h3>
            <p>Add your first job application using the form on the left. Track every company you apply to and monitor your progress.</p>
        </div>
        {% endif %}
    </div>
</div>

<!-- Edit Modal -->
<div class="modal-overlay" id="editModal">
    <div class="modal">
        <div class="modal-header">
            <h3>Edit Application</h3>
            <button onclick="closeEditModal()" class="modal-close">&times;</button>
        </div>
        <form method="POST" id="editForm">
            <div class="form-grid form-grid-2">
                <div class="form-group">
                    <label>Company</label>
                    <input type="text" name="company" id="edit_company" class="form-input" required>
                </div>
                <div class="form-group">
                    <label>Role</label>
                    <input type="text" name="role" id="edit_role" class="form-input" required>
                </div>
                <div class="form-group">
                    <label>Date Applied</label>
                    <input type="date" name="date_applied" id="edit_date" class="form-input">
                </div>
                <div class="form-group">
                    <label>Status</label>
                    <select name="status" id="edit_status" class="form-select">
                        <option value="Applied">Applied</option>
                        <option value="Interview">Interview</option>
                        <option value="Offer">Offer</option>
                        <option value="Rejected">Rejected</option>
                        <option value="Withdrawn">Withdrawn</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Location</label>
                    <input type="text" name="location" id="edit_location" class="form-input">
                </div>
                <div class="form-group">
                    <label>Salary</label>
                    <input type="text" name="salary" id="edit_salary" class="form-input">
                </div>
            </div>
            <div class="form-group">
                <label>Job URL</label>
                <input type="url" name="job_url" id="edit_job_url" class="form-input">
            </div>
            <div class="form-group">
                <label>Notes</label>
                <textarea name="notes" id="edit_notes" class="form-textarea" rows="3"></textarea>
            </div>
            <div class="modal-actions">
                <button type="button" onclick="closeEditModal()" class="btn btn-ghost">Cancel</button>
                <button type="submit" class="btn btn-primary">Save Changes</button>
            </div>
        </form>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="{{ url_for('static', filename='js/tracker.js') }}"></script>
{% endblock %}
""",
    'templates/templates_page.html': r"""
{% extends "base.html" %}
{% block title %}Resume Templates{% endblock %}
{% block page_title %}Resume Templates & PDF Download{% endblock %}

{% block content %}
<div class="templates-layout">
    <!-- Template Selector -->
    <div class="templates-grid-panel">
        <div class="section-header">
            <h2 class="section-title">Choose a Template</h2>
            <p class="section-sub">Select a professional template that suits your target role</p>
        </div>

        <div class="template-cards">
            <!-- Modern Template -->
            <div class="template-card" id="tpl-modern" onclick="selectTemplate('modern')">
                <div class="template-preview modern-preview">
                    <div class="tpl-header-bar"></div>
                    <div class="tpl-name-block"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                    <div class="tpl-divider"></div>
                    <div class="tpl-line"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                </div>
                <div class="template-card-info">
                    <div class="template-name">Modern</div>
                    <div class="template-desc">Clean layout with royal purple header. High ATS ranking.</div>
                    <span class="template-badge tpl-badge-modern">Popular</span>
                </div>
                <div class="template-check" id="check-modern"></div>
            </div>

            <!-- Classic Template -->
            <div class="template-card" id="tpl-classic" onclick="selectTemplate('classic')">
                <div class="template-preview classic-preview">
                    <div class="tpl-classic-header"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line"></div>
                    <div class="tpl-classic-rule"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                    <div class="tpl-classic-rule"></div>
                    <div class="tpl-line"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                </div>
                <div class="template-card-info">
                    <div class="template-name">Classic</div>
                    <div class="template-desc">Traditional single-column format. Ideal for formal industries.</div>
                    <span class="template-badge tpl-badge-classic">Professional</span>
                </div>
                <div class="template-check" id="check-classic"></div>
            </div>

            <!-- Minimal Template -->
            <div class="template-card" id="tpl-minimal" onclick="selectTemplate('minimal')">
                <div class="template-preview minimal-preview">
                    <div class="tpl-min-name"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                    <div style="height:8px"></div>
                    <div class="tpl-min-section"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line"></div>
                    <div class="tpl-min-section"></div>
                    <div class="tpl-line tpl-line-wide"></div>
                    <div class="tpl-line tpl-line-medium"></div>
                </div>
                <div class="template-card-info">
                    <div class="template-name">Minimal</div>
                    <div class="template-desc">Ultra-clean minimalist design. Modern and ATS-friendly.</div>
                    <span class="template-badge tpl-badge-minimal">ATS-Friendly</span>
                </div>
                <div class="template-check" id="check-minimal"></div>
            </div>
        </div>
    </div>

    <!-- Download Panel -->
    <div class="download-panel">
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-icon">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                    </svg>
                </div>
                <div>
                    <h2 class="form-card-title">Generate PDF</h2>
                    <p class="form-card-sub">Select resume and template, then download</p>
                </div>
            </div>

            <form method="POST" action="{{ url_for('download_pdf') }}" id="pdfForm">
                <input type="hidden" name="template_name" id="selectedTemplate" value="modern">

                <div class="form-group">
                    <label for="resume_id">Select Resume</label>
                    <select id="resume_id" name="resume_id" class="form-select" required>
                        <option value="">-- Select a resume --</option>
                        {% for r in resume_list %}
                        <option value="{{ r.id }}">{{ r.full_name }} ({{ r.email }})</option>
                        {% endfor %}
                    </select>
                    {% if not resume_list %}
                    <div class="form-hint">No resumes saved yet. <a href="{{ url_for('resume_builder') }}">Create one first &rarr;</a></div>
                    {% endif %}
                </div>

                <div class="selected-template-display">
                    <div class="std-label">Selected Template:</div>
                    <div class="std-name" id="selectedTemplateName">Modern</div>
                </div>

                <button type="submit" class="btn btn-primary btn-lg w-full" id="downloadBtn">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
                    </svg>
                    Download PDF Resume
                </button>
            </form>

            <div class="download-tips">
                <h4 style="display: flex; align-items: center; gap: 6px;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <line x1="12" y1="16" x2="12" y2="12"/>
                        <line x1="12" y1="8" x2="12.01" y2="8"/>
                    </svg>
                    PDF Tips
                </h4>
                <ul>
                    <li>Fill out your resume completely before downloading</li>
                    <li>Modern template is best for tech/IT roles</li>
                    <li>Classic template is best for formal sectors (banking, gov)</li>
                    <li>Minimal template has the highest ATS compatibility</li>
                    <li>PDF is generated with all sections you filled in the builder</li>
                </ul>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
let selectedTemplate = 'modern';

function selectTemplate(name) {
    // Remove all active states
    document.querySelectorAll('.template-card').forEach(c => c.classList.remove('active'));
    document.querySelectorAll('.template-check').forEach(c => c.classList.remove('visible'));

    // Set active
    document.getElementById('tpl-' + name).classList.add('active');
    document.getElementById('check-' + name).classList.add('visible');
    document.getElementById('selectedTemplate').value = name;

    const names = { modern: 'Modern', classic: 'Classic', minimal: 'Minimal' };
    document.getElementById('selectedTemplateName').textContent = names[name];
    selectedTemplate = name;
}

// Default selection
selectTemplate('modern');
</script>
{% endblock %}
""",
    'templates/upload.html': r"""
{% extends "base.html" %}
{% block title %}Upload Resume{% endblock %}
{% block page_title %}Upload & Parse Resume{% endblock %}

{% block content %}
<div class="upload-layout">
    <div class="form-card" style="max-width: 640px; margin: 0 auto;">
        <div class="form-card-header">
            <div class="form-card-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    <polyline points="17 8 12 3 7 8"/>
                    <line x1="12" y1="3" x2="12" y2="15"/>
                </svg>
            </div>
            <div>
                <h2 class="form-card-title">Upload Your Resume</h2>
                <p class="form-card-sub">Extract text from PDF or DOCX files</p>
            </div>
        </div>

        <form method="POST" enctype="multipart/form-data">
            <div class="upload-dropzone" id="dropzone" onclick="document.getElementById('resume_file').click()">
                <div class="dropzone-icon">
                    <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="12" y1="18" x2="12" y2="12"/>
                        <polyline points="9 15 12 12 15 15"/>
                    </svg>
                </div>
                <div class="dropzone-text">Click to upload or drag &amp; drop</div>
                <div class="dropzone-sub">PDF or DOCX - max 10 MB</div>
                <input type="file" id="resume_file" name="resume_file" accept=".pdf,.docx" style="display:none" onchange="showFilename(this)">
                <div class="dropzone-filename" id="dropzoneFilename"></div>
            </div>

            <button type="submit" class="btn btn-primary w-full" style="margin-top: 16px;">
                Extract Text from File
            </button>
        </form>

        {% if extracted_text %}
        <div class="upload-result">
            <h3 style="color: var(--purple-neon); margin-bottom: 12px;">Text Extracted Successfully</h3>
            <div class="upload-text-box">{{ extracted_text }}</div>
            <p style="color: var(--text-muted); font-size: 13px; margin-top: 12px;">
                Copy this text and paste it into the ATS Analyzer or use it to fill the Resume Builder.
            </p>
            <div style="display:flex; gap:12px; margin-top: 12px;">
                <a href="{{ url_for('ats_analyzer') }}" class="btn btn-primary btn-sm">Use in ATS Analyzer</a>
                <a href="{{ url_for('resume_builder') }}" class="btn btn-outline btn-sm">Fill Resume Builder</a>
            </div>
        </div>
        {% endif %}

        <div class="upload-note">
            <strong>Note:</strong> Upload requires <code>PyMuPDF</code> (PDF) or <code>python-docx</code> (DOCX) to be installed. If extraction fails, copy the text manually and paste it into the ATS Analyzer.
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
function showFilename(input) {
    const el = document.getElementById('dropzoneFilename');
    if (input.files.length > 0) {
        el.textContent = input.files[0].name;
        el.style.display = 'block';
    }
}

// Drag and drop
const dropzone = document.getElementById('dropzone');
dropzone.addEventListener('dragover', e => { e.preventDefault(); dropzone.classList.add('dragover'); });
dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
dropzone.addEventListener('drop', e => {
    e.preventDefault();
    dropzone.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    if (file) {
        const input = document.getElementById('resume_file');
        const dt = new DataTransfer();
        dt.items.add(file);
        input.files = dt.files;
        showFilename(input);
    }
});
</script>
{% endblock %}
""",
    'templates/resume_builder.html': r"""
{% extends "base.html" %}
{% block title %}Resume Builder{% endblock %}
{% block page_title %}{% if edit %}Edit Resume{% else %}Build New Resume{% endif %}{% endblock %}

{% block content %}
<form method="POST" id="resumeForm">

<!-- Personal Information -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Personal Information</h2>
            <p class="form-card-sub">Your basic contact details</p>
        </div>
    </div>
    <div class="form-grid form-grid-2">
        <div class="form-group">
            <label for="full_name">Full Name <span class="required">*</span></label>
            <input type="text" id="full_name" name="full_name" class="form-input"
                placeholder="e.g., Devadharshini R" required
                value="{{ resume.full_name if resume else '' }}">
        </div>
        <div class="form-group">
            <label for="email">Email Address <span class="required">*</span></label>
            <input type="email" id="email" name="email" class="form-input"
                placeholder="you@email.com" required
                value="{{ resume.email if resume else '' }}">
        </div>
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="text" id="phone" name="phone" class="form-input"
                placeholder="+91 98765 43210"
                value="{{ resume.phone if resume else '' }}">
        </div>
        <div class="form-group">
            <label for="location">Location</label>
            <input type="text" id="location" name="location" class="form-input"
                placeholder="Chennai, Tamil Nadu"
                value="{{ resume.location if resume else '' }}">
        </div>
        <div class="form-group">
            <label for="linkedin">LinkedIn Profile URL</label>
            <input type="url" id="linkedin" name="linkedin" class="form-input"
                placeholder="https://linkedin.com/in/yourprofile"
                value="{{ resume.linkedin if resume else '' }}">
        </div>
        <div class="form-group">
            <label for="portfolio">Portfolio / GitHub URL</label>
            <input type="url" id="portfolio" name="portfolio" class="form-input"
                placeholder="https://github.com/yourname"
                value="{{ resume.portfolio if resume else '' }}">
        </div>
    </div>
    <div class="form-group">
        <label for="summary">Professional Summary</label>
        <textarea id="summary" name="summary" class="form-textarea" rows="3"
            placeholder="Write a compelling 2-3 sentence summary of your professional background, key skills, and career goals...">{{ resume.summary if resume else '' }}</textarea>
    </div>
</div>

<!-- Education -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                <path d="M6 12v5c3 3 9 3 12 0v-5"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Education</h2>
            <p class="form-card-sub">Academic qualifications</p>
        </div>
    </div>
    <div id="educationList">
        {% if resume and resume.education %}
            {% for edu in resume.education %}
            <div class="dynamic-row" data-row="education">
                <div class="form-grid form-grid-4">
                    <div class="form-group">
                        <label>Degree / Course</label>
                        <input type="text" name="edu_degree" class="form-input" placeholder="MCA / B.Sc. CS" value="{{ edu.degree }}">
                    </div>
                    <div class="form-group">
                        <label>Institution</label>
                        <input type="text" name="edu_institution" class="form-input" placeholder="University Name" value="{{ edu.institution }}">
                    </div>
                    <div class="form-group">
                        <label>Year</label>
                        <input type="text" name="edu_year" class="form-input" placeholder="2022 - 2024" value="{{ edu.year }}">
                    </div>
                    <div class="form-group">
                        <label>Grade / CGPA</label>
                        <input type="text" name="edu_grade" class="form-input" placeholder="8.5 CGPA" value="{{ edu.grade }}">
                    </div>
                </div>
                <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
            </div>
            {% endfor %}
        {% else %}
        <div class="dynamic-row" data-row="education">
            <div class="form-grid form-grid-4">
                <div class="form-group">
                    <label>Degree / Course</label>
                    <input type="text" name="edu_degree" class="form-input" placeholder="MCA / B.Sc. CS">
                </div>
                <div class="form-group">
                    <label>Institution</label>
                    <input type="text" name="edu_institution" class="form-input" placeholder="University Name">
                </div>
                <div class="form-group">
                    <label>Year</label>
                    <input type="text" name="edu_year" class="form-input" placeholder="2022 - 2024">
                </div>
                <div class="form-group">
                    <label>Grade / CGPA</label>
                    <input type="text" name="edu_grade" class="form-input" placeholder="8.5 CGPA">
                </div>
            </div>
            <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
        </div>
        {% endif %}
    </div>
    <button type="button" class="btn btn-ghost btn-sm" onclick="addEducation()">+ Add Education</button>
</div>

<!-- Work Experience -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Work Experience</h2>
            <p class="form-card-sub">Jobs, internships, and roles</p>
        </div>
    </div>
    <div id="experienceList">
        {% if resume and resume.experience %}
            {% for exp in resume.experience %}
            <div class="dynamic-row" data-row="experience">
                <div class="form-grid form-grid-3">
                    <div class="form-group">
                        <label>Job Title / Role</label>
                        <input type="text" name="exp_role" class="form-input" placeholder="Software Tester" value="{{ exp.role }}">
                    </div>
                    <div class="form-group">
                        <label>Company</label>
                        <input type="text" name="exp_company" class="form-input" placeholder="Company Name" value="{{ exp.company }}">
                    </div>
                    <div class="form-group">
                        <label>Duration</label>
                        <input type="text" name="exp_duration" class="form-input" placeholder="Jun 2023 - Present" value="{{ exp.duration }}">
                    </div>
                </div>
                <div class="form-group">
                    <label>Responsibilities &amp; Achievements</label>
                    <textarea name="exp_description" class="form-textarea" rows="3"
                        placeholder="- Designed and executed manual test cases for web applications&#10;- Automated regression tests using Selenium and Java&#10;- Reduced bug escape rate by 30%">{{ exp.description }}</textarea>
                </div>
                <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
            </div>
            {% endfor %}
        {% else %}
        <div class="dynamic-row" data-row="experience">
            <div class="form-grid form-grid-3">
                <div class="form-group">
                    <label>Job Title / Role</label>
                    <input type="text" name="exp_role" class="form-input" placeholder="Software Tester">
                </div>
                <div class="form-group">
                    <label>Company</label>
                    <input type="text" name="exp_company" class="form-input" placeholder="Company Name">
                </div>
                <div class="form-group">
                    <label>Duration</label>
                    <input type="text" name="exp_duration" class="form-input" placeholder="Jun 2023 - Present">
                </div>
            </div>
            <div class="form-group">
                <label>Responsibilities &amp; Achievements</label>
                <textarea name="exp_description" class="form-textarea" rows="3"
                    placeholder="- Describe your responsibilities and achievements (one per line)..."></textarea>
            </div>
            <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
        </div>
        {% endif %}
    </div>
    <button type="button" class="btn btn-ghost btn-sm" onclick="addExperience()">+ Add Experience</button>
</div>

<!-- Skills -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Skills</h2>
            <p class="form-card-sub">Technical and soft skills - comma or newline separated</p>
        </div>
    </div>
    <div class="form-group">
        <textarea id="skills" name="skills" class="form-textarea" rows="4"
            placeholder="Python, Java, SQL, Selenium, Manual Testing, Agile, JIRA, Git, HTML, CSS">{{ resume.skills if resume else '' }}</textarea>
        <div class="form-hint">Tip: Include skills that match the job descriptions you're targeting</div>
    </div>
</div>

<!-- Projects -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
                <path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
                <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>
                <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Projects</h2>
            <p class="form-card-sub">Academic, personal, or professional projects</p>
        </div>
    </div>
    <div id="projectList">
        {% if resume and resume.projects %}
            {% for proj in resume.projects %}
            <div class="dynamic-row" data-row="project">
                <div class="form-grid form-grid-2">
                    <div class="form-group">
                        <label>Project Title</label>
                        <input type="text" name="proj_title" class="form-input" placeholder="ATS Resume Builder" value="{{ proj.title }}">
                    </div>
                    <div class="form-group">
                        <label>Technologies Used</label>
                        <input type="text" name="proj_tech" class="form-input" placeholder="Python, Flask, SQLite" value="{{ proj.tech }}">
                    </div>
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea name="proj_description" class="form-textarea" rows="2"
                        placeholder="Brief description of the project and your contribution...">{{ proj.description }}</textarea>
                </div>
                <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
            </div>
            {% endfor %}
        {% else %}
        <div class="dynamic-row" data-row="project">
            <div class="form-grid form-grid-2">
                <div class="form-group">
                    <label>Project Title</label>
                    <input type="text" name="proj_title" class="form-input" placeholder="ATS Resume Builder">
                </div>
                <div class="form-group">
                    <label>Technologies Used</label>
                    <input type="text" name="proj_tech" class="form-input" placeholder="Python, Flask, SQLite">
                </div>
            </div>
            <div class="form-group">
                <label>Description</label>
                <textarea name="proj_description" class="form-textarea" rows="2"
                    placeholder="Brief description of the project and your contribution..."></textarea>
            </div>
            <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
        </div>
        {% endif %}
    </div>
    <button type="button" class="btn btn-ghost btn-sm" onclick="addProject()">+ Add Project</button>
</div>

<!-- Certifications -->
<div class="form-card">
    <div class="form-card-header">
        <div class="form-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="8" r="7"/>
                <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
            </svg>
        </div>
        <div>
            <h2 class="form-card-title">Certifications &amp; Achievements</h2>
            <p class="form-card-sub">One per line</p>
        </div>
    </div>
    <div class="form-group">
        <textarea id="certifications" name="certifications" class="form-textarea" rows="4"
            placeholder="AWS Certified Cloud Practitioner - 2024&#10;Selenium WebDriver with Java - Udemy&#10;Postman API Testing - Coursera">{{ resume.certifications if resume else '' }}</textarea>
    </div>
</div>

<!-- Submit -->
<div class="form-actions">
    <a href="{{ url_for('dashboard') }}" class="btn btn-ghost">Cancel</a>
    <button type="submit" class="btn btn-primary btn-lg" id="saveBtn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/>
            <polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/>
        </svg>
        {% if edit %}Update Resume{% else %}Save Resume{% endif %}
    </button>
</div>

</form>
{% endblock %}

{% block scripts %}
<script src="{{ url_for('static', filename='js/resume_builder.js') }}"></script>
{% endblock %}
""",
    'templates/view_resume.html': r"""
{% extends "base.html" %}
{% block title %}View Resume{% endblock %}
{% block page_title %}Resume Preview{% endblock %}

{% block content %}
<div class="resume-view-header">
    <div class="resume-view-actions">
        <a href="{{ url_for('edit_resume', resume_id=resume.id) }}" class="btn btn-outline">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; margin-right:4px;">
                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
            </svg>
            Edit
        </a>
        <a href="{{ url_for('ats_analyzer') }}" class="btn btn-outline">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; margin-right:4px;">
                <circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>
            </svg>
            Analyze ATS
        </a>
        <a href="{{ url_for('pdf_rebuilder') }}?resume_id={{ resume.id }}" class="btn btn-secondary" style="background: rgba(147, 51, 234, 0.35); border: 1px solid rgba(192, 132, 252, 0.45); color: #f3e8ff;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; margin-right:4px;">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <path d="M12 18v-6M9 15l3-3 3 3"/>
            </svg>
            Rebuild in PDF
        </a>
        <a href="{{ url_for('templates_page') }}" class="btn btn-primary">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; margin-right:4px;">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
            </svg>
            Download PDF
        </a>
        <form method="POST" action="{{ url_for('delete_resume', resume_id=resume.id) }}" style="display:inline" onsubmit="return confirm('Delete this resume?')">
            <button class="btn btn-danger">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; margin-right:4px;">
                    <polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
                </svg>
                Delete
            </button>
        </form>
    </div>
</div>

<!-- Resume Preview Card -->
<div class="resume-preview-card">
    <!-- Header -->
    <div class="rp-header">
        <div class="rp-avatar">{{ resume.full_name[0].upper() if resume.full_name else '?' }}</div>
        <div class="rp-header-info">
            <h1 class="rp-name">{{ resume.full_name or 'Name' }}</h1>
            <div class="rp-contacts">
                {% if resume.email %}<span>{{ resume.email }}</span>{% endif %}
                {% if resume.phone %}<span>{{ resume.phone }}</span>{% endif %}
                {% if resume.location %}<span>{{ resume.location }}</span>{% endif %}
                {% if resume.linkedin %}<a href="{{ resume.linkedin }}" target="_blank">LinkedIn &nearr;</a>{% endif %}
                {% if resume.portfolio %}<a href="{{ resume.portfolio }}" target="_blank">Portfolio &nearr;</a>{% endif %}
            </div>
        </div>
    </div>

    {% if resume.summary %}
    <div class="rp-section">
        <div class="rp-section-title">Professional Summary</div>
        <p class="rp-summary">{{ resume.summary }}</p>
    </div>
    {% endif %}

    {% if resume.skills %}
    <div class="rp-section">
        <div class="rp-section-title">Skills</div>
        <div class="skills-cloud">
            {% for skill in resume.skills.replace('\n', ',').split(',') %}
                {% if skill.strip() %}
                <span class="skill-badge skill-neutral">{{ skill.strip() }}</span>
                {% endif %}
            {% endfor %}
        </div>
    </div>
    {% endif %}

    {% if resume.experience %}
    <div class="rp-section">
        <div class="rp-section-title">Work Experience</div>
        {% for exp in resume.experience %}
        <div class="rp-exp-item">
            <div class="rp-exp-header">
                <div class="rp-exp-role">{{ exp.role }}</div>
                <div class="rp-exp-meta">{{ exp.company }}{% if exp.duration %} | {{ exp.duration }}{% endif %}</div>
            </div>
            {% if exp.description %}
            <div class="rp-exp-desc">
                {% for line in exp.description.split('\n') %}{% if line.strip() %}<div class="rp-bullet">{{ line.strip().lstrip('*- ').strip() }}</div>{% endif %}{% endfor %}
            </div>
            {% endif %}
        </div>
        {% endfor %}
    </div>
    {% endif %}

    {% if resume.education %}
    <div class="rp-section">
        <div class="rp-section-title">Education</div>
        {% for edu in resume.education %}
        <div class="rp-edu-item">
            <div class="rp-edu-degree">{{ edu.degree }}</div>
            <div class="rp-edu-meta">{{ edu.institution }}{% if edu.year %} | {{ edu.year }}{% endif %}{% if edu.grade %} | {{ edu.grade }}{% endif %}</div>
        </div>
        {% endfor %}
    </div>
    {% endif %}

    {% if resume.projects %}
    <div class="rp-section">
        <div class="rp-section-title">Projects</div>
        {% for proj in resume.projects %}
        <div class="rp-exp-item">
            <div class="rp-exp-header">
                <div class="rp-exp-role">{{ proj.title }}</div>
                {% if proj.tech %}<div class="rp-exp-meta">{{ proj.tech }}</div>{% endif %}
            </div>
            {% if proj.description %}
            <div class="rp-exp-desc">
                {% for line in proj.description.split('\n') %}{% if line.strip() %}<div class="rp-bullet">{{ line.strip().lstrip('*- ').strip() }}</div>{% endif %}{% endfor %}
            </div>
            {% endif %}
        </div>
        {% endfor %}
    </div>
    {% endif %}

    {% if resume.certifications %}
    <div class="rp-section">
        <div class="rp-section-title">Certifications</div>
        {% for cert in resume.certifications.split('\n') %}
            {% if cert.strip() %}
            <div class="rp-bullet">{{ cert.strip().lstrip('*- ').strip() }}</div>
            {% endif %}
        {% endfor %}
    </div>
    {% endif %}
</div>
{% endblock %}
""",
    'static/css/style.css': r"""
/* ============================================================
   ATS RESUME BUILDER - ALL-PURPLE CYBERPUNK GLASS THEME
   Universal Device Optimization: Mobile, Tablet, Laptop, 4K
   ============================================================ */

/* -- Global Custom Properties: Exclusive Purple Palette -- */
:root {
    /* Cosmic Purple Background Tones */
    --bg-darkest:    #060012;
    --bg-dark:       #0b001f;
    --bg-mid:        #12002f;
    --bg-card:       rgba(24, 6, 52, 0.72);
    --bg-card-hover: rgba(38, 10, 80, 0.80);
    --bg-input:      rgba(10, 1, 26, 0.65);
    --bg-input-focus:rgba(26, 5, 58, 0.80);

    /* Purple Spectrum (Accents & Vibrancy) */
    --purple-deep:   #581c87;
    --purple-royal:  #7c3aed;
    --purple-vivid:  #9333ea;
    --purple-bright: #a855f7;
    --purple-neon:   #c084fc;
    --purple-soft:   #d8b4fe;
    --purple-light:  #e9d5ff;
    --purple-pale:   #f5edff;

    /* Luminous Borders & Glows */
    --border-subtle: rgba(168, 85, 247, 0.18);
    --border-glow:   rgba(192, 132, 252, 0.42);
    --border-focus:  #c084fc;
    --glow-shadow:   0 0 28px rgba(168, 85, 247, 0.32);
    --glow-intense:  0 0 38px rgba(192, 132, 252, 0.50);

    /* Purple Themed Status Variants */
    --status-1:      rgba(216, 180, 254, 0.22);
    --status-1-text: #f5edff;
    --status-1-bord: rgba(216, 180, 254, 0.45);

    --status-2:      rgba(192, 132, 252, 0.20);
    --status-2-text: #e9d5ff;
    --status-2-bord: rgba(192, 132, 252, 0.40);

    --status-3:      rgba(147, 51, 234, 0.22);
    --status-3-text: #d8b4fe;
    --status-3-bord: rgba(168, 85, 247, 0.40);

    --status-4:      rgba(88, 28, 135, 0.30);
    --status-4-text: #c4b5fd;
    --status-4-bord: rgba(124, 58, 237, 0.35);

    /* Typography */
    --text-primary:   #fdfaff;
    --text-secondary: #d8b4fe;
    --text-muted:     #a796c9;
    --text-dim:       #746196;

    /* Geometry */
    --sidebar-w:  260px;
    --topbar-h:   62px;
    --radius-lg:  20px;
    --radius-md:  14px;
    --radius-sm:  9px;

    /* Physics */
    --ease-smooth: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

/* -- Reset & Cross-Device Base ----------------------------- */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
}

html {
    scroll-behavior: smooth;
    font-size: 16px;
    height: 100%;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--bg-darkest);
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

a {
    color: inherit;
    text-decoration: none;
}

button, input, textarea, select {
    font-family: inherit;
}

/* -- Dynamic Ambient Animated Purple Nebulae --------------- */
@keyframes cosmicPurpleShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes purpleOrbFloatA {
    0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
    33%       { transform: translate3d(55px, -75px, 0) scale(1.15); }
    66%       { transform: translate3d(-45px, 45px, 0) scale(0.92); }
}

@keyframes purpleOrbFloatB {
    0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
    50%       { transform: translate3d(-65px, 60px, 0) scale(1.12); }
}

body::before {
    content: '';
    position: fixed;
    inset: 0;
    z-index: -2;
    background: linear-gradient(
        135deg,
        #050010 0%,
        #0c0024 18%,
        #1b0048 38%,
        #0f002d 55%,
        #270066 75%,
        #120033 90%,
        #050010 100%
    );
    background-size: 400% 400%;
    animation: cosmicPurpleShift 16s ease infinite;
    pointer-events: none;
    will-change: background-position;
}

body::after {
    content: '';
    position: fixed;
    inset: 0;
    z-index: -1;
    background:
        radial-gradient(ellipse 55vw 48vh at 15% 20%, rgba(147, 51, 234, 0.32) 0%, transparent 68%),
        radial-gradient(ellipse 48vw 42vh at 85% 80%, rgba(124, 58, 237, 0.28) 0%, transparent 65%),
        radial-gradient(ellipse 38vw 32vh at 50% 48%, rgba(192, 132, 252, 0.16) 0%, transparent 60%),
        radial-gradient(ellipse 30vw 30vh at 80% 12%, rgba(216, 180, 254, 0.14) 0%, transparent 55%);
    animation: purpleOrbFloatA 22s ease-in-out infinite;
    pointer-events: none;
    will-change: transform;
}

/* -- Custom Purple Scrollbars ------------------------------ */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: rgba(11, 0, 31, 0.5);
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--purple-vivid), var(--purple-royal));
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--purple-neon);
}

/* ============================================================
   SIDEBAR NAVIGATION
   ============================================================ */
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: var(--sidebar-w);
    height: 100vh;
    height: 100dvh;
    background: rgba(14, 2, 38, 0.88);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border-right: 1px solid var(--border-subtle);
    display: flex;
    flex-direction: column;
    z-index: 400;
    transition: transform 0.32s cubic-bezier(0.4, 0, 0.2, 1);
    overflow-y: auto;
    overflow-x: hidden;
    box-shadow: 4px 0 35px rgba(124, 58, 237, 0.15);
}

.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 18px 18px;
    border-bottom: 1px solid var(--border-subtle);
    flex-shrink: 0;
    position: relative;
}

.brand-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.brand-text {
    display: flex;
    flex-direction: column;
}

.brand-name {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 800;
    background: linear-gradient(90deg, #ffffff 0%, var(--purple-neon) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.2px;
}

.brand-sub {
    font-size: 10px;
    color: var(--purple-bright);
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.sidebar-close-btn {
    display: none;
    margin-left: auto;
    background: rgba(168, 85, 247, 0.15);
    border: 1px solid var(--border-subtle);
    color: var(--text-secondary);
    width: 32px;
    height: 32px;
    border-radius: 8px;
    font-size: 14px;
    cursor: pointer;
    align-items: center;
    justify-content: center;
    transition: var(--ease-smooth);
}
.sidebar-close-btn:hover {
    background: rgba(168, 85, 247, 0.3);
    color: #ffffff;
}

.sidebar-nav {
    flex: 1;
    padding: 14px 10px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    overflow-y: auto;
}

.nav-section-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: var(--text-dim);
    padding: 14px 12px 6px;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 11px 14px;
    border-radius: var(--radius-sm);
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 500;
    transition: var(--ease-smooth);
    position: relative;
    min-height: 44px;
}

.nav-item:hover {
    background: rgba(168, 85, 247, 0.14);
    color: var(--text-primary);
    transform: translateX(3px);
}

.nav-item.active {
    background: linear-gradient(90deg, rgba(147, 51, 234, 0.28), rgba(168, 85, 247, 0.12));
    color: var(--purple-pale);
    font-weight: 700;
    border: 1px solid rgba(168, 85, 247, 0.3);
}

.nav-item.active::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 3.5px;
    height: 22px;
    background: linear-gradient(180deg, var(--purple-bright), var(--purple-neon));
    border-radius: 0 4px 4px 0;
    box-shadow: 0 0 10px var(--purple-bright);
}

.nav-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    flex-shrink: 0;
}

.nav-label {
    flex: 1;
    white-space: nowrap;
}

.nav-badge {
    font-size: 10px;
    background: linear-gradient(135deg, var(--purple-royal), var(--purple-bright));
    color: #ffffff;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 700;
    box-shadow: 0 0 10px rgba(168, 85, 247, 0.5);
}

.sidebar-footer {
    padding: 14px;
    border-top: 1px solid var(--border-subtle);
    flex-shrink: 0;
}

.sidebar-footer-card {
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.2), rgba(168, 85, 247, 0.1));
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.footer-icon {
    font-size: 22px;
    line-height: 1;
}

.footer-title {
    font-size: 12px;
    font-weight: 700;
    color: var(--text-primary);
}

.footer-sub {
    font-size: 11px;
    color: var(--text-secondary);
}

/* Mobile Overlay */
.sidebar-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(5, 0, 16, 0.72);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    z-index: 350;
    transition: opacity 0.3s ease;
}

/* ============================================================
   TOPBAR & MAIN WRAPPER
   ============================================================ */
.main-wrapper {
    margin-left: var(--sidebar-w);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    transition: margin-left 0.32s cubic-bezier(0.4, 0, 0.2, 1);
    background: transparent;
}

.topbar {
    height: var(--topbar-h);
    background: rgba(12, 1, 32, 0.82);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-subtle);
    display: flex;
    align-items: center;
    padding: 0 24px;
    gap: 16px;
    position: sticky;
    top: 0;
    z-index: 200;
    box-shadow: 0 4px 25px rgba(88, 28, 135, 0.15);
}

.menu-btn {
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5px;
    width: 44px;
    height: 44px;
    background: rgba(168, 85, 247, 0.12);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: var(--ease-smooth);
    flex-shrink: 0;
}
.menu-btn:hover {
    background: rgba(168, 85, 247, 0.25);
}

.menu-btn span {
    display: block;
    width: 20px;
    height: 2px;
    background: var(--purple-soft);
    border-radius: 2px;
    transition: transform 0.25s ease, opacity 0.25s ease;
}

/* Animated Hamburger to Cross */
.menu-btn.open span:nth-child(1) {
    transform: translateY(7px) rotate(45deg);
}
.menu-btn.open span:nth-child(2) {
    opacity: 0;
}
.menu-btn.open span:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
}

.topbar-title {
    font-size: 17px;
    font-weight: 700;
    color: var(--text-primary);
    flex: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.topbar-right {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-shrink: 0;
}

.topbar-chip {
    display: flex;
    align-items: center;
    gap: 7px;
    background: rgba(38, 8, 82, 0.65);
    border: 1px solid var(--border-subtle);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    color: var(--text-secondary);
    font-weight: 600;
}

.chip-dot {
    width: 7px;
    height: 7px;
    background: var(--purple-neon);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--purple-neon);
    animation: purplePulse 2s infinite;
}

@keyframes purplePulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(0.85); }
}

.page-content {
    flex: 1;
    padding: 28px;
    max-width: 1440px;
    margin: 0 auto;
    width: 100%;
}

/* -- Flash Notifications ----------------------------------- */
.flash-container {
    padding: 16px 28px 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.flash {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 18px;
    border-radius: var(--radius-sm);
    font-size: 14px;
    gap: 12px;
    background: rgba(38, 8, 82, 0.85);
    border: 1px solid var(--border-glow);
    color: var(--purple-pale);
    box-shadow: var(--glow-shadow);
    animation: slideDownIn 0.3s ease;
}

@keyframes slideDownIn {
    from { transform: translateY(-10px); opacity: 0; }
    to   { transform: translateY(0); opacity: 1; }
}

.flash-close {
    background: none;
    border: none;
    color: var(--purple-neon);
    font-size: 16px;
    cursor: pointer;
    padding: 2px 6px;
    transition: var(--ease-smooth);
}
.flash-close:hover {
    color: #ffffff;
}

/* ============================================================
   BUTTONS (PURPLE SPECTRUM)
   ============================================================ */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 11px 20px;
    border-radius: var(--radius-sm);
    font-size: 14px;
    font-weight: 600;
    border: none;
    transition: var(--ease-smooth);
    white-space: nowrap;
    cursor: pointer;
    text-decoration: none;
    min-height: 44px;
    position: relative;
    user-select: none;
}

.btn:active {
    transform: scale(0.98);
}

.btn-primary {
    background: linear-gradient(135deg, var(--purple-royal) 0%, var(--purple-vivid) 50%, var(--purple-bright) 100%);
    color: #ffffff;
    box-shadow: 0 4px 20px rgba(147, 51, 234, 0.38);
    border: 1px solid rgba(192, 132, 252, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--glow-intense);
    filter: brightness(1.1);
}

.btn-outline {
    background: rgba(147, 51, 234, 0.10);
    color: var(--purple-pale);
    border: 1.5px solid var(--purple-bright);
}

.btn-outline:hover {
    background: rgba(147, 51, 234, 0.22);
    border-color: var(--purple-neon);
    transform: translateY(-1px);
    box-shadow: var(--glow-shadow);
}

.btn-ghost {
    background: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border-subtle);
}

.btn-ghost:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-glow);
}

.btn-danger {
    background: rgba(88, 28, 135, 0.4);
    color: var(--purple-pale);
    border: 1px solid rgba(168, 85, 247, 0.35);
}
.btn-danger:hover {
    background: rgba(124, 58, 237, 0.45);
    border-color: var(--purple-bright);
}

.btn-lg {
    padding: 13px 26px;
    font-size: 15px;
    min-height: 48px;
}

.btn-sm {
    padding: 6px 13px;
    font-size: 12px;
    min-height: 34px;
}

.w-full {
    width: 100%;
}

/* ============================================================
   GLASSMORPHIC CARDS & FORMS
   ============================================================ */
.form-card {
    background: var(--bg-card);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 24px;
    margin-bottom: 20px;
    transition: var(--ease-smooth);
}

.form-card:hover {
    border-color: var(--border-glow);
    box-shadow: 0 8px 30px rgba(124, 58, 237, 0.12);
}

.form-card-header {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 22px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-subtle);
}

.form-card-icon {
    font-size: 22px;
    width: 44px;
    height: 44px;
    background: rgba(147, 51, 234, 0.18);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.form-card-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
}

.form-card-sub {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 3px;
}

.form-grid {
    display: grid;
    gap: 16px;
}
.form-grid-2 { grid-template-columns: repeat(2, 1fr); }
.form-grid-3 { grid-template-columns: repeat(3, 1fr); }
.form-grid-4 { grid-template-columns: repeat(4, 1fr); }

.form-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.form-group label {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-secondary);
    letter-spacing: 0.3px;
}

.required {
    color: var(--purple-neon);
}

.form-input, .form-select, .form-textarea {
    background: var(--bg-input);
    border: 1.5px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    color: var(--text-primary);
    padding: 12px 14px;
    font-size: 15px;
    transition: var(--ease-smooth);
    width: 100%;
    outline: none;
    min-height: 46px;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
    border-color: var(--border-focus);
    background: var(--bg-input-focus);
    box-shadow: 0 0 0 3px rgba(192, 132, 252, 0.22);
}

.form-input::placeholder, .form-textarea::placeholder {
    color: var(--text-dim);
}

.form-textarea {
    resize: vertical;
    min-height: 95px;
}

.form-select {
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23c084fc' stroke-width='1.8' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 14px center;
    padding-right: 38px;
    cursor: pointer;
}

.form-hint {
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 4px;
}
.form-hint a {
    color: var(--purple-neon);
}

.dynamic-row {
    background: rgba(18, 2, 45, 0.55);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 16px;
    margin-bottom: 14px;
    position: relative;
}

.btn-remove {
    background: rgba(88, 28, 135, 0.35);
    border: 1px solid var(--border-subtle);
    color: var(--purple-soft);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 6px;
    margin-top: 10px;
    cursor: pointer;
    transition: var(--ease-smooth);
}
.btn-remove:hover {
    background: rgba(147, 51, 234, 0.35);
    color: #ffffff;
    border-color: var(--purple-bright);
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 12px;
    padding-bottom: 20px;
    flex-wrap: wrap;
}

/* ============================================================
   DASHBOARD HERO & STATS
   ============================================================ */
.dashboard-hero {
    background: linear-gradient(135deg, rgba(30, 8, 68, 0.85) 0%, rgba(68, 15, 140, 0.25) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-lg);
    padding: 44px;
    margin-bottom: 26px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 10px 40px rgba(88, 28, 135, 0.20);
}

.dashboard-hero::before {
    content: '';
    position: absolute;
    top: -90px;
    right: -90px;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(192, 132, 252, 0.2) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(168, 85, 247, 0.16);
    border: 1px solid var(--border-glow);
    color: var(--purple-neon);
    font-size: 12px;
    font-weight: 700;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 16px;
    letter-spacing: 0.5px;
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 36px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #ffffff 0%, #e9d5ff 50%, var(--purple-neon) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 15px;
    color: var(--text-secondary);
    margin-bottom: 26px;
    max-width: 480px;
    line-height: 1.6;
}

.hero-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.hero-illustration {
    flex-shrink: 0;
}

.hero-score-card {
    background: rgba(45, 12, 95, 0.75);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-md);
    padding: 24px;
    text-align: center;
    min-width: 175px;
    box-shadow: var(--glow-shadow);
}

.score-ring-demo {
    position: relative;
    display: inline-block;
}

.score-ring-label {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    font-family: 'Outfit', sans-serif;
}

.score-card-label {
    font-size: 12px;
    color: var(--text-secondary);
    margin-top: 8px;
    font-weight: 600;
}

/* Stats Row */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 28px;
}

.stat-card {
    background: var(--bg-card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: var(--ease-smooth);
}

.stat-card:hover {
    border-color: var(--border-glow);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(124, 58, 237, 0.16);
}

.stat-icon {
    width: 46px;
    height: 46px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
    border: 1px solid var(--border-subtle);
}

/* Stat Icons: All Cohesive Violet / Purple Variations */
.stat-icon-purple {
    background: rgba(168, 85, 247, 0.18);
    color: var(--purple-neon);
}
.stat-icon-blue {
    background: rgba(147, 51, 234, 0.22);
    color: var(--purple-soft);
}
.stat-icon-green {
    background: rgba(192, 132, 252, 0.20);
    color: var(--purple-pale);
}
.stat-icon-amber {
    background: rgba(124, 58, 237, 0.24);
    color: var(--purple-bright);
}
.stat-icon-red {
    background: rgba(88, 28, 135, 0.35);
    color: var(--purple-soft);
}

.stat-value {
    font-size: 28px;
    font-weight: 800;
    color: var(--text-primary);
    font-family: 'Outfit', sans-serif;
    line-height: 1;
}

.stat-label {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 4px;
}

/* Section Header */
.section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 10px;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-primary);
    font-family: 'Outfit', sans-serif;
}

.section-sub {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 3px;
}

/* Feature Grid */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 30px;
}

.feature-card {
    background: var(--bg-card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 24px;
    transition: var(--ease-smooth);
    position: relative;
    overflow: hidden;
    display: block;
}

.feature-card:hover {
    transform: translateY(-3px);
    border-color: var(--purple-neon);
    box-shadow: var(--glow-shadow);
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3.5px;
    border-radius: var(--radius-md) var(--radius-md) 0 0;
    background: linear-gradient(90deg, var(--purple-royal), var(--purple-bright), var(--purple-neon));
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 12px;
}

.feature-card h3 {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 8px;
    color: var(--text-primary);
}

.feature-card p {
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.5;
}

.feature-arrow {
    position: absolute;
    bottom: 16px;
    right: 18px;
    font-size: 16px;
    color: var(--purple-neon);
    opacity: 0;
    transition: var(--ease-smooth);
}

.feature-card:hover .feature-arrow {
    opacity: 1;
    transform: translateX(4px);
}

/* Resume List on Dashboard */
.resume-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.resume-list-item {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 14px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: var(--ease-smooth);
    flex-wrap: wrap;
}

.resume-list-item:hover {
    border-color: var(--border-glow);
}

.resume-avatar {
    width: 38px;
    height: 38px;
    background: linear-gradient(135deg, var(--purple-royal), var(--purple-bright));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 15px;
    color: #ffffff;
    flex-shrink: 0;
}

.resume-info {
    flex: 1;
    min-width: 0;
}

.resume-name {
    font-weight: 600;
    font-size: 14px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.resume-email {
    font-size: 12px;
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.resume-date {
    font-size: 12px;
    color: var(--text-dim);
}

.resume-actions {
    display: flex;
    gap: 8px;
    flex-shrink: 0;
}

/* ============================================================
   ATS ANALYZER & SCORE RING
   ============================================================ */
.ats-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    align-items: start;
}

.toggle-group {
    display: flex;
    background: var(--bg-input);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 4px;
    gap: 4px;
    margin-bottom: 20px;
}

.toggle-btn {
    flex: 1;
    padding: 10px;
    border-radius: 7px;
    border: none;
    background: transparent;
    color: var(--text-secondary);
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: var(--ease-smooth);
    min-height: 42px;
}

.toggle-btn.active {
    background: linear-gradient(135deg, var(--purple-royal), var(--purple-bright));
    color: #ffffff;
    box-shadow: 0 2px 12px rgba(147, 51, 234, 0.4);
}

.score-card-main {
    background: var(--bg-card);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-md);
    padding: 28px;
    text-align: center;
    margin-bottom: 16px;
    box-shadow: var(--glow-shadow);
}

.score-label {
    font-size: 13px;
    font-weight: 800;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 16px;
}

.score-ring-container {
    position: relative;
    display: inline-block;
}

.score-ring-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.score-number {
    font-family: 'Outfit', sans-serif;
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1;
}

.score-status {
    font-size: 12px;
    font-weight: 700;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.score-status.good { color: var(--purple-pale); }
.score-status.ok   { color: var(--purple-neon); }
.score-status.low  { color: var(--purple-bright); }

.score-meta {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 14px;
}

/* Tips & Skills */
.tips-card {
    background: rgba(124, 58, 237, 0.12);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-md);
    padding: 18px;
    margin-bottom: 16px;
}

.tips-title {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--purple-pale);
}

.tips-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.tips-list li {
    font-size: 13px;
    color: var(--text-secondary);
    padding-left: 16px;
    position: relative;
}

.tips-list li::before {
    content: '\2192';
    position: absolute;
    left: 0;
    color: var(--purple-neon);
}

.skills-section {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 18px;
    margin-bottom: 14px;
}

.skills-section-title {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 12px;
}

.skills-matched-title { color: var(--purple-pale); }
.skills-missing-title { color: var(--purple-neon); }

.skills-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.skill-badge {
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    transition: var(--ease-smooth);
}

.skill-matched {
    background: var(--status-1);
    color: var(--status-1-text);
    border: 1px solid var(--status-1-bord);
    box-shadow: 0 0 10px rgba(192, 132, 252, 0.25);
}

.skill-missing {
    background: var(--status-3);
    color: var(--status-3-text);
    border: 1px solid var(--status-3-bord);
}

.skill-neutral {
    background: rgba(38, 8, 82, 0.6);
    color: var(--text-secondary);
    border: 1px solid var(--border-subtle);
}

.skills-empty {
    font-size: 13px;
    color: var(--text-dim);
    font-style: italic;
}

/* Gap Analysis */
.gap-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 18px;
    margin-bottom: 14px;
}

.gap-title {
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 14px;
    color: var(--text-primary);
}

.gap-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.gap-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 11px 14px;
    background: rgba(18, 2, 45, 0.60);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    gap: 10px;
    flex-wrap: wrap;
}

.gap-item-info {
    display: flex;
    align-items: center;
    gap: 9px;
    flex-wrap: wrap;
}

.gap-skill {
    font-size: 13.5px;
    font-weight: 600;
}

.gap-category {
    font-size: 11px;
    color: var(--purple-soft);
    background: rgba(147, 51, 234, 0.25);
    padding: 2px 8px;
    border-radius: 10px;
}

/* Placeholder for ATS */
.ats-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 16px;
}

.ats-placeholder {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 44px 28px;
    text-align: center;
}

.placeholder-icon {
    font-size: 46px;
    margin-bottom: 14px;
}

.ats-placeholder h3 {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.ats-placeholder p {
    font-size: 14px;
    color: var(--text-secondary);
    max-width: 380px;
    margin: 0 auto;
}

.placeholder-steps {
    display: flex;
    flex-direction: column;
    gap: 9px;
    margin-top: 22px;
    text-align: left;
    max-width: 280px;
    margin-left: auto;
    margin-right: auto;
}

.p-step {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
    color: var(--text-secondary);
}

.p-step-num {
    width: 22px;
    height: 22px;
    background: var(--purple-royal);
    color: #ffffff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 700;
    flex-shrink: 0;
}

.alert {
    padding: 14px 18px;
    border-radius: var(--radius-sm);
    font-size: 14px;
    display: flex;
    gap: 10px;
    align-items: flex-start;
}

.alert-warning {
    background: rgba(124, 58, 237, 0.16);
    border: 1px solid var(--border-glow);
    color: var(--purple-pale);
}

/* ============================================================
   TEMPLATES SELECTOR & CARDS (ALL-PURPLE)
   ============================================================ */
.templates-layout {
    display: grid;
    grid-template-columns: 1fr 330px;
    gap: 22px;
    align-items: start;
}

.template-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}

.template-card {
    background: var(--bg-card);
    border: 2px solid var(--border-subtle);
    border-radius: var(--radius-md);
    overflow: hidden;
    cursor: pointer;
    transition: var(--ease-smooth);
    position: relative;
}

.template-card:hover {
    border-color: var(--border-glow);
    transform: translateY(-2px);
}

.template-card.active {
    border-color: var(--purple-neon);
    box-shadow: var(--glow-shadow);
}

.template-preview {
    height: 165px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.modern-preview  { background: linear-gradient(135deg, #18003a, #2a0058); }
.classic-preview { background: linear-gradient(135deg, #12002e, #1f0045); }
.minimal-preview { background: linear-gradient(135deg, #1a0042, #0d0024); }

.tpl-header-bar   { height: 26px; background: linear-gradient(90deg, var(--purple-royal), var(--purple-bright)); border-radius: 4px; margin-bottom: 6px; }
.tpl-name-block   { height: 11px; background: rgba(255, 255, 255, 0.2); border-radius: 3px; width: 70%; }
.tpl-line         { height: 6px;  background: rgba(255, 255, 255, 0.1); border-radius: 2px; }
.tpl-line-wide    { width: 90%; }
.tpl-line-medium  { width: 60%; }
.tpl-divider      { height: 1px; background: rgba(168, 85, 247, 0.45); margin: 4px 0; }
.tpl-classic-header { height: 18px; background: rgba(124, 58, 237, 0.7); border-radius: 3px; margin-bottom: 6px; }
.tpl-classic-rule   { height: 1px; background: rgba(255, 255, 255, 0.2); margin: 4px 0; }
.tpl-min-name     { height: 13px; background: rgba(255, 255, 255, 0.25); border-radius: 3px; width: 60%; }
.tpl-min-section  { height: 7px;  background: rgba(192, 132, 252, 0.55); border-radius: 2px; width: 40%; }

.template-card-info {
    padding: 14px;
}

.template-name {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 4px;
}

.template-desc {
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.4;
    margin-bottom: 8px;
}

.template-badge {
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 10px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.tpl-badge-modern  { background: rgba(168, 85, 247, 0.22); color: var(--purple-pale); }
.tpl-badge-classic { background: rgba(124, 58, 237, 0.25); color: var(--purple-soft); }
.tpl-badge-minimal { background: rgba(147, 51, 234, 0.22); color: var(--purple-neon); }

.template-check {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 22px;
    height: 22px;
    background: var(--purple-bright);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: var(--ease-smooth);
    box-shadow: 0 0 10px var(--purple-bright);
}
.template-check::after {
    content: '\2713';
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
}
.template-check.visible {
    opacity: 1;
}

.selected-template-display {
    background: var(--bg-input);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 14px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 8px;
}

.std-label {
    font-size: 12px;
    color: var(--text-secondary);
    font-weight: 600;
}

.std-name {
    font-size: 15px;
    font-weight: 700;
    color: var(--purple-neon);
}

.download-tips {
    margin-top: 20px;
    padding: 16px;
    background: var(--bg-input);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-subtle);
}

.download-tips h4 {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--purple-pale);
}

.download-tips ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.download-tips li {
    font-size: 12px;
    color: var(--text-secondary);
    padding-left: 14px;
    position: relative;
}
.download-tips li::before {
    content: '\2192';
    position: absolute;
    left: 0;
    color: var(--purple-neon);
}

/* ============================================================
   INTERVIEW PREP
   ============================================================ */
.interview-layout {
    display: grid;
    grid-template-columns: 360px 1fr;
    gap: 24px;
    align-items: start;
}

.interview-tips-box {
    margin-top: 18px;
    background: var(--bg-input);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 16px;
}

.interview-tips-box h4 {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--purple-pale);
}

.interview-tips-box ol {
    padding-left: 18px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.interview-tips-box li {
    font-size: 13px;
    color: var(--text-secondary);
}

.questions-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 12px;
}

.questions-count-chips {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.count-chip {
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}

.chip-hr {
    background: var(--status-1);
    color: var(--status-1-text);
    border: 1px solid var(--status-1-bord);
}
.chip-tech {
    background: var(--status-2);
    color: var(--status-2-text);
    border: 1px solid var(--status-2-bord);
}
.chip-sit {
    background: var(--status-3);
    color: var(--status-3-text);
    border: 1px solid var(--status-3-bord);
}

.role-hints {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: var(--text-secondary);
    flex-wrap: wrap;
}

.role-tag {
    background: rgba(147, 51, 234, 0.22);
    padding: 3px 10px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 600;
    color: var(--purple-pale);
}

.q-section {
    margin-bottom: 24px;
}

.q-section-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border-subtle);
    flex-wrap: wrap;
}

.q-section-icon {
    font-size: 18px;
}

.q-count {
    background: rgba(147, 51, 234, 0.25);
    color: var(--purple-pale);
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 10px;
    margin-left: auto;
}

.q-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.q-item {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    overflow: hidden;
    cursor: pointer;
    transition: var(--ease-smooth);
}

.q-item:hover {
    border-color: var(--border-glow);
}

.q-item.open {
    border-color: var(--purple-neon);
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.2);
}

.q-header {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 14px;
}

.q-skill-tag {
    background: rgba(124, 58, 237, 0.24);
    border: 1px solid var(--border-subtle);
    border-radius: 6px;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 700;
    color: var(--purple-neon);
    white-space: nowrap;
    flex-shrink: 0;
}

.q-text {
    flex: 1;
    font-size: 14px;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.4;
}

.q-toggle {
    color: var(--purple-soft);
    font-size: 11px;
    flex-shrink: 0;
    margin-top: 2px;
}

.q-answer {
    display: none;
    padding: 14px 14px 14px 34px;
    background: rgba(18, 2, 45, 0.65);
    border-top: 1px solid var(--border-subtle);
}

.q-item.open .q-answer {
    display: block;
}

.q-answer-label {
    font-size: 11px;
    font-weight: 700;
    color: var(--purple-neon);
    margin-bottom: 7px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.q-answer p {
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.6;
}

.interview-actions {
    display: flex;
    gap: 10px;
    margin-top: 12px;
    flex-wrap: wrap;
}

/* ============================================================
   JOB APPLICATION TRACKER
   ============================================================ */
.tracker-layout {
    display: grid;
    grid-template-columns: 330px 1fr;
    gap: 22px;
    align-items: start;
}

.tracker-filters {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
}

.tracker-table-wrapper {
    overflow-x: auto;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-subtle);
    background: var(--bg-card);
    -webkit-overflow-scrolling: touch;
}

.tracker-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    min-width: 620px;
}

.tracker-table th {
    background: rgba(30, 8, 70, 0.7);
    color: var(--text-secondary);
    font-size: 11.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 13px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border-subtle);
    white-space: nowrap;
}

.tracker-table td {
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-subtle);
    vertical-align: middle;
}

.tracker-table tr:last-child td {
    border-bottom: none;
}

.tracker-table tbody tr {
    background: transparent;
    transition: var(--ease-smooth);
}

.tracker-table tbody tr:hover {
    background: rgba(147, 51, 234, 0.12);
}

.app-company {
    display: flex;
    align-items: center;
    gap: 10px;
}

.company-avatar {
    width: 34px;
    height: 34px;
    background: linear-gradient(135deg, var(--purple-royal), var(--purple-bright));
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    color: #ffffff;
    flex-shrink: 0;
}

.company-name {
    font-weight: 600;
    font-size: 14px;
}

.job-link {
    font-size: 11px;
    color: var(--purple-neon);
    display: block;
}

.app-role {
    font-weight: 500;
}

.app-notes {
    font-size: 12px;
    color: var(--text-secondary);
    max-width: 180px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.app-actions {
    display: flex;
    gap: 6px;
    white-space: nowrap;
}

/* Status Badges: Purple Cohesive */
.status-badge {
    padding: 4px 11px;
    border-radius: 20px;
    font-size: 11.5px;
    font-weight: 700;
    white-space: nowrap;
}

.status-applied {
    background: var(--status-3);
    color: var(--status-3-text);
    border: 1px solid var(--status-3-bord);
}
.status-interview {
    background: var(--status-2);
    color: var(--status-2-text);
    border: 1px solid var(--status-2-bord);
    box-shadow: 0 0 10px rgba(192, 132, 252, 0.3);
}
.status-offer {
    background: var(--status-1);
    color: var(--status-1-text);
    border: 1px solid var(--status-1-bord);
    box-shadow: 0 0 12px rgba(216, 180, 254, 0.4);
}
.status-rejected {
    background: var(--status-4);
    color: var(--status-4-text);
    border: 1px solid var(--status-4-bord);
}
.status-withdrawn {
    background: rgba(38, 8, 82, 0.6);
    color: var(--text-muted);
    border: 1px solid var(--border-subtle);
}

/* -- Modal Popup ------------------------------------------- */
.modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(6, 0, 18, 0.82);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    z-index: 500;
    align-items: center;
    justify-content: center;
    padding: 16px;
}

.modal-overlay.open {
    display: flex;
}

.modal {
    background: rgba(22, 5, 54, 0.95);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-lg);
    width: 100%;
    max-width: 580px;
    max-height: 92vh;
    overflow-y: auto;
    padding: 26px;
    animation: modalScaleIn 0.22s ease;
    box-shadow: 0 10px 45px rgba(124, 58, 237, 0.35);
}

@keyframes modalScaleIn {
    from { transform: scale(0.94) translateY(-14px); opacity: 0; }
    to   { transform: scale(1) translateY(0); opacity: 1; }
}

.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 22px;
}

.modal-header h3 {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
}

.modal-close {
    background: rgba(147, 51, 234, 0.18);
    border: 1px solid var(--border-subtle);
    color: var(--purple-soft);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 14px;
    transition: var(--ease-smooth);
}
.modal-close:hover {
    background: rgba(192, 132, 252, 0.35);
    color: #ffffff;
}

.modal-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
}

/* ============================================================
   RESUME VIEW & PRINT
   ============================================================ */
.resume-view-header {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 10px;
}

.resume-view-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.resume-preview-card {
    background: var(--bg-card);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-lg);
    padding: 40px;
    max-width: 860px;
    margin: 0 auto;
    box-shadow: 0 10px 40px rgba(88, 28, 135, 0.18);
}

.rp-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 26px;
    padding-bottom: 22px;
    border-bottom: 2px solid var(--purple-bright);
    flex-wrap: wrap;
}

.rp-avatar {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, var(--purple-royal), var(--purple-bright));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    flex-shrink: 0;
    box-shadow: 0 0 16px rgba(168, 85, 247, 0.5);
}

.rp-name {
    font-family: 'Outfit', sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 6px;
}

.rp-contacts {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 13px;
    color: var(--text-secondary);
}
.rp-contacts a {
    color: var(--purple-neon);
}

.rp-section {
    margin-bottom: 24px;
}

.rp-section-title {
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.6px;
    color: var(--purple-neon);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-subtle);
}

.rp-summary {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.7;
}

.rp-exp-item { margin-bottom: 16px; }
.rp-exp-role { font-size: 15px; font-weight: 700; color: var(--text-primary); }
.rp-exp-meta { font-size: 13px; color: var(--text-secondary); margin-top: 2px; }
.rp-exp-desc { display: flex; flex-direction: column; gap: 4px; margin-top: 6px; }
.rp-bullet   { font-size: 13px; color: var(--text-secondary); padding-left: 14px; position: relative; }
.rp-bullet::before { content: '\2192'; position: absolute; left: 0; color: var(--purple-bright); }
.rp-edu-item   { margin-bottom: 10px; }
.rp-edu-degree { font-size: 14px; font-weight: 700; color: var(--text-primary); }
.rp-edu-meta   { font-size: 13px; color: var(--text-secondary); }

/* ============================================================
   UPLOAD PAGE
   ============================================================ */
.upload-dropzone {
    border: 2px dashed rgba(168, 85, 247, 0.4);
    border-radius: var(--radius-md);
    padding: 46px 28px;
    text-align: center;
    cursor: pointer;
    transition: var(--ease-smooth);
    background: rgba(18, 2, 45, 0.4);
}

.upload-dropzone:hover, .upload-dropzone.dragover {
    border-color: var(--purple-neon);
    background: rgba(147, 51, 234, 0.15);
    box-shadow: var(--glow-shadow);
}

.dropzone-icon {
    font-size: 46px;
    margin-bottom: 12px;
}

.dropzone-text {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 6px;
}

.dropzone-sub {
    font-size: 13px;
    color: var(--text-secondary);
}

.dropzone-filename {
    display: none;
    margin-top: 14px;
    padding: 8px 16px;
    background: rgba(147, 51, 234, 0.25);
    border-radius: 8px;
    font-size: 13px;
    color: var(--purple-pale);
    font-weight: 600;
}

.upload-result {
    margin-top: 24px;
    padding: 20px;
    background: var(--bg-card);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-subtle);
}

.upload-text-box {
    background: var(--bg-darkest);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 14px;
    font-size: 13px;
    color: var(--text-secondary);
    white-space: pre-wrap;
    max-height: 280px;
    overflow-y: auto;
    font-family: monospace;
}

.upload-note {
    margin-top: 20px;
    padding: 12px 16px;
    background: rgba(124, 58, 237, 0.16);
    border: 1px solid var(--border-glow);
    border-radius: var(--radius-sm);
    font-size: 12px;
    color: var(--purple-pale);
    line-height: 1.5;
}

/* ============================================================
   RESPONSIVE OPTIMIZATION ACROSS ALL DEVICES
   ============================================================ */

/* -- 1. Large Monitors & 4K Displays (- 1441px) ------------ */
@media (min-width: 1441px) {
    .page-content {
        padding: 36px 40px;
    }
    .dashboard-hero {
        padding: 50px;
    }
    .hero-title {
        font-size: 42px;
    }
}

/* -- 2. Medium Laptops & Desktops (1025px - 1440px) --------- */
@media (max-width: 1440px) and (min-width: 1025px) {
    .dashboard-hero {
        padding: 36px;
    }
    .hero-title {
        font-size: 32px;
    }
}

/* -- 3. Tablets & Small Laptops (769px - 1024px) ------------ */
@media (max-width: 1024px) {
    :root {
        --sidebar-w: 240px;
        --topbar-h: 58px;
    }

    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
    }

    .feature-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .ats-layout,
    .templates-layout,
    .interview-layout,
    .tracker-layout {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .template-cards {
        grid-template-columns: repeat(3, 1fr);
    }

    .dashboard-hero {
        padding: 32px;
        gap: 20px;
    }
    .hero-title {
        font-size: 28px;
    }
}

/* -- 4. Mobile Devices & Small Tablets (- 768px) ------------ */
@media (max-width: 768px) {
    :root {
        --topbar-h: 56px;
        font-size: 15px;
    }

    /* Off-screen Drawer */
    .sidebar {
        transform: translateX(-100%);
        width: 280px;
        box-shadow: 10px 0 40px rgba(5, 0, 16, 0.8);
    }
    .sidebar.open {
        transform: translateX(0);
    }
    .sidebar-overlay.open {
        display: block;
    }
    .sidebar-close-btn {
        display: flex;
    }

    .main-wrapper {
        margin-left: 0;
    }

    .menu-btn {
        display: flex;
    }

    .topbar {
        padding: 0 16px;
    }

    .page-content {
        padding: 16px;
    }

    .flash-container {
        padding: 12px 16px 0;
    }

    /* Grids to single or compact 2-column */
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    .stat-card {
        padding: 14px 12px;
        gap: 12px;
    }
    .stat-value {
        font-size: 22px;
    }
    .stat-icon {
        width: 38px;
        height: 38px;
        font-size: 18px;
    }

    .feature-grid {
        grid-template-columns: 1fr;
    }

    .form-grid-2, .form-grid-3, .form-grid-4 {
        grid-template-columns: 1fr;
        gap: 12px;
    }

    /* Hero Section on Mobile */
    .dashboard-hero {
        flex-direction: column;
        padding: 24px 18px;
        gap: 18px;
        border-radius: var(--radius-md);
    }
    .hero-illustration {
        display: none;
    }
    .hero-title {
        font-size: 24px;
        line-height: 1.25;
    }
    .hero-subtitle {
        font-size: 14px;
        margin-bottom: 20px;
    }
    .hero-actions {
        width: 100%;
        flex-direction: column;
    }
    .hero-actions .btn {
        width: 100%;
    }

    /* Buttons stack gracefully on mobile */
    .form-actions {
        flex-direction: column;
    }
    .form-actions .btn {
        width: 100%;
    }

    .ats-actions {
        flex-direction: column;
    }
    .ats-actions .btn {
        width: 100%;
    }

    .resume-view-actions {
        width: 100%;
    }
    .resume-view-actions .btn {
        flex: 1;
    }

    .modal-actions {
        flex-direction: column;
    }
    .modal-actions .btn {
        width: 100%;
    }

    /* Form Card & Inputs on Mobile: Prevent iOS zoom */
    .form-card {
        padding: 18px 16px;
    }
    .form-input, .form-select, .form-textarea {
        font-size: 16px !important; /* Critical to disable iOS auto-zoom */
        min-height: 48px;
    }

    /* Templates Cards */
    .template-cards {
        grid-template-columns: 1fr;
    }

    /* Tracker filters */
    .tracker-filters {
        flex-direction: column;
    }

    /* Resume Preview Card */
    .resume-preview-card {
        padding: 20px 16px;
    }
    .rp-name {
        font-size: 24px;
    }
    .rp-avatar {
        width: 52px;
        height: 52px;
        font-size: 22px;
    }

    /* Score Ring on Mobile */
    .score-card-main {
        padding: 20px 14px;
    }
    .score-ring {
        width: 135px;
        height: 135px;
    }
    .score-number {
        font-size: 28px;
    }

    /* Modal responsiveness */
    .modal {
        padding: 20px 16px;
        max-height: 94vh;
    }
}

/* -- 5. Small Handheld Phones (- 420px) ---------------------- */
@media (max-width: 420px) {
    .topbar-chip {
        display: none;
    }

    .topbar-title {
        font-size: 15px;
    }

    .hero-title {
        font-size: 21px;
    }

    .stat-card {
        padding: 12px 10px;
    }
    .stat-value {
        font-size: 20px;
    }
    .stat-label {
        font-size: 11px;
    }

    .q-header {
        padding: 12px 10px;
    }
    .q-text {
        font-size: 13px;
    }

    .resume-list-item {
        padding: 12px;
    }
    .resume-actions {
        width: 100%;
        justify-content: flex-end;
    }
}

/* -- Touch Optimization for Touchscreens -------------------- */
@media (hover: none) and (pointer: coarse) {
    .nav-item {
        min-height: 48px;
    }
    .btn {
        min-height: 48px;
        touch-action: manipulation;
    }
    .btn-sm {
        min-height: 38px;
    }
    .toggle-btn {
        min-height: 44px;
    }

    /* Disable hover transforms on touch to prevent sticky hover bug */
    .stat-card:hover,
    .feature-card:hover,
    .template-card:hover,
    .resume-list-item:hover {
        transform: none !important;
    }
}

/* -- Print Styles ------------------------------------------- */
@media print {
    .sidebar, .topbar, .flash-container, .form-actions,
    .btn, .ats-actions, .interview-actions, .menu-btn {
        display: none !important;
    }
    .main-wrapper {
        margin-left: 0 !important;
    }
    body::before, body::after {
        display: none !important;
    }
    body {
        background: #ffffff !important;
        color: #000000 !important;
    }
}
""",
    'static/js/main.js': r"""
// === Mobile Responsive Sidebar Toggle =========================================
function toggleSidebar(forceState) {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const menuBtn = document.getElementById('menuBtn');
    
    const shouldOpen = (typeof forceState === 'boolean') ? forceState : !sidebar.classList.contains('open');
    
    if (shouldOpen) {
        sidebar.classList.add('open');
        overlay.classList.add('open');
        if (menuBtn) menuBtn.classList.add('open');
        document.body.style.overflow = window.innerWidth <= 768 ? 'hidden' : '';
    } else {
        sidebar.classList.remove('open');
        overlay.classList.remove('open');
        if (menuBtn) menuBtn.classList.remove('open');
        document.body.style.overflow = '';
    }
}

// Close sidebar when clicking any navigation link on small screens
document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.sidebar .nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                toggleSidebar(false);
            }
        });
    });

    // Handle Escape key to close mobile menu or open modals
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            toggleSidebar(false);
            const openModal = document.querySelector('.modal-overlay.open');
            if (openModal) openModal.classList.remove('open');
        }
    });

    // Auto-dismiss flash notifications after 5 seconds
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(f => {
        setTimeout(() => {
            f.style.opacity = '0';
            f.style.transform = 'translateY(-8px)';
            f.style.transition = 'all 0.3s ease';
            setTimeout(() => f.remove(), 300);
        }, 5000);
    });

    // Smooth count-up animation for stat numbers
    document.querySelectorAll('.stat-value').forEach(el => {
        const target = parseInt(el.textContent.trim());
        if (!isNaN(target) && target > 0) {
            animateCount(el, 0, target, 800);
        }
    });
});

function animateCount(el, start, end, duration) {
    const startTime = performance.now();
    const update = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(start + (end - start) * eased);
        if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
}

// === Interactive Purple Ripple Effect on Buttons ===============================
document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-primary, .btn-outline, .btn-ghost');
    if (!btn) return;

    const ripple = document.createElement('span');
    const rect = btn.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);

    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        border-radius: 50%;
        background: rgba(232, 121, 249, 0.35);
        top: ${e.clientY - rect.top - size / 2}px;
        left: ${e.clientX - rect.left - size / 2}px;
        transform: scale(0);
        animation: purpleRipple 0.55s ease-out;
        pointer-events: none;
    `;

    if (!document.getElementById('purpleRippleStyle')) {
        const style = document.createElement('style');
        style.id = 'purpleRippleStyle';
        style.textContent = '@keyframes purpleRipple { to { transform: scale(2.6); opacity: 0; } }';
        document.head.appendChild(style);
    }

    btn.style.position = 'relative';
    btn.style.overflow = 'hidden';
    btn.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
});

// === Responsive Loading State for Form Submissions ============================
document.addEventListener('submit', (e) => {
    const btn = e.target.querySelector('button[type="submit"]');
    if (btn) {
        const originalText = btn.innerHTML;
        btn.innerHTML = `
            <span style="display:inline-flex;align-items:center;gap:8px">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="animation:spin 1s linear infinite">
                    <circle cx="12" cy="12" r="10" stroke="#c084fc" opacity="0.25"/>
                    <path d="M12 2a10 10 0 0 1 10 10" stroke="#f3e8ff"/>
                </svg>
                Processing...
            </span>
        `;
        btn.disabled = true;

        if (!document.getElementById('spinStyle')) {
            const style = document.createElement('style');
            style.id = 'spinStyle';
            style.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
            document.head.appendChild(style);
        }

        // Safety failsafe: re-enable button after 10s if network stalls
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }, 10000);
    }
});
""",
    'static/js/resume_builder.js': r"""
// === Resume Builder - Dynamic Form Functions ==================================

function addEducation() {
    const list = document.getElementById('educationList');
    const row = document.createElement('div');
    row.className = 'dynamic-row';
    row.setAttribute('data-row', 'education');
    row.innerHTML = `
        <div class="form-grid form-grid-4">
            <div class="form-group">
                <label>Degree / Course</label>
                <input type="text" name="edu_degree" class="form-input" placeholder="MCA / B.Sc. CS">
            </div>
            <div class="form-group">
                <label>Institution</label>
                <input type="text" name="edu_institution" class="form-input" placeholder="University Name">
            </div>
            <div class="form-group">
                <label>Year</label>
                <input type="text" name="edu_year" class="form-input" placeholder="2022 - 2024">
            </div>
            <div class="form-group">
                <label>Grade / CGPA</label>
                <input type="text" name="edu_grade" class="form-input" placeholder="8.5 CGPA">
            </div>
        </div>
        <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
    `;
    list.appendChild(row);
    row.querySelector('input').focus();
    row.style.animation = 'slideIn 0.3s ease';
}

function addExperience() {
    const list = document.getElementById('experienceList');
    const row = document.createElement('div');
    row.className = 'dynamic-row';
    row.setAttribute('data-row', 'experience');
    row.innerHTML = `
        <div class="form-grid form-grid-3">
            <div class="form-group">
                <label>Job Title / Role</label>
                <input type="text" name="exp_role" class="form-input" placeholder="Software Tester">
            </div>
            <div class="form-group">
                <label>Company</label>
                <input type="text" name="exp_company" class="form-input" placeholder="Company Name">
            </div>
            <div class="form-group">
                <label>Duration</label>
                <input type="text" name="exp_duration" class="form-input" placeholder="Jun 2023 - Present">
            </div>
        </div>
        <div class="form-group">
            <label>Responsibilities & Achievements</label>
            <textarea name="exp_description" class="form-textarea" rows="3"
                placeholder="- Describe your responsibilities and achievements (one per line)..."></textarea>
        </div>
        <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
    `;
    list.appendChild(row);
    row.querySelector('input').focus();
}

function addProject() {
    const list = document.getElementById('projectList');
    const row = document.createElement('div');
    row.className = 'dynamic-row';
    row.setAttribute('data-row', 'project');
    row.innerHTML = `
        <div class="form-grid form-grid-2">
            <div class="form-group">
                <label>Project Title</label>
                <input type="text" name="proj_title" class="form-input" placeholder="ATS Resume Builder">
            </div>
            <div class="form-group">
                <label>Technologies Used</label>
                <input type="text" name="proj_tech" class="form-input" placeholder="Python, Flask, SQLite">
            </div>
        </div>
        <div class="form-group">
            <label>Description</label>
            <textarea name="proj_description" class="form-textarea" rows="2"
                placeholder="Brief description of the project and your contribution..."></textarea>
        </div>
        <button type="button" class="btn-remove" onclick="removeRow(this)">&times; Remove</button>
    `;
    list.appendChild(row);
    row.querySelector('input').focus();
}

function removeRow(btn) {
    const row = btn.closest('.dynamic-row');
    row.style.opacity = '0';
    row.style.transform = 'translateY(-8px)';
    row.style.transition = 'all 0.2s ease';
    setTimeout(() => row.remove(), 200);
}

// === Form validation ==========================================================
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resumeForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        const name = form.querySelector('#full_name').value.trim();
        const email = form.querySelector('#email').value.trim();
        if (!name || !email) {
            e.preventDefault();
            alert('Please fill in at least your Full Name and Email Address.');
        }
    });
});
""",
    'static/js/tracker.js': r"""
// === Job Tracker JavaScript ===================================================

function filterTable() {
    const search = document.getElementById('filterSearch').value.toLowerCase();
    const status = document.getElementById('filterStatus').value;
    const rows = document.querySelectorAll('.app-row');

    rows.forEach(row => {
        const company = row.dataset.company || '';
        const role = row.dataset.role || '';
        const rowStatus = row.dataset.status || '';

        const matchSearch = !search || company.includes(search) || role.includes(search);
        const matchStatus = !status || rowStatus === status;

        row.style.display = matchSearch && matchStatus ? '' : 'none';
    });
}

function openEditModal(id, company, role, date, status, location, salary, jobUrl, notes) {
    document.getElementById('edit_company').value = company || '';
    document.getElementById('edit_role').value = role || '';
    document.getElementById('edit_date').value = date || '';
    document.getElementById('edit_status').value = status || 'Applied';
    document.getElementById('edit_location').value = location || '';
    document.getElementById('edit_salary').value = salary || '';
    document.getElementById('edit_job_url').value = jobUrl || '';
    document.getElementById('edit_notes').value = notes ? notes.replace(/`/g, '') : '';

    const form = document.getElementById('editForm');
    form.action = `/tracker/${id}/update`;

    document.getElementById('editModal').classList.add('open');
}

function closeEditModal() {
    document.getElementById('editModal').classList.remove('open');
}

// Close modal on overlay click
document.getElementById('editModal').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) closeEditModal();
});

// Set today as default date for new applications
document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById('date_applied');
    if (dateInput && !dateInput.value) {
        dateInput.value = new Date().toISOString().split('T')[0];
    }
});
""",
}

def extract_all():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    for rel_path, content in ASSETS.items():
        full_path = os.path.join(base_dir, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

