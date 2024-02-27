function check_me(element) {
    var checked_label = element.parentElement.querySelector("label");
    checked_label.classList.toggle("to-be-removed");
}
