const upload = function(picklist_name){
    document.getElementById('picklist_name').value = picklist_name;
    document.getElementById('selected_file').click();
};

const on_file_chooser_close = function(){
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
