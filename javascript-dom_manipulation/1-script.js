#!/usr/bin/node

const header = document.querySelector('#red_header');
header.addEventListener('click', function (e) {
  e.target.style.color = '#FF0000';
});