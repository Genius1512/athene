function getJSON(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url)
    xhr.send()

    xhr.onload = function() {
        if (xhr.status != 200) { // analyze HTTP status of the response
            alert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
        } else { // show the result
            alert(`Done, got ${xhr.response.length} bytes`); // response is the server response
            console.log(xhr.response)
        }
    };
}


function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    var profilePre = document.getElementById("profile-text");
    var url = "/athene/files/data.json";

    console.log(getJSON(searchTerm));
}
