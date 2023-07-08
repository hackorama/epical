function logs() {
    log = document.getElementById('epical');
    if (typeof(log) != 'undefined' && log != null) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                log.innerHTML = '<pre>' + xhr.responseText + '</pre>';
            }
        }
        xhr.open('GET', 'epical.log?' + Date.now());
        xhr.send();
    }
}

function check(url, callback) {
    var xhr = new XMLHttpRequest();
    var result = false
    xhr.onreadystatechange = function() {
        result = Boolean(xhr.readyState == 4 && xhr.status == 200)
        return(callback(result))
    }
    xhr.open('GET', url + "?" + Date.now()); // append timestamp to force no caching
    xhr.send();
}

function controls() {
    check('disable', function(r) {
        disable_button = document.getElementById('disable_button');
        if (r === true) {
            disable = document.getElementById('disable');
            disable.style.filter = "grayscale(0%)"
            disable_button.value = "Enable"
        } else {
            disable_button.value = "Disable"
        }
    });
    check('battery', function(r) {
        battery_button = document.getElementById('battery_button');
        if (r === true) {
            battery = document.getElementById('battery');
            battery.style.filter = "grayscale(0%)"
            battery_button.value = "Cancel"
        } else {
            battery_button.value = "Charge"
        }
    });
    var photo_found = false
    photo_button = document.getElementById('photo_button');
    photo_button.disabled = true
    check('photo.bmp', function(r) {
        if (r === true && photo_found === false ) {
            photo_found = true
            photo = document.getElementById('photo');
            photo.style.filter = "grayscale(0%)"

            preview = document.getElementById('preview');
            preview.innerHTML = "<img src=\"photo.bmp\" alt=\"photo preview\">"
            photo_button.disabled = false
        }
    });
    check('photo.png', function(r) {
        if (r === true && photo_found === false) {
            photo_found = true
            photo = document.getElementById('photo');
            photo.style.filter = "grayscale(0%)"

            preview = document.getElementById('preview');
            preview.innerHTML = "<img src=\"photo.png\" alt=\"photo preview\">"
            photo_button.disabled = false
        }
    });
    check('photo.jpeg', function(r) {
        if (r === true && photo_found === false) {
            photo_found = true
            photo = document.getElementById('photo');
            photo.style.filter = "grayscale(0%)"

            preview = document.getElementById('preview');
            preview.innerHTML = "<img src=\"photo.jpeg\" alt=\"photo preview\">"
            photo_button.disabled = false
        }
    });
    check('photo.jpg', function(r) {
        if (r === true && photo_found === false) {
            photo_found = true
            photo = document.getElementById('photo');
            photo.style.filter = "grayscale(0%)"

            preview = document.getElementById('preview');
            preview.innerHTML = "<img src=\"photo.jpg\" alt=\"photo preview\">"
            photo_button.disabled = false
        }
    });
    check('epical.tar', function(r) {
        package_button = document.getElementById('package_button');
        if (r === true) {
            package = document.getElementById('package');
            package.style.filter = "grayscale(0%)"
            package_button.disabled = false
        } else {
            package_button.disabled = true
        }
    });
}

function fileSelected() {
    upload_button = document.getElementById('upload_button');
    upload_button.disabled = false
}

function start() {
    controls();
    logs();
}