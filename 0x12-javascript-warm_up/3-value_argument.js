#!/usr/bin/node
const numArgs = process.argv;

if (numArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(numArgs[2]);
}
