#!/usr/bin/node

const squareParent = require('./5-square');

class Square extends squareParent {
  charPrint (c = 'X') {
    let i;
    let rect = '';

    for (i = 0; i < this.width; i++) {
      rect += c;
    }

    for (i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }
}
module.exports = Square;
