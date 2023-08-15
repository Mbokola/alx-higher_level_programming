#!/usr/bin/node

class Rectangle { // Write a class Rectangle using class notation.
  constructor (w, h) { // The constructor must take 2 arguments w and h
    this.width = w; // Initialize the instance attribute width with the value of w
    this.height = h; // Initialize the instance attribute height with the value of h
  }
}

// Export the class, refer to task 0
module.exports = Rectangle;
