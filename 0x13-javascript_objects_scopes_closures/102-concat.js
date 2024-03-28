#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const sourceFiles = [fileA, fileB];

async function execute () {
  for (const file of sourceFiles) {
    try {
      const data = await readfile(file);
      writefile(fileC, data);
    } catch (err) {
      console.error(err);
    }
  }
}

function readfile (file) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, (err, data) => {
      if (err) {
        reject(err);
      }
      resolve(data);
    });
  });
}

function writefile (file, data) {
  return new Promise((resolve, reject) => {
    fs.appendFile(file, data, (err) => {
      if (err) {
        reject(err);
      }
    });
  });
}

execute();
