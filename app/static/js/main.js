document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    
    if (searchForm) {
        // Initialize form elements based on URL parameters
        const urlParams = new URLSearchParams(window.location.search);
        
        const sortSelect = document.getElementById('sort');
        if (sortSelect && urlParams.has('sort')) {
            sortSelect.value = urlParams.get('sort');
        }
        
        const orderSelect = document.getElementById('order');
        if (orderSelect && urlParams.has('order')) {
            orderSelect.value = urlParams.get('order');
        }
        
        const perPageSelect = document.getElementById('per_page');
        if (perPageSelect && urlParams.has('per_page')) {
            perPageSelect.value = urlParams.get('per_page');
        }
    }
});