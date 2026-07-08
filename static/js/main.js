window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    if (window.scrollY > 40) {
        navbar.style.boxShadow = "0 5px 20px rgba(0,0,0,.10)";
    } else {
        navbar.style.boxShadow = "none";
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".product-card");

    cards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(25px)";

        setTimeout(() => {
            card.style.transition = ".45s ease";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, index * 60);
    });

    const externalButtons = document.querySelectorAll('a[target="_blank"]');

    externalButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const confirmOpen = confirm("¿Deseas abrir este producto en una nueva pestaña?");

            if (!confirmOpen) {
                event.preventDefault();
            }
        });
    });
});