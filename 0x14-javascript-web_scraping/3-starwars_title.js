#!/usr/bin/node

const request = require('request');
const number = process.argv[2];
const api_url = `https://swapi-api.alx-tools.com/api/films/${number}`;

request(api_url, { json: true }, (err, response, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
