#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.err(err);
    return;
  }
  body.characters.forEach((character) => {
    request(character, { json: true }, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(body.name);
    });
  });
});
