#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (err, response, body) => {
  if (err) {
    console.err(err);
    return;
  }
  const found = body.results.map((film) => {
    const films = film.characters.filter((url) => {
      const id = url.substring(url.length - 4);
      return id === '/18/';
    });
    return films;
  }).filter((film) => film.length > 0);
  console.log(found.length);
});
