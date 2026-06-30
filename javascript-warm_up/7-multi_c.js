#!/usr/bin/node

const argv = process.argv;
if (argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
