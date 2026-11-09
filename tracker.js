// ── Job Tracker JavaScript ────────────────────────────────────────────────────

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
