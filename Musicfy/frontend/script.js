document.addEventListener("DOMContentLoaded", function() {
    fetch('http://localhost:8000/api/songs/')
    .then(response => response.json())
    .then(data => {
        const songList = document.getElementById('song-list');
        data.forEach(song => {
            const songItem = document.createElement('div');
            songItem.classList.add('song-item');
            songItem.innerHTML = `
                <h3>${song.title}</h3>
                <p>${song.artist}</p>
                <img src="${song.cover}" alt="${song.title} cover">
                <audio controls>
                    <source src="${song.audio}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            `;
            songList.appendChild(songItem);
        });
    })
    .catch(error => {
        console.error('Error fetching songs:', error);
        const errorMsg = document.createElement('p');
        errorMsg.textContent = 'Failed to load songs. Please try again later.';
        document.body.appendChild(errorMsg);
    });
});