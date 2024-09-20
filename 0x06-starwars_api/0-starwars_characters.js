#!/usr/bin/node

const request = require('request');

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
        chars.forEach((char) => {
            request(char, (err, response, body) => {
            if (err) {
                throw err;
            } else {
                console.log(JSON.parse(body).name);
            }
            });
        });
    }
  }
);