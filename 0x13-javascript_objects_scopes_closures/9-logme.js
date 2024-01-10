#!/usr/bin/node
// Script that prints “JavaScript is amazing”

let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
