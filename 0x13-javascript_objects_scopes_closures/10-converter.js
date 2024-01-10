#!/usr/bin/node
// Script that prints “JavaScript is amazing”

exports.converter = function (base) {
  return (n) => n.toString(base);
};
