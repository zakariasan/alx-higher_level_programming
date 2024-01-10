#!/usr/bin/node
// Script that prints “JavaScript is amazing”
const SquareF = require('./5-square');

class Square extends SquareF {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
