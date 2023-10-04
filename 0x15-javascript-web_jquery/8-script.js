// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const $movies = $('ul#list_movies');

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: function (data) {
    $.each(data.results, function (i, movie) {
      $movies.append('<li>' + movie.title + '</li>');
    });
  }
});
