#!/usr/bin/node
const argv = process.argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(a, b));
