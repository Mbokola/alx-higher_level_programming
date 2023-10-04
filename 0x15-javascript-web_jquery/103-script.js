$(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {  // Enter key pressed
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    if (languageCode) {
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, (data) => {
        $('#hello').text(data.hello);
      });
    }
  }
});
