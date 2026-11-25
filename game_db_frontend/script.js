async function getRequest() {
    const gamesDiv = document.getElementById('container');

    try {
        // URL нужно обернуть в кавычки
        const response = await fetch('http://127.0.0.1:8000/api/v1/game_db/');

        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }

        const data = await response.json();

        gamesDiv.innerHTML = '';

        const ElementContainer = document.createElement('div');
        ElementContainer.classList = 'wrapper';

        gamesDiv.appendChild(ElementContainer);

        data.forEach(game => {
            const gameElement = document.createElement('div');
            gameElement.classList.add('card');

            gameElement.innerHTML = `
                <img src="${game.str_thumbnails}" alt="${game.name}">
                <h2>${game.name}</h2>
                <p>${game.description}</p>
                <p><b>Category:</b> ${game.category_name}</p>
                <p><b>Price:</b> ${game.price_value} $</p>
            `;

            ElementContainer.appendChild(gameElement);
        });


    } catch (error) {
        gamesDiv.textContent = error.message;
        console.error(error);
    }
}

getRequest();


const themeSelect = document.getElementById('theme-select');

themeSelect.value = localStorage.getItem('theme') || 'light';

document.documentElement.setAttribute('data-theme', themeSelect.value);

themeSelect.addEventListener('change', function() {
    document.documentElement.setAttribute('data-theme', this.value);
    localStorage.setItem('theme', this.value);
});


// document.getElementById('games').textContent = JSON.stringify(data, null, 2);
