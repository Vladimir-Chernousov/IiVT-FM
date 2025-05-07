document.addEventListener("DOMContentLoaded", function () {
  const backToTop = document.querySelector(".back-to-top");

  if (backToTop) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 100) {
        backToTop.style.display = "flex"; // Используем flex вместо block
      } else {
        backToTop.style.display = "none";
      }
    });

    backToTop.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  ScrollReveal().reveal('.project-header', {
        duration: 1000,
        origin: 'top',
        distance: '50px'
    });

    ScrollReveal().reveal('.section, .subsection, .authors', {
        duration: 800,
        origin: 'bottom',
        distance: '40px',
        interval: 200
    });

    ScrollReveal().reveal('.author-link', {
        duration: 600,
        origin: 'left',
        distance: '30px',
        delay: 200
    });
});

