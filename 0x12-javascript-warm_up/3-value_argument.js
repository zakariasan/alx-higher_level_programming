#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
