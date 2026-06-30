#!/usr/bin/node

const argv = process.argv;
const num = parseInt(argv[2]);
function facto (int) {
  if (isNaN(int) || int === 0) {
    return 1;
  } else {
    return int * facto(int - 1);
  }
}
console.log(facto(num));
