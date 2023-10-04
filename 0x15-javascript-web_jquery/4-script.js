//adds a <li> element to a list when the user clicks on the tag DIV#add_item:
$(document).on('click', '#toggle_header', function () {
  const header = $('header');
  if (header.hasClass('red')) {
    header.removeClass('red').addClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('green').addClass('red');
  } else {
    header.addClass('red');
  }
});
