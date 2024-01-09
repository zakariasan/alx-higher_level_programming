#!/usr/bin/node
// Script that computes and prints a factorial

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const pr = process.argv.sort().reverse();
  console.log(pr[1]);
}
