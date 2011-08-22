//Useful links:
// http://code.google.com/apis/maps/documentation/javascript/reference.html#Marker
// http://code.google.com/apis/maps/documentation/javascript/services.html#Geocoding
// http://jqueryui.com/demos/autocomplete/#remote-with-cache

var geocoder;
var map;
var marker;

function initialize(){
    //MAP
    var latlng = new google.maps.LatLng(41.659,-4.714);
    var options = {
        zoom: 16,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };

    map = new google.maps.Map(document.getElementById("map_canvas"), options);

    //GEOCODER
    geocoder = new google.maps.Geocoder();

    marker = new google.maps.Marker({
        map: map,
           draggable: true
    });

}
// address_component selection
function find(components, item) {
    for(var j=0;j < components.length; j++){
        for(var k=0; k < components[j].types.length; k++){
            if(components[j].types[k] == item){
                return components[j].long_name;
            }
        }
    }
};

    $(document).ready(function() { 

        initialize();

        $(function() {
            $("#address").autocomplete({
                //This bit uses the geocoder to fetch address values
                source: function(request, response) {
                    geocoder.geocode( {'address': request.term }, function(results, status) {
                        response($.map(results, function(item) {
                            return {
                                label:  item.formatted_address,
                            value: item.formatted_address,
                            components: item.address_components,
                            location_type: item.geometry.location_type,
                            latitude: item.geometry.location.lat(),
                            longitude: item.geometry.location.lng()
                            }
                        }));
                    })
                },

                //This bit is executed upon selection of an address
                select: function(event, ui) {
                    $("#lat").val(ui.item.latitude);
                    $("#lng").val(ui.item.longitude);
                    $("#country").val(find(ui.item.components, "country"));
                    $("#locality").val(find(ui.item.components, "locality"));
                    $("#route").val(find(ui.item.components, "route"));
                    $("#street_number").val(find(ui.item.components, "street_number"));
                    $("#postal_code").val(find(ui.item.components, "postal_code"));
                    $("#state").val(find(ui.item.components, "administrative_area_level_1"));
                    $("#location_type").val(ui.item.location_type);
                    var location = new google.maps.LatLng(ui.item.latitude, ui.item.longitude);
                    marker.setPosition(location);
                    map.setCenter(location);
                }
            });
        });

        //Add listener to marker for reverse geocoding
        google.maps.event.addListener(marker, 'drag', function() {
            geocoder.geocode({'latLng': marker.getPosition()}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    if (results[0]) {
                        $('#address').val(results[0].formatted_address);
                        $('#country').val(find(results[0].address_components, "country"));
                        $('#locality').val(find(results[0].address_components, "locality"));
                        $('#street_number').val(find(results[0].address_components, "street_number"));
                        $('#postal_code').val(find(results[0].address_components, "postal_code"));
                        $('#route').val(find(results[0].address_components, "route"));
                        $('#state').val(find(results[0].address_components, "administration_area_level_1"));
                        $('#lat').val(marker.getPosition().lat());
                        $('#lng').val(marker.getPosition().lng());
                        $('#location_type').val(results[0].geometry.location_type);
                    }
                }
            });
        });

    });
