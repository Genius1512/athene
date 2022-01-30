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

function checkForEnter(event) {
    if (event.KeyCode == 13) {
        document.getElementById("enter").onclick();
    }
}

var data = JSON.parse(fetchSite("/athene/files/data.json"));

function search() {
    var searchTerm = document.getElementById("search-term-input").value;

    var mode;
    if (3 <= searchTerm.length <= 4) {
        mode = "teachers";
    } else {
        mode = "students";
    }

    var profileText;
    if (data[mode][searchTerm] === undefined) {
        profileText = "Profile not found";
    } else {
        profileText = searchTerm + "'s profile:\n";
    for (const key in data[mode][searchTerm]) {
        profileText += "    " + key + ": " + data[mode][searchTerm][key] + "\n";
    }
    }
    document.getElementById("profile-text").innerHTML = profileText;
}
