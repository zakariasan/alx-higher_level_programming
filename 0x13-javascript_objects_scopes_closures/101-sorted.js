#!/usr/bin/node
// Script that prints “JavaScript is amazing”

const dicty = require('./101-data').dict;
const res = {};
for (const id in dicty) {
  const occurrences = dicty[id];
  if (!res[occurrences]) {
    res[occurrences] = [];
  }
  res[occurrences].push(id.toString());
}

console.log(res);
