function getJSON(url) {
    var out = "";
    fetch(url)
        .then(function(resp) {
            return resp.json()
        })
        .then(function(data) {
            out = data;
        })

    return out
}


function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    var profilePre = document.getElementById("profile-text");
    var url = "http://genius1512.github.io/athene/files/data.json";

    console.log(getJSON(url));
}
