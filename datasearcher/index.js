function getJSON(url) {
    fetch('https://yesno.wtf/api')  
        .then(res => res.json())  
        .then((out) => {  
            return out;
        })  
        .catch(err => {  
            throw err  
    });
}

function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    var profilePre = document.getElementById("profile-text");

    profilePre.innerHTML(getJSON("https://genius1512.github.io/athene/files/data.json"))
}