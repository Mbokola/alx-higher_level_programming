// adds the class red to the <header> element when the user clicks on the tag
$(document).on('click', '#update_header', function () {
  $('header').text('New Header!!!');
});
