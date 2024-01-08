#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let t = 0; t < x; t++) {
    theFunction();
  }
};
