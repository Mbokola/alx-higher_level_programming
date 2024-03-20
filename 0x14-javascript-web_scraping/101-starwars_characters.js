#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, async (err, res, body) => {
  if (err) {
    console.err(err);
    return;
  }
  for (const characterUrl of body.characters) {
    try {
      const body = await getRequest(characterUrl)
      console.log(body.name);
    } catch (err) {
      console.error(err);
    }
  }
});

function getRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true } , (err, res, body) => {
      if (err) {
        reject(err)
      } else {
        resolve(body)
      }
    });
  });
};
