document.addEventListener('DOMContentLoaded',function(){
    let searchInput = document.querySelector('#search-input');
    if(searchInput){
        searchInput.addEventListener('input', function(){
            if (this.value.trim().length > 0) {
                this.style.border = '2px solid #28a745'; 
            }
            else {
                this.style.border = '1px solid #ced4da'; 
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    let cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa'; 
        });
        card.addEventListener('mouseleave', function() {
            this.style.backgroundColor = ''; 
        });
    });
});