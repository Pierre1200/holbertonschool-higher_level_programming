#!/usr/bin/node
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const helloDiv = document.getElementById('hello');
    helloDiv.textContent = data.hello;
  });