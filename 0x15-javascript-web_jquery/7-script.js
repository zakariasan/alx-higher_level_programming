$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(did){
	$('#character').text(did.name);
});
