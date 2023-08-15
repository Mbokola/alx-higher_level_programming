#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // import the rectangle class
class Square extends Rectangle { // Write a class Square that defines a square and inherits from Rectangle
  constructor (size) { // The constructor must take 1 argument: size
    super(size, size); // The constructor of Rectangle must be called (by using super())
  }
}
// Export the class
module.exports = Square;
