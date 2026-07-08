// Navbar shadow

window.addEventListener("scroll", () => {

    const nav = document.querySelector(".navbar");

    if(window.scrollY > 40){

        nav.style.boxShadow="0 5px 20px rgba(0,0,0,.10)";

    }else{

        nav.style.boxShadow="none";

    }

});



// Animación de aparición

const cards = document.querySelectorAll(".product-card");

cards.forEach((card,index)=>{

    card.style.opacity=0;

    card.style.transform="translateY(30px)";

    setTimeout(()=>{

        card.style.transition=".5s";

        card.style.opacity=1;

        card.style.transform="translateY(0px)";

    },index*80);

});



// Confirmar salida

const links = document.querySelectorAll(".btn");

links.forEach(link=>{

    link.addEventListener("click",(e)=>{

        if(!confirm("¿Deseas abrir este producto en una nueva pestaña?")){

            e.preventDefault();

        }

    });

});