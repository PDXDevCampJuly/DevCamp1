/**
 * Created by summerlynbryant on 8/28/15.
 */

var el = document.querySelector(".tagline");
console.log(el);
var welcome = el.textContent;
var galleryGreeting = "develop something beautiful, ";
var name = sessionStorage.getItem("name");
el.textContent = galleryGreeting + name;


var gallery = document.getElementById('gallery');

var generateGallery = function () {
	var galleryHTML = '<ul>';

	for (i = 1; i <= 60; i++) {

		if (i < 10) {
			i = "0" + i;
		}
		galleryHTML += '<li>';
		galleryHTML += '<a href="images/pdxcg_';
		galleryHTML += i + '.jpg" data-lightbox="gallery">';
		galleryHTML += '<img src="images/pdxcg_';
		galleryHTML += i + '.jpg">';
		galleryHTML += '</a></li>';
	}

	galleryHTML += '</ul>';
	gallery.innerHTML = galleryHTML;
};

generateGallery();