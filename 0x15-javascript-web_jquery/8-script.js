$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (did) {
  $('#list_movies').append(did.results.map(data => `<li>${data.title}</li>`));
});
