/**
 * Created by summerlynbryant on 8/28/15.
 */


function captureForm() {
    // do some stuff with the values in the form
    // stop form from being submitted
}


<


function emailValidate(el) {
    var valid = /[^@] +@[^@]+/.test(el.value);
    if (!valid) {
        setErrorMessage(el,
            "You have entered an invalid email. Please enter a valid email address");
    }
    return valid;
}
