function fetchSite(url) {
    var xhr = new XMLHttpRequest();
    xhr.responseType = "json";

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            return xhr.responseText;
        }
    }
    xhr.open("GET", url);
    xhr.send();
}

function search() {
    var searchTerm = document.getElementById("search-term-input").value;

    var resp = fetchSite(searchTerm);    
    console.log(typeof(resp));
    console.log(resp);
}
