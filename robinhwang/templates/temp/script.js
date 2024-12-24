document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {

            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');

        });
    });

});

document.addEventListener("DOMContentLoaded", function () {
    const progressBars = [
        { id: "progress-energy", value: 64 },
        { id: "progress-mind", value: 52 },
        { id: "progress-nature", value: 59 },
        { id: "progress-tactics", value: 93 },
    ];

    const container = document.querySelector('.mbti-container');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Start animation for each progress bar
                progressBars.forEach((bar) => {
                    const progressBar = document.getElementById(bar.id);
                    let currentValue = 0;
                    const increment = bar.value / 100;

                    const animate = setInterval(() => {
                        currentValue += increment;
                        progressBar.value = currentValue;
                        if (currentValue >= bar.value) {
                            clearInterval(animate);
                            progressBar.value = bar.value; // Ensure it ends at the exact value
                        }
                    }, 10);
                });

                // Stop observing the container once animation starts
                observer.unobserve(container);
            }
        });
    }, { threshold: 0.2 }); // Trigger animation when 20% of the container is visible

    observer.observe(container);
});
