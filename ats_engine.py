"""
ATS Engine - Skill extraction, match scoring, gap analysis, interview Q generation.
All rule-based - no external API required.
"""

import re
import json
import os

# --- Load Skills Database (with Built-in Cloud Fallback) -------------------------

_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
_DB_PATH = os.path.join(_DATA_DIR, 'skills_db.json')

_DEFAULT_SKILLS = {
    "programming_languages": [
        "python", "java", "javascript", "typescript", "c", "c++", "c#", "ruby", "go", "rust",
        "kotlin", "swift", "php", "r", "scala", "perl", "dart", "lua", "haskell", "matlab",
        "vba", "cobol", "fortran", "assembly", "groovy", "julia", "elixir", "clojure"
    ],
    "web_frontend": [
        "html", "css", "html5", "css3", "react", "angular", "vue", "vue.js", "react.js",
        "next.js", "nuxt.js", "svelte", "jquery", "bootstrap", "tailwind", "tailwindcss",
        "sass", "scss", "less", "webpack", "vite", "babel", "redux", "mobx", "graphql",
        "typescript", "ajax", "rest api", "responsive design", "web design"
    ],
    "web_backend": [
        "flask", "django", "fastapi", "express", "express.js", "node.js", "spring", "spring boot",
        "laravel", "rails", "ruby on rails", "asp.net", ".net", "hibernate", "microservices",
        "rest", "restful api", "soap", "api development", "web services"
    ],
    "databases": [
        "sql", "mysql", "postgresql", "sqlite", "mongodb", "redis", "oracle", "microsoft sql server",
        "cassandra", "dynamodb", "firebase", "elasticsearch", "neo4j", "mariadb", "nosql",
        "database design", "data modeling", "stored procedures", "database administration"
    ],
    "cloud_devops": [
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "jenkins", "terraform",
        "ansible", "ci/cd", "devops", "linux", "unix", "bash", "shell scripting", "git",
        "github", "gitlab", "bitbucket", "nginx", "apache", "helm", "prometheus", "grafana",
        "cloudformation", "serverless", "lambda", "ec2", "s3", "rds"
    ],
    "data_science_ml": [
        "machine learning", "deep learning", "artificial intelligence", "ai", "ml", "nlp",
        "natural language processing", "computer vision", "tensorflow", "pytorch", "keras",
        "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", "tableau", "power bi",
        "data analysis", "data visualization", "statistics", "big data", "hadoop", "spark",
        "data mining", "neural networks", "regression", "classification", "clustering",
        "feature engineering", "model training", "opencv", "hugging face"
    ],
    "testing": [
        "manual testing", "automation testing", "selenium", "playwright", "cypress",
        "functional testing", "regression testing", "integration testing", "unit testing",
        "performance testing", "load testing", "api testing", "postman", "testng",
        "junit", "pytest", "jest", "mocha", "cucumber", "bdd", "tdd", "jmeter",
        "qa", "quality assurance", "test planning", "test cases", "bug reporting",
        "defect tracking", "appium", "mobile testing", "cross browser testing"
    ],
    "project_management": [
        "agile", "scrum", "kanban", "jira", "confluence", "trello", "asana",
        "project management", "product management", "sprint planning", "sdlc",
        "waterfall", "lean", "six sigma", "pmp", "risk management"
    ],
    "security": [
        "cybersecurity", "network security", "penetration testing", "ethical hacking",
        "owasp", "encryption", "ssl", "tls", "vpn", "firewall", "siem", "vulnerability assessment",
        "information security", "identity management", "sso", "oauth", "jwt"
    ],
    "mobile": [
        "android", "ios", "react native", "flutter", "xamarin", "swift", "kotlin",
        "mobile development", "android studio", "xcode"
    ],
    "soft_skills": [
        "communication", "leadership", "teamwork", "problem solving", "critical thinking",
        "time management", "adaptability", "creativity", "collaboration", "analytical",
        "attention to detail", "multitasking", "presentation", "negotiation"
    ],
    "learning_resources": {
        "python": "https://www.w3schools.com/python/",
        "java": "https://www.w3schools.com/java/",
        "javascript": "https://javascript.info/",
        "react": "https://react.dev/learn",
        "sql": "https://www.w3schools.com/sql/",
        "mysql": "https://www.mysqltutorial.org/",
        "docker": "https://docs.docker.com/get-started/",
        "aws": "https://aws.amazon.com/training/",
        "machine learning": "https://www.coursera.org/learn/machine-learning",
        "selenium": "https://www.selenium.dev/documentation/",
        "git": "https://git-scm.com/doc",
        "agile": "https://www.atlassian.com/agile",
        "default": "https://www.coursera.org/search?query="
    }
}

