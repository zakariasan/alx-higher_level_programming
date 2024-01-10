#!/usr/bin/node
// Script that prints “JavaScript is amazing”

exports.nbOccurences = function (list, searchElement) {
  return (list.filter((item) => item === searchElement).length);
};
