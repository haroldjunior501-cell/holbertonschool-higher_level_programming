document.querySelector('#add_item').addEventListener('click', function () {
  var li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
});
