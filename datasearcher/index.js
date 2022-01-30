function fetchSite(url) {
    var xhr = new XMLHttpRequest();

    xhr.open('GET', url, false);

    try {
        xhr.send();
        if (xhr.status != 200) {
            console.error(xhr.status + "/" + xhr.statusText);
            return null
        } else {
            return xhr.response
        }
    } catch(err) {
        console.error("Request failed");
        return "Failed"
    }
}

function search() {
    var searchTerm = document.getElementById("search-term-input").value;

    var resp = fetchSite(searchTerm);    
    console.log(typeof(resp));
    console.log(resp);
}
