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

  print () { // Create an instance method called print()
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X'; // using the character X
      }
      console.log(line); //  prints the rectangle
    }
  }

  rotate () { // exchanges the width and the height of the rectangle
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () { // multiplies the width and the height of the rectangle by 2
    this.height *= 2;
    this.width *= 2;
  }
}
// Export the class, refer to task 0
module.exports = Rectangle;
