#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        throw error
    }
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((url) => {
        request(url, (charError, charResponse, charBody) => {
            if (charError) {
                throw charError;
            }

            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});
