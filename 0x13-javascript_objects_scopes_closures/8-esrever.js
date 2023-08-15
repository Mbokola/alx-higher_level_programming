#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let len = list.length - 1;
  while (len >= 0) {
    reversed.push(list[len]);
    len--;
  }
  return reversed;
};
