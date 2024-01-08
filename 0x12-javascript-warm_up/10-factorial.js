#!/usr/bin/node
// Script that computes and prints a factorial

function fact (nbr) {
  if (isNaN(nbr) || nbr === 0) {
    return (1);
  }
  return (fact(nbr - 1) * nbr);
}

console.log(fact(parseInt(process.argv[2])));
