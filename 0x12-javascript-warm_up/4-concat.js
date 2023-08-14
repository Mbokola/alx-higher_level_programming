#!/usr/bin/node
const len = process.argv.length;
if (len >= 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (len === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
