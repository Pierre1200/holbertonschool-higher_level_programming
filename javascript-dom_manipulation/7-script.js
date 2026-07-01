#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const listMovies = document.getElementById('list_movies');

        movies.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            listMovies.appendChild(li);
        });
    });