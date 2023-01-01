#!/usr/bin/node
let num = process.argv.slice(2);
const numArgs = process.argv.length - 2;

if (numArgs === 0 || numArgs === 1) {
  console.log(0);
} else {
  num = num.sort(function (a, b) { return b - a; });
  console.log(num[1]);
}
