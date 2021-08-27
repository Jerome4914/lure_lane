function initMap() {
    geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        {'address': document.getElementById("map_location").innerHTML},
        function (results, status) {
            if (status == 'OK') {
                const map = new google.maps.Map(document.getElementById("map"), {
                    zoom: 11,
                    center: results[0].geometry.location,
                    gestureHandling: "cooperative",
                    mapTypeId: 'satellite'
                });
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location,
                });
            } else {
                alert(
                    'Geocode was not successful for the following reason: ' + status
                );
            }
        }
    );
}
