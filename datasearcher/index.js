function fetchJSON(url) {
    xhr = new XMLHttpRequest();
    xhr.open("GET", url, false);
    try {
        xhr.send()
        if (xhr.status != 200) {
            console.error(xhr.status + "/" + xhr.statusText);
        } else {
            return JSON.parse(xhr.response);
        }
    } catch(err) {
        console.error("Request failed");
    }
}

var data = fetchJSON("https://genius1512.github.io/athene/files/data.json");

function getProfileText(mode, identifier) {
    var text = `${identifier}'s profile:\n`;
    for (const key in data[mode][identifier]) {
        text += `    ${key}: ${data[mode][identifier][key]}\n`;
    }
    return text;
}

function listProfiles(term) {
    var text = "Search results:\n";
    for (const student in data.students) {
        for (const attribute in data.students[student]) {
            if (data.students[student][attribute].includes(term)) {
                text += student + "\n";
            }
        }
        if (student.includes(term)) {
            text += student + "\n";
        }
    }
    for (const teacher in data.teachers) {
        for (const attribute in data.teachers[teacher]) {
            if (data.teachers[teacher][attribute].includes(term)) {
                text += teacher + "\n";
            }
        }
        if (teacher.includes(term)) {
            text += teacher + "\n";
        }
    }
    return text;
}

function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    if (searchTerm === "") {
        return;
    }
    var mode = (function(term) {
        if (term.length <= 4) {
            return "teachers";
        } else {
            return "students";
        }
    })(searchTerm);

    var content;
    if (!(searchTerm in data[mode])) {
        content =  listProfiles(searchTerm);
    } else {
        content = getProfileText(mode, searchTerm);
    }
    document.getElementById("profile-text").innerHTML = content;
}
