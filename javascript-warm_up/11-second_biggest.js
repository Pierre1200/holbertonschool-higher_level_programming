#!/usr/bin/node

const argv = process.argv;
const numbers = argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  const uniqueNumbers = [...new Set(numbers)];
  uniqueNumbers.sort((a, b) => b - a);
  console.log(uniqueNumbers[1]);
}
