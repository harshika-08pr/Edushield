// ==========================================
// EduShield JavaScript
// ==========================================

// ------------------------------
// Active Navbar
// ------------------------------

document.addEventListener("DOMContentLoaded", function () {

    let current = window.location.pathname;

    document.querySelectorAll(".nav-link").forEach(link => {

        if(link.getAttribute("href") === current){

            link.classList.add("active");

        }

    });

});

// ------------------------------
// Animate Cards
// ------------------------------

const cards = document.querySelectorAll(".card");

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.classList.add("show-card");

        }

    });

});

cards.forEach(card => {

    observer.observe(card);

});

// ------------------------------
// Counter Animation
// ------------------------------

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    counter.innerText = "0";

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const c = +counter.innerText;

        const increment = target / 80;

        if(c < target){

            counter.innerText = `${Math.ceil(c + increment)}`;

            setTimeout(updateCounter,25);

        }
        else{

            counter.innerText = target;

        }

    };

    updateCounter();

});

// ------------------------------
// Loading Spinner
// ------------------------------

const form = document.querySelector("form");

if(form){

form.addEventListener("submit",function(){

const spinner=document.getElementById("loading");

if(spinner){

spinner.style.display="flex";

}

});

}