var labels =  []
for(i = 0; i < 100; i++) {
	labels.push(""+i)
}
var labelIndex = 0;
var map;
function initMap() {
	
	var position = {lat: 47.768265941637964, lng: -1.1724274633209006};
	map = new google.maps.Map(document.querySelector('#geo'), {
	  zoom: 8,
	  center: position
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