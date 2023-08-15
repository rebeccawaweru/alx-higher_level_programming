#!/usr/bin/node
let y = 0;
exports.logMe = function (item) {
  console.log(y + ': ' + item);
  y++;
};
