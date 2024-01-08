#!/usr/bin/node
// script that prints x times “C is fun”

if (process.argv.length === 3) {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    let sq = '';
    for (let y = 0; y < parseInt(process.argv[2]); y++) {
      sq = sq + 'X';
    }
    console.log(sq);
  }
} else {
  console.log('Missing size');
}
