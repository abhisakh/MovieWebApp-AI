// scripts.js

document.addEventListener('DOMContentLoaded', () => {

    // -----------------------------
    // Flash Messages Auto-Dismiss
    // -----------------------------
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.classList.add("fade-out");
            setTimeout(() => flash.remove(), 1000);
        }, 4000);
    });

    // -----------------------------
    // Add Movie Form Toggle
    // -----------------------------
    const toggleAddBtn = document.getElementById("toggleAddMovie");
    const addFormContainer = document.getElementById("addMovieForm");
    const cancelAddBtn = document.getElementById("cancelAddMovie");

    if (toggleAddBtn && addFormContainer) {
        toggleAddBtn.addEventListener("click", () => {
            addFormContainer.classList.toggle("open");
            toggleAddBtn.textContent = addFormContainer.classList.contains("open")
                ? "✖ Close Form"
                : "➕ Add Movie";
        });
    }

    if (cancelAddBtn && addFormContainer) {
        cancelAddBtn.addEventListener("click", () => {
            addFormContainer.classList.remove("open");
            toggleAddBtn.textContent = "➕ Add Movie";
        });
    }

    // -----------------------------
    // Update Movie Form Toggle
    // -----------------------------
    const updateButtons = document.querySelectorAll('.toggle-update-btn');
    updateButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const formContainer = btn.nextElementSibling;
            formContainer.classList.toggle('open');
        });
    });

    const cancelUpdateButtons = document.querySelectorAll('.cancel-update-btn');
    cancelUpdateButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const formContainer = btn.closest('.collapsible-update-form');
            formContainer.classList.remove('open');
        });
    });

    // -----------------------------
    // AI Movie Suggestions Handling
    // -----------------------------
    const userSelect = document.getElementById('target_user');
    const userIdInputs = document.querySelectorAll('.user-id-input');

    const searchForm = document.getElementById('ai-search-form');
    const searchButton = document.getElementById('search-button');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Function to update hidden user_id input in all forms
    function updateForms() {
        const selectedUserId = userSelect ? userSelect.value : null;
        if (selectedUserId) {
            userIdInputs.forEach(input => {
                input.value = selectedUserId;
            });
        }
    }

    // Initialize User Select for AI Suggestions
    if (userSelect) {
        updateForms();
        userSelect.addEventListener('change', updateForms);
    }

    // Show loading spinner on AI Suggestions form submit
    if (searchForm && searchButton && loadingIndicator) {
        searchForm.addEventListener('submit', () => {
            searchButton.disabled = true;
            searchButton.innerHTML = '<i class="bi bi-search"></i> Searching...';
            loadingIndicator.style.display = 'block';
        });
    }

});
