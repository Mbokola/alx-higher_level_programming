#!/usr/bin/node

class Rectangle { // Write a class Rectangle
  constructor (w, h) { // The constructor must take 2 arguments w and h
    if (w > 0 && h > 0) { // If both w and h are positive integers
      this.width = w; // Initialize the instance attribute width with the value of w
      this.height = h; // Initialize the instance attribute height with the value of h
    }
    /*
          If w or h is equal to 0 or not a positive integer, no attributes will be set
          resulting in an "empty" object.
        */
  }
}
// Export the class, refer to task 0
module.exports = Rectangle;
