#!/usr/bin/node

const size = process.argv[2];

if (!size || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'x';
    }
    console.log(line);
  }
}
