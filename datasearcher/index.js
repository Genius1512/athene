const profileTemplate = document.getElementById("profile-template");
const profilesContainer = document.getElementById("profiles-container");
const searchInput = document.getElementById("search-input");

let profiles;

// fetch json data
async function getProfiles() {
    let response = await fetch("https://genius15125.github.io/athene/files/data.json");

    var json;
    if (response.ok) {
        json = response.json();
    } else {
        console.error("HTTPError: " + response.status);
    }

    return json;
}

async function getData() {
    profiles = await getProfiles();
}
getData();
