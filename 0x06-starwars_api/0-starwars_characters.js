#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((url) => {
        request(url, (charError, charResponse, charBody) => {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});
