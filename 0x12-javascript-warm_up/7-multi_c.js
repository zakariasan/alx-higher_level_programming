#!/usr/bin/node
// script that prints x times “C is fun”

if (process.argv.length === 3) {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
}
