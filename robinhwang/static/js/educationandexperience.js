function adjustTimelineClasses() {
    const screenWidth = window.innerWidth;

    // If screen width is below 1024px, remove classes
    if (screenWidth < 1024) {
        const timelineElements = document.querySelectorAll('.timeline');
        timelineElements.forEach(element => element.classList.remove('timeline'));
        timelineElements.forEach(element => element.classList.add('temp-timeline'));
    }
    // If screen width is 1024px or above, re-add classes
    else {
        const timelineElements = document.querySelectorAll('.temp-timeline');
        timelineElements.forEach(element => {
                element.classList.add('timeline');
        });
    }
}

// Run the function on page load
adjustTimelineClasses();

// Monitor screen size changes dynamically
window.addEventListener('resize', adjustTimelineClasses);