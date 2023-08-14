#!/usr/bin/node

const len = process.argv.length;
if (len >= 3) {
  const converted = Number(process.argv[2]);
  if (isNaN(converted)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + converted);
  }
} else {
  console.log('Not a number');
}
