#!/usr/bin/node

const Rectangle = require('./5-square'); // import the rectangle class
class Square extends Rectangle { // Write a class Square that defines a square and inherits from Rectangle
  constructor (size) { // The constructor must take 1 argument: size
    super(size, size); // The constructor of Rectangle must be called (by using super())
  }

  charPrint (c) { // prints the rectangle using the character c
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

// Export the class
module.exports = Square;
