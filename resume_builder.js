// ── Resume Builder — Dynamic Form Functions ────────────────────────────────────

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
                <input type="text" name="edu_year" class="form-input" placeholder="2022 – 2024">
            </div>
            <div class="form-group">
                <label>Grade / CGPA</label>
                <input type="text" name="edu_grade" class="form-input" placeholder="8.5 CGPA">
            </div>
        </div>
        <button type="button" class="btn-remove" onclick="removeRow(this)">✕ Remove</button>
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
                <input type="text" name="exp_duration" class="form-input" placeholder="Jun 2023 – Present">
            </div>
        </div>
        <div class="form-group">
            <label>Responsibilities & Achievements</label>
            <textarea name="exp_description" class="form-textarea" rows="3"
                placeholder="• Describe your responsibilities and achievements (one per line)..."></textarea>
        </div>
        <button type="button" class="btn-remove" onclick="removeRow(this)">✕ Remove</button>
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
        <button type="button" class="btn-remove" onclick="removeRow(this)">✕ Remove</button>
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

// ── Form validation ───────────────────────────────────────────────────────────
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