SKILLS_DB = _DEFAULT_SKILLS
try:
    if os.path.exists(_DB_PATH):
        with open(_DB_PATH, 'r', encoding='utf-8') as f:
            SKILLS_DB = json.load(f)
    else:
        # Recreate directory and file automatically if missing in cloud container
        os.makedirs(_DATA_DIR, exist_ok=True)
        with open(_DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(_DEFAULT_SKILLS, f, indent=2)
except Exception:
    SKILLS_DB = _DEFAULT_SKILLS

# Flatten all skills into one searchable list (preserve category info)
ALL_SKILLS = {}  # skill_lower -> category
for category, skills in SKILLS_DB.items():
    if isinstance(skills, list):
        for s in skills:
            ALL_SKILLS[s.lower()] = category

LEARNING_RESOURCES = SKILLS_DB.get('learning_resources', {})

# --- Text Preprocessing -------------------------------------------------------

def preprocess(text):
    """Lowercase and normalize whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s\.\+\#\/]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# --- Skill Extraction ---------------------------------------------------------

def extract_skills(text):
    """Return list of skills found in the text, with their categories."""
    text = preprocess(text)
    found = {}
    # Sort by length descending so multi-word skills match before sub-strings
    for skill in sorted(ALL_SKILLS.keys(), key=len, reverse=True):
        pattern = r'(?<![a-z0-9\.\+\#])' + re.escape(skill) + r'(?![a-z0-9\.\+\#])'
        if re.search(pattern, text):
            if skill not in found:
                found[skill] = ALL_SKILLS[skill]
    return found  # {skill: category}

# --- ATS Scoring -------------------------------------------------------------

def calculate_ats_score(resume_text, jd_text):
    """
    Calculate ATS match score between resume and job description.
    Returns a dict with score, matched skills, missing skills, tips.
    """
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    if not jd_skills:
        return {
            'score': 0,
            'matched': {},
            'missing': {},
            'resume_skills': resume_skills,
            'jd_skills': jd_skills,
            'tips': [],
            'keyword_density': 0,
            'error': 'No recognized skills found in the job description.'
        }

    matched = {s: c for s, c in jd_skills.items() if s in resume_skills}
    missing = {s: c for s, c in jd_skills.items() if s not in resume_skills}

    score = round(len(matched) / len(jd_skills) * 100)

    # Bonus keyword density check (simple word overlap)
    resume_words = set(preprocess(resume_text).split())
    jd_words = set(preprocess(jd_text).split())
    stopwords = {'and','or','the','a','an','to','for','in','of','with','is','are','be','will','we','you','our'}
    jd_words -= stopwords
    if jd_words:
        keyword_density = round(len(resume_words & jd_words) / len(jd_words) * 100)
    else:
        keyword_density = 0

    # Generate improvement tips
    tips = _generate_tips(score, matched, missing, resume_text, jd_text)

    return {
        'score': score,
        'matched': matched,
        'missing': missing,
        'resume_skills': resume_skills,
        'jd_skills': jd_skills,
        'tips': tips,
        'keyword_density': keyword_density,
        'error': None
    }

def _generate_tips(score, matched, missing, resume_text, jd_text):
    tips = []
    if score < 40:
        tips.append('Your resume has very low skill overlap. Tailor it specifically for this role.')
    elif score < 70:
        tips.append('Good foundation! Add the missing skills (if you have them) to boost your score.')
    else:
        tips.append('Excellent match! Your resume is well-aligned with this job description.')

    if len(missing) > 0:
        top_missing = list(missing.keys())[:3]
        tips.append(f'Consider adding: {", ".join(top_missing)} to strengthen your application.')

    if len(resume_text) < 300:
        tips.append('Your resume text seems short. A detailed resume performs better in ATS systems.')

    if 'summary' not in preprocess(resume_text) and 'objective' not in preprocess(resume_text):
        tips.append('Add a professional summary/objective at the top of your resume.')

    return tips

# --- Skill Gap Analyzer -------------------------------------------------------

def get_learning_resource(skill):
    skill_l = skill.lower()
    if skill_l in LEARNING_RESOURCES:
        return LEARNING_RESOURCES[skill_l]
    # Try partial match
    for k, v in LEARNING_RESOURCES.items():
        if k in skill_l or skill_l in k:
            return v
    return LEARNING_RESOURCES.get('default', '#') + skill.replace(' ', '+')

def analyze_skill_gaps(missing_skills):
    """Return list of {skill, category, resource} for missing skills."""
    gaps = []
    for skill, category in missing_skills.items():
        gaps.append({
            'skill': skill,
            'category': category.replace('_', ' ').title(),
            'resource': get_learning_resource(skill)
        })
    return gaps

# --- Interview Question Generator ---------------------------------------------

# Question bank per skill category
QUESTION_BANK = {
    'programming_languages': {
        'python': [
            ('What are Python decorators and how do you use them?', 'Decorators are functions that modify the behavior of other functions using the @syntax. Example: @staticmethod, @property, or custom decorators for logging/auth.'),
            ('Explain the difference between a list and a tuple in Python.', 'Lists are mutable (can be changed), tuples are immutable. Tuples are faster and used for fixed data. Lists use [], tuples use ().'),
            ('What is a virtual environment and why is it used?', 'A virtual environment isolates project dependencies so different projects can use different package versions without conflicts.'),
        ],
        'java': [
            ('What is the difference between abstract class and interface in Java?', 'Abstract classes can have implementations and state; interfaces (pre-Java 8) are pure contracts. A class can implement multiple interfaces but extend only one abstract class.'),
            ('Explain OOP concepts: encapsulation, inheritance, polymorphism, abstraction.', 'Encapsulation: bundling data with methods. Inheritance: child class inherits parent. Polymorphism: one interface, many forms. Abstraction: hiding complexity.'),
        ],
        'javascript': [
            ('What is the event loop in JavaScript?', 'The event loop handles async operations. It picks callbacks from the task queue and executes them when the call stack is empty, enabling non-blocking I/O.'),
            ('Explain the difference between let, const, and var.', 'var is function-scoped and hoisted. let and const are block-scoped. const cannot be reassigned. Prefer const > let > var.'),
        ],
    },
    'web_frontend': {
        'react': [
            ('What are React hooks and why were they introduced?', 'Hooks (useState, useEffect, etc.) let you use state and lifecycle features in functional components, reducing the need for class components.'),
            ('Explain the virtual DOM and how React uses it.', 'React keeps a virtual copy of the DOM. When state changes, it diffs the virtual DOM with the real DOM and only updates what changed - improving performance.'),
        ],
        'html': [
            ('What are semantic HTML elements and why are they important?', 'Semantic elements like <header>, <main>, <article> describe content meaning, improving accessibility, SEO, and code readability.'),
        ],
    },
    'databases': {
        'sql': [
            ('What is the difference between INNER JOIN and LEFT JOIN?', 'INNER JOIN returns rows where there is a match in both tables. LEFT JOIN returns all rows from the left table + matching rows from the right (NULL if no match).'),
            ('Explain database normalization and the first 3 normal forms.', '1NF: atomic values, no repeating groups. 2NF: no partial dependencies. 3NF: no transitive dependencies. Goal: reduce data redundancy.'),
        ],
        'mongodb': [
            ('What is the difference between SQL and NoSQL databases?', 'SQL databases are relational with fixed schemas and support ACID transactions. NoSQL (like MongoDB) are flexible schema, horizontally scalable, suited for unstructured data.'),
        ],
    },
    'cloud_devops': {
        'docker': [
            ('What is the difference between a Docker image and a container?', 'An image is a read-only blueprint. A container is a running instance of an image. Multiple containers can be created from the same image.'),
            ('What is Docker Compose used for?', 'Docker Compose defines and runs multi-container applications using a YAML file (docker-compose.yml), orchestrating services, networks, and volumes.'),
        ],
        'git': [
            ('What is the difference between git merge and git rebase?', 'Merge combines histories with a merge commit. Rebase rewrites history by replaying commits on top of another branch - creates a linear history.'),
        ],
        'aws': [
            ('What are the main AWS services you have worked with?', 'Common services: EC2 (compute), S3 (storage), RDS (database), Lambda (serverless), IAM (identity/access management), VPC (networking).'),
        ],
    },
    'testing': {
        'selenium': [
            ('What is the Page Object Model in Selenium?', 'POM is a design pattern where each web page has a corresponding class that stores elements and methods. It improves test maintainability and reduces duplication.'),
            ('What are the different types of locators in Selenium?', 'ID, Name, ClassName, TagName, LinkText, PartialLinkText, CSS Selector, XPath. Prefer ID > CSS Selector > XPath for performance.'),
            ('How do you handle dynamic web elements in Selenium?', 'Use explicit waits (WebDriverWait + ExpectedConditions) instead of Thread.sleep() to wait for elements to become visible, clickable, or present.'),
        ],
        'manual testing': [
            ('What is the difference between verification and validation?', 'Verification: are we building the product right? (reviews, inspections). Validation: are we building the right product? (testing against requirements).'),
            ('What is a test case and what does it contain?', 'A test case documents test steps, preconditions, expected results, actual results, and pass/fail status. It ensures systematic test coverage.'),
        ],
        'api testing': [
            ('What is the difference between GET, POST, PUT, and DELETE in REST APIs?', 'GET: retrieve data. POST: create new resource. PUT: update/replace resource. DELETE: remove resource. These follow REST conventions.'),
            ('How do you validate an API response in Postman?', 'Using the Tests tab with JavaScript: pm.test("Status", () => pm.response.to.have.status(200)); pm.expect(jsonData.key).to.equal(value);'),
        ],
    },
    'data_science_ml': {
        'machine learning': [
            ('What is the difference between supervised and unsupervised learning?', 'Supervised: learns from labeled data (classification, regression). Unsupervised: finds patterns in unlabeled data (clustering, dimensionality reduction).'),
            ('What is overfitting and how do you prevent it?', 'Overfitting: model performs well on training data but poorly on new data. Prevention: cross-validation, regularization (L1/L2), dropout, more training data, early stopping.'),
        ],
        'python': [
            ('Which Python libraries do you use for data analysis?', 'Pandas for data manipulation, NumPy for numerical computing, Matplotlib/Seaborn for visualization, Scikit-learn for ML models.'),
        ],
    },
    'project_management': {
        'agile': [
            ('What is the difference between Scrum and Kanban?', 'Scrum uses fixed sprints (1-4 weeks) with defined roles (Scrum Master, Product Owner). Kanban is a continuous flow board with WIP limits - no fixed iterations.'),
            ('What happens in a Sprint Retrospective?', 'The team reflects on the past sprint: what went well, what can improve, action items for next sprint. Focused on team process improvement.'),
        ],
        'jira': [
            ('How do you use Jira in your project workflow?', 'Jira is used to create user stories, track bugs, manage sprints, and generate burndown charts. Workflows can be customized per project.'),
        ],
    },
}

# Generic HR & behavioral questions
HR_QUESTIONS = [
    ('Tell me about yourself.', 'Briefly describe your educational background, key technical skills, and relevant projects/experience. Keep it professional and aligned with the role.'),
    ('Why do you want to work for this company?', 'Research the company - mention specific products, culture, or mission that resonates with you. Connect your goals with their values.'),
    ('Where do you see yourself in 5 years?', 'Express ambition within the field: growth in expertise, leadership roles, or specific technical domains - aligned with the company\'s direction.'),
    ('What is your greatest strength?', 'Choose a genuine, role-relevant strength with a specific example. Avoid generic answers like "I\'m a hard worker."'),
    ('Describe a challenge you faced and how you handled it.', 'Use the STAR method: Situation, Task, Action, Result. Focus on problem-solving and a positive outcome.'),
    ('How do you handle tight deadlines and multiple priorities?', 'Describe your prioritization approach: using task lists, communicating proactively with stakeholders, breaking tasks into smaller pieces.'),
    ('Are you comfortable working in a team environment?', 'Give a specific example of successful team collaboration - your role, how you communicated, and what you achieved together.'),
]

SITUATIONAL_QUESTIONS = [
    ('How would you approach debugging a complex production issue?', 'Reproduce the issue in staging if possible, check logs and error messages, narrow down the scope using binary search approach, fix and test thoroughly before deploying.'),
    ('If you disagreed with your team lead\'s technical decision, what would you do?', 'Respectfully raise your concern with supporting evidence/data in a private discussion. If overruled, accept the decision and support it as a team.'),
    ('How do you stay updated with new technologies in your field?', 'Reading tech blogs (Medium, Dev.to), following documentation, taking online courses (Coursera, Udemy), building side projects, attending webinars.'),
    ('What would you do if you found a bug in production right before a release?', 'Immediately escalate to the team lead, document the bug severity, propose a hotfix timeline, and decide together whether to delay the release or deploy a patch.'),
]

def generate_interview_questions(jd_text, resume_text=''):
    """
    Generate categorized interview questions from JD skills.
    Returns {hr: [...], technical: [...], situational: [...]}
    """
    jd_skills = extract_skills(jd_text)

    technical_qs = []
    added_skills = set()

    for skill, category in jd_skills.items():
        if skill in added_skills:
            continue

        # Check the question bank
        cat_bank = QUESTION_BANK.get(category, {})
        if skill in cat_bank:
            for q, a in cat_bank[skill]:
                technical_qs.append({'skill': skill, 'question': q, 'answer': a, 'category': category})
            added_skills.add(skill)
        else:
            # Generic technical question for unrecognized skills
            technical_qs.append({
                'skill': skill,
                'question': f'Describe your experience with {skill.title()} and how you have used it in a project.',
                'answer': f'Provide a specific project example using {skill.title()}, your role, what you implemented, and the outcome.',
                'category': category
            })
            added_skills.add(skill)

        if len(technical_qs) >= 12:
            break

    # Detect role type for extra HR context
    jd_lower = jd_text.lower()
    role_hints = []
    if any(w in jd_lower for w in ['test', 'qa', 'quality']):
        role_hints.append('QA/Testing')
    if any(w in jd_lower for w in ['develop', 'engineer', 'programmer']):
        role_hints.append('Development')
    if any(w in jd_lower for w in ['data', 'analyst', 'science']):
        role_hints.append('Data')
    if any(w in jd_lower for w in ['devops', 'cloud', 'infrastructure']):
        role_hints.append('DevOps')

    return {
        'hr': HR_QUESTIONS,
        'technical': technical_qs,
        'situational': SITUATIONAL_QUESTIONS,
        'role_hints': role_hints,
        'total_technical': len(technical_qs)
    }


# --- Resume Data Parser (For Style Cloner & PDF Rebuilder) --------------------

def parse_resume_data(text):
    """
    Intelligently parses uploaded resume text into structured fields and detects style archetype.
    Used by the PDF Resume Rebuilder tool.
    """
    if not text:
        return {}

    lines = [line.strip() for line in text.split('\n') if line.strip()]
    raw_lower = text.lower()

    # 1. Contact Extraction
    email_match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    email = email_match.group(0) if email_match else ''

    phone_match = re.search(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\b\d{10}\b', text)
    phone = phone_match.group(0) if phone_match else ''

    linkedin_match = re.search(r'(?:https?://)?(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+', text, re.IGNORECASE)
    linkedin = linkedin_match.group(0) if linkedin_match else ''
    if linkedin and not linkedin.startswith('http'):
        linkedin = 'https://' + linkedin

    portfolio_match = re.search(r'(?:https?://)?(?:www\.)?github\.com/[a-zA-Z0-9_-]+', text, re.IGNORECASE)
    portfolio = portfolio_match.group(0) if portfolio_match else ''
    if portfolio and not portfolio.startswith('http'):
        portfolio = 'https://' + portfolio

    # 2. Name Extraction (Examine first 5 lines for a candidate name)
    name = ''
    for line in lines[:6]:
        cleaned = re.sub(r'[^a-zA-Z\s\.]', '', line).strip()
        words = cleaned.split()
        if 2 <= len(words) <= 4:
            if not any(k in line.lower() for k in ['resume', 'curriculum', 'vitae', 'email', 'phone', 'page', 'profile', 'objective']):
                name = cleaned.title()
                break
    if not name and lines:
        name = lines[0][:30].title()

    # 3. Location Extraction
    location = ''
    location_patterns = [
        r'(?:location|address|city)\s*[:\-]\s*([a-zA-Z\s,]+)',
        r'\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?),\s*([A-Z]{2}|[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)\b'
    ]
    for pat in location_patterns:
        loc_match = re.search(pat, text)
        if loc_match:
            location = loc_match.group(1).strip() if len(loc_match.groups()) == 1 else f"{loc_match.group(1)}, {loc_match.group(2)}"
            break
    if not location:
        # Check first 5 lines for comma separated city
        for line in lines[1:5]:
            if ',' in line and not '@' in line and not 'http' in line:
                location = line.strip(' |---')[:40]
                break

    # 4. Section Splitting
    SECTION_HEADERS = {
        'summary': ['professional summary', 'career objective', 'summary', 'about me', 'profile', 'executive summary'],
        'skills': ['technical skills', 'skills & abilities', 'key skills', 'core competencies', 'skills', 'technologies'],
        'experience': ['work experience', 'professional experience', 'employment history', 'experience', 'internships', 'work history'],
        'education': ['education', 'academic background', 'educational qualifications', 'academics', 'qualifications'],
        'projects': ['academic projects', 'key projects', 'projects', 'personal projects', 'technical projects'],
        'certifications': ['certifications', 'licenses & certifications', 'certificates', 'achievements', 'awards', 'courses']
    }

    # Identify lines that act as section headers
    section_positions = []
    for idx, line in enumerate(lines):
        clean_header = re.sub(r'[^a-zA-Z\s]', '', line).strip().lower()
        for sec_name, keywords in SECTION_HEADERS.items():
            if clean_header in keywords and len(clean_header) > 2:
                section_positions.append((idx, sec_name))
                break

    section_positions.sort(key=lambda x: x[0])

    sections = {}
    for i, (start_idx, sec_name) in enumerate(section_positions):
        end_idx = section_positions[i+1][0] if i+1 < len(section_positions) else len(lines)
        sec_text = '\n'.join(lines[start_idx+1:end_idx]).strip()
        sections[sec_name] = sec_text

    # 5. Extract Skills
    found_skills_dict = extract_skills(text)
    auto_skills = list(found_skills_dict.keys())
    # If skills section has additional tokens
    if 'skills' in sections:
        skills_chunk = sections['skills']
        raw_items = [s.strip() for s in re.split(r'[,|-\n]', skills_chunk) if len(s.strip()) > 1]
        for it in raw_items:
            it_clean = it.strip('--* ').lower()
            if it_clean and it_clean not in auto_skills and len(it_clean) < 30:
                auto_skills.append(it_clean)

    skills_str = ', '.join([s.title() for s in auto_skills[:25]])

    # 6. Extract Summary
    summary = sections.get('summary', '')
    if not summary:
        # Check first paragraph after name/contact info
        for line in lines[2:8]:
            if len(line) > 50 and not '@' in line and not 'http' in line:
                summary = line
                break

    # 7. Extract Experience Entries
    experience_list = []
    exp_text = sections.get('experience', '')
    if exp_text:
        exp_blocks = [b.strip() for b in re.split(r'\n(?=[A-Z0-9][a-zA-Z0-9\s-\--|]{2,40}(?:19\d\d|20\d\d|present|current))', exp_text, flags=re.IGNORECASE) if b.strip()]
        for block in exp_blocks[:5]:
            block_lines = [l.strip() for l in block.split('\n') if l.strip()]
            if not block_lines:
                continue
            first_line = block_lines[0]
            # Try to extract role and company
            role = first_line
            company = ''
            duration = ''
            if '-' in first_line or '-' in first_line or '|' in first_line:
                parts = re.split(r'[--|]', first_line)
                role = parts[0].strip()
                company = parts[1].strip() if len(parts) > 1 else ''
            
            # Find date in block
            date_match = re.search(r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)?\.?\s*(?:19\d\d|20\d\d)\s*[--to\s]+\s*(?:(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)?\.?\s*(?:19\d\d|20\d\d)|present|current)\b', block, re.IGNORECASE)
            if date_match:
                duration = date_match.group(0).strip()
            
            desc_lines = [l.lstrip('---* ') for l in block_lines[1:] if len(l) > 5]
            experience_list.append({
                'role': role[:45],
                'company': company[:45],
                'duration': duration[:30],
                'description': '\n'.join(desc_lines)
            })

    # Default fallback experience if none parsed
    if not experience_list and exp_text:
        experience_list.append({
            'role': 'Professional Role',
            'company': 'Previous Company',
            'duration': '2022 - Present',
            'description': exp_text[:300]
        })

    # 8. Extract Education Entries
    education_list = []
    edu_text = sections.get('education', '')
    if edu_text:
        edu_lines = [l.strip() for l in edu_text.split('\n') if l.strip()]
        for line in edu_lines:
            degree_found = ''
            for deg_kw in ['mca', 'bca', 'b.tech', 'm.tech', 'b.e', 'm.e', 'b.sc', 'm.sc', 'bachelor', 'master', 'diploma', 'ph.d', 'secondary']:
                if deg_kw in line.lower():
                    degree_found = line
                    break
            
            year_match = re.search(r'\b(?:20\d\d|19\d\d)(?:\s*[--]\s*(?:20\d\d|present))?\b', line, re.IGNORECASE)
            year = year_match.group(0) if year_match else ''
            
            grade_match = re.search(r'(?:\b\d\.\d+\s*(?:cgpa|gpa)?|\b\d{2,3}%\b)', line, re.IGNORECASE)
            grade = grade_match.group(0) if grade_match else ''
            
            if degree_found or len(education_list) < 2:
                education_list.append({
                    'degree': degree_found[:40] if degree_found else line[:40],
                    'institution': 'University / College',
                    'year': year,
                    'grade': grade
                })
            if len(education_list) >= 3:
                break

    # 9. Extract Projects
    projects_list = []
    proj_text = sections.get('projects', '')
    if proj_text:
        proj_blocks = [b.strip() for b in proj_text.split('\n\n') if b.strip()]
        for block in proj_blocks[:4]:
            p_lines = [l.strip() for l in block.split('\n') if l.strip()]
            if not p_lines:
                continue
            title = p_lines[0]
            tech = ''
            tech_match = re.search(r'\((.*?)\)', title)
            if tech_match:
                tech = tech_match.group(1)
                title = title.replace(tech_match.group(0), '').strip()
            desc = '\n'.join(p_lines[1:])
            projects_list.append({
                'title': title[:50],
                'tech': tech[:40],
                'description': desc
            })

    # 10. Extract Certifications
    cert_text = sections.get('certifications', '')

    # 11. Layout Style Archetype Detection
    # Determines which template matches the original layout
    detected_style = 'modern'
    if any(k in raw_lower for k in ['manager', 'director', 'lead', 'vice president', 'architect']):
        detected_style = 'executive'
    elif len(lines) < 25 and len(found_skills_dict) < 8:
        detected_style = 'minimal'
    elif 'classic' in raw_lower or 'curriculum vitae' in raw_lower or not email:
        detected_style = 'classic'

    return {
        'full_name': name or 'Devadharshini R',
        'email': email or 'candidate@example.com',
        'phone': phone or '+91 98765 43210',
        'location': location or 'Chennai, Tamil Nadu',
        'linkedin': linkedin,
        'portfolio': portfolio,
        'summary': summary or 'Motivated professional with strong hands-on problem solving skills and experience in software development and testing.',
        'skills': skills_str or 'Python, SQL, Manual Testing, Selenium, HTML, CSS, Git, Agile',
        'education': education_list,
        'experience': experience_list,
        'projects': projects_list,
        'certifications': cert_text,
        'detected_style': detected_style,
        'sections_found': list(sections.keys())
    }


# --- Job Description Optimization --------------------------------------------

def optimize_resume_for_jd(parsed_data, jd_text):
    """
    Optimize a parsed resume dict against a Job Description.
    Returns the mutated parsed_data plus an optimization_report dict.
    Pure rule-based - no external API required.
    """
    if not jd_text or not jd_text.strip():
        return parsed_data, {}

    resume_skills_str = parsed_data.get('skills', '')
    resume_summary = parsed_data.get('summary', '')

    # --- Score before optimization ---
    score_before_data = calculate_ats_score(
        resume_skills_str + ' ' + resume_summary,
        jd_text
    )
    score_before = score_before_data.get('score', 0)
    matched_skills = score_before_data.get('matched_skills', [])
    missing_skills = score_before_data.get('missing_skills', [])

    # --- Extract top JD keywords (bigrams + single words) ---
    jd_lower = jd_text.lower()
    jd_words = re.findall(r'\b[a-z][a-z0-9+#.]{2,}\b', jd_lower)
    # Build bigrams
    jd_bigrams = [jd_words[i] + ' ' + jd_words[i+1] for i in range(len(jd_words)-1)]
    all_jd_terms = jd_bigrams + jd_words

    # Match against skills DB
    all_known = []
    for cat, items in _DEFAULT_SKILLS.items():
        if isinstance(items, list):
            all_known.extend(items)

    jd_keywords = []
    for term in all_jd_terms:
        if term in all_known and term not in jd_keywords:
            jd_keywords.append(term)

    # --- Reorder skills: matched first, then rest ---
    existing_skill_list = [s.strip() for s in resume_skills_str.split(',') if s.strip()]
    matched_set = {m.lower() for m in matched_skills}

    leading = [s for s in existing_skill_list if s.lower() in matched_set]
    trailing = [s for s in existing_skill_list if s.lower() not in matched_set]

    # Suggested skills: top missing that exist in JD keywords
    suggested = []
    for m in missing_skills[:8]:
        if m.lower() in jd_lower and m not in suggested:
            suggested.append(m)

    optimized_skills_list = leading + trailing
    optimized_skills_str = ', '.join(optimized_skills_list) if optimized_skills_list else resume_skills_str

    # --- Optimize summary: inject top 3 missing JD keywords naturally ---
    optimized_summary = resume_summary
    summary_changed = False
    if missing_skills and resume_summary:
        inject_terms = [s for s in missing_skills[:5] if len(s) > 3 and s.lower() not in resume_summary.lower()][:3]
        if inject_terms:
            terms_str = ', '.join(inject_terms)
            if resume_summary.endswith('.'):
                optimized_summary = resume_summary[:-1] + ', with exposure to ' + terms_str + '.'
            else:
                optimized_summary = resume_summary + '. Familiar with ' + terms_str + '.'
            summary_changed = True

    # --- Score after optimization ---
    score_after_data = calculate_ats_score(
        optimized_skills_str + ' ' + optimized_summary,
        jd_text
    )
    score_after = score_after_data.get('score', 0)

    # Apply changes back to parsed_data
    parsed_data['skills'] = optimized_skills_str
    if summary_changed:
        parsed_data['summary'] = optimized_summary

    optimization_report = {
        'score_before': score_before,
        'score_after': score_after,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills[:10],
        'suggested_skills': suggested,
        'summary_changed': summary_changed,
        'optimized_summary': optimized_summary if summary_changed else '',
    }

    return parsed_data, optimization_report
