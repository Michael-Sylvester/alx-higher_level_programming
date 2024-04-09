#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let rect = '';

    for (i = 0; i < this.width; i++) {
      rect += 'x';
    }

    for (i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
