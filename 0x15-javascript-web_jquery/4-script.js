//updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header
$(document).on('click', '#toggle_header', function () {
    var header = $('header');
    if (header.hasClass('red')) {
        header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
        header.removeClass('green').addClass('red');
    } else {
        header.addClass('red');
    }
});
