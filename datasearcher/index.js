function fetchSite(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.send();

    xhr.onload = function() {
        if (xhr.status != 200) {
            console.error("Error " + xhr.status + ": " + xhr.statusText);
        } else {
            return xhr.response;
        }
    }
}

function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    console.log(typeof(fetchSite(searchTerm)));
}
