var jumbotron = document.getElementById("jumbotron");
//Image cycling function, setting the image to 1 with "if statement adding a
// 0 to the beginning of the number if less than 10.
// This also takes care of the CSS styling that was hard coded and enables
// the rotation of the images.
var i = 1;
var nextImage = function () {
		if(i < 10) {
			i = "0" + i;
		}

		imgSrc = "images/pdxcg_" + i + ".jpg";
    	document.getElementById("jumbotron").style.background = 'url(' + imgSrc + ')';
    	i++;
}

//a builtin interval calling the nextImage function that is set in milliseconds
setInterval(nextImage, 20000);