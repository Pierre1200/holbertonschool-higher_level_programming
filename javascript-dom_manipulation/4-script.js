#!/usr/bin/node

const AddLi = document.createElement('li');
AddLi.textContent = 'Item';

const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const ul = document.querySelector('.my_list');
  ul.appendChild(AddLi);
});