#!/usr/bin/node
const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
}

const fact = factorial(num);
console.log(fact);

function factorial (a) {
  if (a <= 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}
