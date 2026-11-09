// ── Mobile Responsive Sidebar Toggle ─────────────────────────────────────────
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

// ── Interactive Purple Ripple Effect on Buttons ───────────────────────────────
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

// ── Responsive Loading State for Form Submissions ────────────────────────────
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
