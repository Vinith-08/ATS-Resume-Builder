"""
ATS Engine — Skill extraction, match scoring, gap analysis, interview Q generation.
All rule-based — no external API required.
"""

import re
import json
import os

# ─── Load Skills Database ─────────────────────────────────────────────────────

_DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'skills_db.json')
with open(_DB_PATH, 'r', encoding='utf-8') as f:
    SKILLS_DB = json.load(f)

# Flatten all skills into one searchable list (preserve category info)
ALL_SKILLS = {}  # skill_lower -> category
for category, skills in SKILLS_DB.items():
    if isinstance(skills, list):
        for s in skills:
            ALL_SKILLS[s.lower()] = category

LEARNING_RESOURCES = SKILLS_DB.get('learning_resources', {})

# ─── Text Preprocessing ───────────────────────────────────────────────────────

def preprocess(text):
    """Lowercase and normalize whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s\.\+\#\/]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ─── Skill Extraction ─────────────────────────────────────────────────────────

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

# ─── ATS Scoring ─────────────────────────────────────────────────────────────

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

# ─── Skill Gap Analyzer ───────────────────────────────────────────────────────

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

# ─── Interview Question Generator ─────────────────────────────────────────────

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
            ('Explain the virtual DOM and how React uses it.', 'React keeps a virtual copy of the DOM. When state changes, it diffs the virtual DOM with the real DOM and only updates what changed — improving performance.'),
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
            ('What is the difference between git merge and git rebase?', 'Merge combines histories with a merge commit. Rebase rewrites history by replaying commits on top of another branch — creates a linear history.'),
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
            ('What is the difference between Scrum and Kanban?', 'Scrum uses fixed sprints (1–4 weeks) with defined roles (Scrum Master, Product Owner). Kanban is a continuous flow board with WIP limits — no fixed iterations.'),
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
    ('Why do you want to work for this company?', 'Research the company — mention specific products, culture, or mission that resonates with you. Connect your goals with their values.'),
    ('Where do you see yourself in 5 years?', 'Express ambition within the field: growth in expertise, leadership roles, or specific technical domains — aligned with the company\'s direction.'),
    ('What is your greatest strength?', 'Choose a genuine, role-relevant strength with a specific example. Avoid generic answers like "I\'m a hard worker."'),
    ('Describe a challenge you faced and how you handled it.', 'Use the STAR method: Situation, Task, Action, Result. Focus on problem-solving and a positive outcome.'),
    ('How do you handle tight deadlines and multiple priorities?', 'Describe your prioritization approach: using task lists, communicating proactively with stakeholders, breaking tasks into smaller pieces.'),
    ('Are you comfortable working in a team environment?', 'Give a specific example of successful team collaboration — your role, how you communicated, and what you achieved together.'),
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
