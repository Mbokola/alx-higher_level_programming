#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  const statusCode = response.statusCode;
  console.log(`code: ${statusCode}`);
});
