#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.err(err);
    return;
  }
  const obj = {};
  body.forEach((user) => {
    if (Object.prototype.hasOwnProperty.call(obj, user.userId)) {
      if (user.completed) {
        obj[user.userId] += 1;
      }
    } else {
      obj[user.userId] = user.completed ? 1 : 0;
    }
  });
  console.log(obj);
});
