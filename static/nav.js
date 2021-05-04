const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.links');
    const navlink= document.querySelectorAll('.links li');


    burger.addEventListener('click',() => {
        nav.classList.toggle('links-active');

        navlink.forEach((link,index) =>{
            if (link.style.animation){
                link.style.animation =''
            }
            else{
            link.style.animation =`linksFade 0.5s ease forwards ${index / 7 + 0.5 }s `;

            }
    
        });
        burger.classList.toggle("link");
    });
  

}
navSlide();