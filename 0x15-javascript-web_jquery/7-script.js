// adds the class red to the <header> element when the user clicks on the tag
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: function (data) {
    $('#character').text(data.name);
  }
});
