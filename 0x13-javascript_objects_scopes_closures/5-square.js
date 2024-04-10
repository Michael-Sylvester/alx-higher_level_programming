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
      rect += 'X';
    }

    for (i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
