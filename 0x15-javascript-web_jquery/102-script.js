$(function () {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    if (languageCode) {
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, (data) => {
        $('#hello').text(data.hello);
      });
    }
  });
});
