function fetchSite(url) {
    var xhr = new XMLHttpRequest();

    xhr.open('GET', url, true);

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

var data;
fetchSite("/athene/files/data.json", function(content) {
    data = content;
})

function search() {
    var searchTerm = document.getElementById("search-term-input").value;

    var mode;
    if (3 <= searchTerm.length && searchTerm.length <= 4) {
        mode = "teachers";
    } else {
        mode = "students";
    }

    var profileText;
    if (data[mode][searchTerm] === undefined) {
        profileText = "Profile not found\nHere are some profiles containing your search:\n";
        for (const key in data["students"]) {
            for (const attribute in data["students"][key]) {
                if (data["students"][key][attribute].includes(searchTerm)) {
                    profileText += "    " + key + "\n";
                }
            }
            if (key.includes(searchTerm)) {
                profileText += "    " + key + "\n";
            }
        }
        for (const key in data["teachers"]) {
            for (const attribute in data["teachers"][key]) {
                if (data["teachers"][key][attribute].includes(searchTerm)) {
                    profileText += "    " + key + "\n";
                }
            }
            if (key.includes(searchTerm)) {
                profileText += "    " + key + "\n";
            }
        }

    } else {
        profileText = searchTerm + "'s profile:\n";
    for (const key in data[mode][searchTerm]) {
        profileText += "    " + key + ": " + data[mode][searchTerm][key] + "\n";
    }
    }
    document.getElementById("profile-text").innerHTML = profileText;
}
