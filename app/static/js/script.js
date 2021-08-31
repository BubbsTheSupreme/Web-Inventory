function itemForm(status) {
    if(status === 1){
        document.getElementById('item').style.visibility = "visible";
        document.getElementById('item').style.display = "block";
    }
    else {
        document.getElementById('item').style.visibility = "hidden";
        document.getElementById('item').style.display = "none";
    }
}

function componentForm(status) {
    if(status === 1){
        document.getElementById('component').style.visibility = "visible";
        document.getElementById('component').style.display = "block";
    }
    else {
        document.getElementById('component').style.visibility = "hidden";
        document.getElementById('component').style.display = "none";
    }
}