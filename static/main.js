function upload(picklist_name){
    document.getElementById('picklist_name').value = picklist_name;
    document.getElementById('selected_file').click();
};

function on_file_chooser_close(){
    var form = document.getElementById('file-form');
    var formData = new FormData(form);
    var fileSelect = document.getElementById('selected_file');
    var files = fileSelect.files;

    // Loop through each of the selected files.
    for (var i = 0; i < files.length; i++) {
        var file = files[i];

        // Check the file type.
        if (file.type.match('text.*,.csv')) {
            continue;
        }

        formData.append('file', file, file.name);
    }

    formData.append('csrf_token', window.csrf_token);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', window.upload_picklist_url, true);
    xhr.onload = function () {
        if (xhr.status !== 200) {
            response = JSON.parse(xhr.response)
            alert(response['error']);
        }
        window.location = window.admin_settings_url
    };

    xhr.send(formData);
};


var map;
var marker;


function initJobLocationMap() {
    // set up the map
    map = new L.Map('mapid');

    // create the tile layer with correct attribution
    var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib = 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 12, attribution: osmAttrib});

    map.setView(new L.LatLng(55.952141, -3.189296), 9);
    map.addLayer(osm);

    map.on('click', onMapClick);

    createMarkerFromFields();
}

function createMarker(latlng) {
    if (marker == null) {
        marker = L.marker(latlng).addTo(map);
    }
    marker.setLatLng(latlng);
    map.setView(latlng, 9);
}

function createMarkerFromFields() {
    createMarker({
        'lat': $('#latitude').val(),
        'lng': $('#longitude').val()
    })
}

function onMapClick(e) {
    document.getElementById('latitude').value = e.latlng.lat;
    document.getElementById('longitude').value = e.latlng.lng;
    createMarker(e.latlng);
}

function get_location_from_postcode() {
    var postcode = $('#postcode').val();

    $.get('/postcode/' + postcode).done(
        function (response) {
            $('#latitude').val(response.latitude);
            $('#longitude').val(response.longitude);
            $('#admin_district').val(response.admin_district);
            latLng = new L.LatLng(response.latitude, response.longitude);
            createMarker(latLng)
        }
    );
}

function initUploadLogo(redirect_url, upload_url) {

    function onSubmit(e) {
        var formData = new FormData(form);
        var fileSelect = document.getElementById('file-select');
        var files = fileSelect.files

        // Loop through each of the selected files.
        for (var i = 0; i < files.length; i++) {
            var file = files[i];

            // Check the file type.
            if (file.type.match('image.*')) {
                continue;
            }

            formData.append('file', file, file.name);
        }

        formData.append('csrf_token', window.csrf_token);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', upload_url, true);
        xhr.onload = function () {
            if (xhr.status !== 200) {
                response = JSON.parse(xhr.response);
                alert(response['error']);
            }
            window.location = redirect_url;
        };

        xhr.send(formData);

        e.preventDefault();
        return false;
    }

    var form = document.getElementById('file-form');
    form.onsubmit = onSubmit;
}
