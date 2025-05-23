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

  // Показываем .project-header при появлении
  ScrollReveal().reveal('.project-header', {
    duration: 1000,
    origin: 'top',
    distance: '50px',
    reset: true, // Анимация повторяется при уходе и возврате
    viewFactor: 0.33 // Срабатывает, когда элемент виден на 1/3 экрана
  });

  // Основные секции и подсекции
  ScrollReveal().reveal('.section, .subsection, .authors', {
    duration: 800,
    origin: 'bottom',
    distance: '40px',
    interval: 200,
    reset: true,
    viewFactor: 0.33
  });

   ScrollReveal().reveal('.section.desktop-only', {
     duration: 800,               // Длительность анимации
     origin: 'bottom',            // Откуда появляется (снизу)
     distance: '40px',            // На какое расстояние двигается
     interval: 200,               // Интервал между элементами (если несколько)
     reset: true,                 // Повторная анимация при уходе и возврате
     viewFactor: 0.4,             // Активация при появлении на 40% экрана
     opacity: 0,                  // Начальная прозрачность
     scale: 0.95                  // Лёгкое уменьшение при старте (опционально)
   });

  // Авторские ссылки
  ScrollReveal().reveal('.author-link', {
    duration: 600,
    origin: 'left',
    distance: '30px',
    delay: 200,
    reset: true,
    viewFactor: 0.33
  });
});

