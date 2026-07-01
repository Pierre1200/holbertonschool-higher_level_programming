#!/usr/bin/node

const header = document.querySelector('#red_header');
header.addEventListener('click', function (e) {
  e.target.classList.add('red');
});