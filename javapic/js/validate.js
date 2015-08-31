/**
 * Created by summerlynbryant on 8/28/15.
 */

function captureForm() {
    // do some stuff with the values in the form
    // stop form from being submitted
}



var email = document.getElementsByName('email').value;
var submit = document.getElementById('submit');

function emailValidate(email) {
    var regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    var valid = regex.test(email);
    if (!valid) {
        alert("You have entered an invalid email. Please enter a valid email address.");
        return false;
    }
    return true;
}

submit.onsubmit = emailValidate(email);







