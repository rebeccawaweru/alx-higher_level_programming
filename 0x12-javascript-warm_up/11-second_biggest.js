#!/usr/bin/node
const secondLarge = process.argv;
if (secondLarge.length <= 3) {
  console.log(0);
} else {
  console.log(secondLarge.sort((a, b) => b - a).slice(3)[0]);
}
