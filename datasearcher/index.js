const userCardTemplate = document.querySelector("[data-user-template]");
const userCardContainer = document.querySelector("[data-user-cards-container]");
const searchInput = document.querySelector("[data-search]");

let profiles = [];

function login(profile) {
    window.open(`https://intranet.tam.ch/ksl/rest/ics/type/timetable/date/1642582786/auth/${profile.hash}/calendar.ics`)
    if (confirm("A file is being downloaded. When done, press ok'")) {
        window.open("https://intranet.tam.ch")
    }
}

searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase();
    var notShowing = 0;
    profiles.forEach(profile => {
        const isVisible =
            profile.name.toLowerCase().includes(value) ||
            profile.id.toLowerCase().includes(value) ||
            profile.class.toLowerCase().includes(value) ||
            profile.hash.toLowerCase().includes(value) ||
            profile.rawName.toLowerCase().includes(value)
        profile.element.classList.toggle("hide", !isVisible)
        if (!isVisible) {
            notShowing += 1;
        }
    })

    if (profiles.length == notShowing) {
        document.getElementById("info-text").innerHTML = "No profiles found";
    } else {
        document.getElementById("info-text").innerHTML = "";
    }
})

fetch("https://genius1512.github.io/athene/files/data.json")
    .then(res => res.json())
    .then(data => ({
        ...data.students,
        ...data.teachers
    }))
    .then(function(data) {
        newData = [];

        for (const profile in data) {
            data[profile]["rawName"] = profile
            if (data[profile].class == undefined) {
                data[profile].class = "None"
            }
            newData.unshift(data[profile])
        }
        
        return newData;
    })
    .then(data => {
        profiles = data.map(profile => {
            const card = userCardTemplate.content.cloneNode(true).children[0]
            const header = card.querySelector("[data-header]")
            const body = card.querySelector("[data-body]")
            header.textContent = profile.rawName
            body.textContent = `Name: ${profile.name}
ID: ${profile.id}
Class: ${profile.class}
Hash: ${profile.hash}`

            if (!(profile.hash == "unknown")) {
                var loginButton = document.createElement("button");
                loginButton.id = "login-button";
                loginButton.className = "button";
                loginButton.innerHTML = "Login";
                loginButton.style.marginTop = ".25rem";
                loginButton.onclick = function() { login(profile) }
                card.appendChild(document.createElement("br"))
                card.appendChild(loginButton);
            }

            userCardContainer.append(card)
            return {
                name: profile.name,
                id: profile.id,
                class: profile.class,
                hash: profile.hash,
                rawName: profile.rawName,
                element: card
            }
        })
    })
