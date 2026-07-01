#!/usr/bin/node

const UpdateHeader = document.querySelector('#update_header');
UpdateHeader.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});