#!/usr/bin/node
// Script that prints “JavaScript is amazing”

const listy = require('./100-data').list;

console.log(listy);
console.log(listy.map((item, index) => index * item));
