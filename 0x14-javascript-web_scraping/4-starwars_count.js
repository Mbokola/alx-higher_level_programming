#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

let foundId;

request(apiUrl, { json:true }, (err, response, body) => {
  if (err) {
    console.err(err);
    return;
  }
  body.results.map((film) => {
    const films = film.characters.find((url) => {
      const id = url.substring(url.length - 4);
      if (id === '/18/') {
        request(url, { json:true }, (err, response, body) => {
          if(err) {
            console.err(err);
            return;
          }
          if (!foundId) console.log(body.films.length);
          foundId = true;
        });
      }
    });
  });
});
