#!/usr/bin/node
const firstNum = Number(process.argv[2]);
const secondNum = Number(process.argv[3]);

// if (isNaN(firstNum) || isNaN(secondNum)) {
//  console.log('NaN');
// }

add(firstNum, secondNum);

function add (a, b) {
  console.log(a + b);
}
