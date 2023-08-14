#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}
const arg = Number(process.argv[2]);
if (!arg) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
