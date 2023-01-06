#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 1; i <= this.height; i++) {
        let row = '';
        for (let j = 1; j <= this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
