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

var data = JSON.parse(fetchSite("/athene/files/data.json"));

function search() {
    var searchTerm = document.getElementById("search-term-input").value;

    var mode;
    if (3 < searchTerm.length < 4) {
        mode = "students";
    } else {
        mode = "teachers";
    }

    var profileText = searchTerm + "'s profile:\n";
    for (const key in data[mode][searchTerm]) {
        profileText += "    " + key + ": " + data[mode][searchTerm] + "\n";
    }
    document.getElementById("profile-text").innerHTML = profileText;

}
