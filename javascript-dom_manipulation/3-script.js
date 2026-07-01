#!/usr/bin/node

const header = document.querySelector('#toggle_header');
header.addEventListener('click', function (e) {
  if (e.target.classList.contains('green')) {
    e.target.classList.remove('green');
    e.target.classList.add('red');
  } else {
    e.target.classList.add('green');
  }
});