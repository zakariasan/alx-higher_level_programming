#!/usr/bin/node
// Script that computes and prints a factorial

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(process.argv.sort((a, b)=> a - b).reverse()[1]);
}
