async function getJSON(url) {
    let response = await fetch(url);

    var json;
    if (response.ok) {
        json = response.json();
    } else {
        console.error("HTTPError: " + response.status);
    }

    return json;
}

var data;
async function getData() {
    data = await getJSON("https://genius1512.github.io/athene/files/data.json");
}
getData();

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
