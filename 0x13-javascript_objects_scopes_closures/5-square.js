#!/usr/bin/node
// Script that prints “JavaScript is amazing”
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
