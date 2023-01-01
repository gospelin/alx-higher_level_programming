#!/usr/bin/node
const num = Number(process.argv[2]);
const fact = factorial(num);
console.log(fact);

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}
