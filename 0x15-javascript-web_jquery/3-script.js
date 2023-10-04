//updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header
$(document).on('click', '#red_header', function () {
    $('header').addClass('red');
});
