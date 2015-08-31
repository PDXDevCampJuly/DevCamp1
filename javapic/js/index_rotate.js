var jumbotron = document.getElementById("jumbotron");
//Image cycling function
var i = 1;
var nextImage = function () {
		if(i < 10) {
			i = "0" + i;
		}

		imgSrc = "images/pdxcg_" + i + ".jpg";
    	document.getElementById("jumbotron").style.background = 'url(' + imgSrc + ')';
    	i++;
}

setInterval(nextImage, 20000);