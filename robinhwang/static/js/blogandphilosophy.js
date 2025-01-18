document.getElementById('searchButton').addEventListener('click', function () {
    const searchQuery = document.getElementById('searchBar').value.toLowerCase();
    const posts = document.querySelectorAll('.box');

    posts.forEach(post => {
        const title = post.querySelector('h2').innerText.toLowerCase();
        const content = post.querySelector('.content').innerText.toLowerCase();

        if (title.includes(searchQuery) || content.includes(searchQuery)) {
            post.style.display = '';
        } else {
            post.style.display = 'none';
        }
    });
});