function checkItem(element) {
    var checkedLabel = element.parentElement.querySelector("label");
    checkedLabel.classList.toggle("to-be-removed");
}

function verifyAdd() {
    var newItem = document.getElementById("new-item");
    var addButton = document.getElementById("add-btn");
    addButton.disabled = newItem.value === "";
}
