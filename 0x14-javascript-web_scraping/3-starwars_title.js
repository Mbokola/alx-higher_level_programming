#!/usr/bin/node

const request = require('request');
const number = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${number}`;

request(apiUrl, { json: true }, (err, response, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
