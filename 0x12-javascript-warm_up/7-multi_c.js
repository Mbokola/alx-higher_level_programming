#!/usr/bin/node

let times = process.argv[2];
if (!times) {
  console.log('Missing number of occurrences');
}
while (times) {
  if (times < 0) {
    break;
  }
  console.log('C is fun');
  times--;
}
