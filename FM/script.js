document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // отключаем слежку после активации
            }
        });
    }, { threshold: 0.2 }); // 20% видимости элемента

    sections.forEach(section => {
        observer.observe(section);
    });
});