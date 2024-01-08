#!/usr/bin/node
// script that prints x times “C is fun”

function add (a, b) {
  return (a + b);
}

if (process.argv.length === 4) {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
} else {
  console.log('NaN');
}
