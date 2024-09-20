#!/usr/bin/node

const fetch = require('node-fetch');
const movieId = process.argv[2];


const apiUrl = `https://swapi.dev/api/films/${movieId}/`;


(async () => {
    const response = await fetch(apiUrl);
    const movieData = await response.json();
    const characterUrls = movieData.characters;

    for (const url of characterUrls) {
            const charResponse = await fetch(url);
            const charData = await charResponse.json();
            console.log(charData.name);
    }
})();
