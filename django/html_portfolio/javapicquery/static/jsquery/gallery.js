/**
 * Created by summerlynbryant on 8/28/15.
 */

var el = document.querySelector(".tagline");
console.log(el);
var welcome = el.textContent;
var galleryGreeting = "develop something beautiful, ";
var name = sessionStorage.getItem("name");
el.textContent = galleryGreeting + name;

var imageList =[];
var imageMax = 60;
var $gallery = $(".gallery");
var $div = $("#image_show");
var $divChild = $("#image_show > img");

// making a FOR loop to make the image names
for (i = 1; i <= imageMax; i++) {
	if (i < 10) {
		imageList.push("../static/images/pdxcg_0" + i + ".jpg");
	}
	else {
		imageList.push("../static/images/pdxcg_" + i + ".jpg");
	}
}
//console.log(imageList);
// this going to create the gallery
var items = [];
$.each(imageList, function(i, item){
	items.push("<li><img src=" + item + "></li>");
});
$gallery.append(items);
//page 328
$gallery.on("click", function(e) {
	$("#image_show").removeClass("display_none").addClass("display_img");
	$divChild.attr("src", e.target.src);
console.log(e)
});
$div.on("click", function() {
	$div.addClass("display_none");
});
$divChild.on("click", function(e){
	e.stopPropagation();
});