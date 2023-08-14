#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);
if (arg1 && arg2) {
  console.log(add(arg1, arg2));
} else {
  console.log('NaN');
}
