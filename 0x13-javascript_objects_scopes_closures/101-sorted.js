#!/usr/bin/node

const dict = require('./101-data');
const dictValue = dict.dict;

const newDict = {}

for (let key in dictValue) {
  let value = dictValue[key];
  if (!(value in newDict)) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}

console.log(newDict);
