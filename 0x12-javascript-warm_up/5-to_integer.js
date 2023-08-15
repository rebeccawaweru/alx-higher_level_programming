#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (Number.isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argument);
}
