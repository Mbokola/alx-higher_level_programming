//fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
$(function  () {
    $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        dataType: 'json',
        success: function (data) {
            $('#hello').text(data.hello);
        }
    });
});
