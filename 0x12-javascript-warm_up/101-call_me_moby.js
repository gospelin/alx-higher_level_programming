#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
};
