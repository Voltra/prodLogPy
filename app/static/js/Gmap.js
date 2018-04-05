var labels =  []
for(i = 0; i < 100; i++) {
	labels.push(""+i)
}
var labelIndex = 0;
var map;
function initMap() {
	
	var Paris = {lat: 46.628213227315086, lng: 2.584222859375018};
	map = new google.maps.Map(document.querySelector('#geo'), {
	  zoom: 6,
	  center: Paris
	});
	
	 google.maps.event.addListener(map, 'click', function(event) {
     	addMarker(event.latLng, map);
     });	
}

function getMap() {	
	return map;
}

function addMarker(location, title, map) {
        // Add the marker at the clicked location, and add the next-available label
        // from the array of alphabetical characters.
        var marker = new google.maps.Marker({
          position: location,
          label: labels[labelIndex++ % labels.length],
			title: title,
          map: map
        });
      }