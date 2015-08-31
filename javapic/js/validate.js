/**
 * Created by summerlynbryant on 8/28/15.
 */

var form = document.getElementById('signup');

function formValidate(e) {
    e.preventDefault();
    var name = e.target.querySelector("[name=name]");
    if (name.value < 1) {
        alert("You're close, but give me a little something.");
        return false;
        }
    var username = e.target.querySelector("[name=username]");
    if (username.value < 1) {
        alert(" At least one letter is all I need!");
        return false;
    }

    var email = e.target.querySelector("[name=email]");
    var regex = /[^@] +@[^@]+/;
    var valid = regex.test(email.value);
    if (!valid) {
        alert("An invalid email, you have entered. Enter a valid email");
        return false;
    }

    sessionStorage.setItem("name", name.value);
    document.location.href="http://localhost:63342/untitled/javapic/gallery.html";
}

form.addEventListener("submit",formValidate,false);

