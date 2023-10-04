// adds a <li> element to a list when the user clicks on the tag DIV#add_item:
$(document).on('click', '#add_item', function () {
  $('.my_list').append('<li>Item</li>');
});
