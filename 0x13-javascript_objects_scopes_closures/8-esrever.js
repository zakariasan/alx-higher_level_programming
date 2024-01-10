#!/usr/bin/node
// Script that prints “JavaScript is amazing”

exports.esrever = function (list) {
  const ret = [];
  for (let item = list.length - 1; item >= 0; item--) {
    ret.push(list[item]);
  }
  return list.reverse();
};
