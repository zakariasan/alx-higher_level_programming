#!/usr/bin/node
// Script that prints “JavaScript is amazing”
const SquareF = require('./5-square');

class Square extends SquareF {
  charPrint (c) {
    const ch = (c === undefined) ? 'X' : 'C';
    for (let x = 0; x < this.height; x++) {
      console.log(ch.repeat(this.width));
    }
  }
}
module.exports = Square;
