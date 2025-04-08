function loadDoc(url, func) {
    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if (xhttp.status != 200) {
            console.log("Error");
        } else {
            func(xhttp.response);
        }
    }
    xhttp.open("GET", url);
    xhttp.send();

}

function upload_file() {
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        if (xhttp.status != 200) {
            console.log("Error");
        } else {
            list_files();
        }
    }

    var formData = new FormData();
    formData.append("file", document.getElementById("file").files[0]);
    formData.append("caption", document.getElementById("caption").value);

    xhttp.open("POST", "/example/uploadfile", true);
    xhttp.send(formData);
}

function list_files() {
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        if (xhttp.status != 200) {
            console.log("Error");
        }
        else {
            responseParse(xhttp.response)
        }
    };

    xhttp.open("GET", "/example/listfiles");
    xhttp.send();
}


function responseParse(response){
    var data = JSON.parse(response);
        var items = data.items;
        var url = data.url;

        var temp = "";
        for (var i = 0; i < items.length; i++) {
            temp += "<div class='image-card'>";
            temp += "<img src='" + url + items[i].filename + "' />";
            temp += "<div class='caption'>" + items[i].caption + "</div>";
            temp += "</div>";
        }

        document.getElementById("divResults").innerHTML = temp;
}
console.log("Script Loaded")








