function search() {
    var searchTerm = document.getElementById("search-term-input").value;
    alert(searchTerm);
}

var enterbutton = document.getElementById("enter");
enterbutton.onclick = search;