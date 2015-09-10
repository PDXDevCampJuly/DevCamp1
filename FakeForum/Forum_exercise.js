///**
// * Created by summerlynbryant on 9/8/15.
// */
//
//var form = document.getElementsByClassName('Post_it');
//console.log(form.value);

var form = document.getElementById("post");



/* Post the form info to the forum on submit. */
function formInput(e) {
    e.preventDefault();
    var post_title = e.target.querySelector("[name=post_title]");
    var post_thoughts = e.target.querySelector("[name=post_thoughts]");
    var entries ={
        "entry_434124687": post_title.value,
        "entry_1823097801": post_thoughts.value
    };

    console.log("Just say you love me");
    $.post("https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",entries,onload);

    onload = function () {
        console.log("Give in to me!");
        if (xhr.status === 200) {


        }
    };

 }

/* Get the posts on the forum and add them to the page. */

$.ajax({
    type: "GET",
    url: "https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
    dataType : "jsonp",
    complete: function (data) {
            console.log(data);
            console.log(data.responseJSON.feed);
            // I want to get the array from the entry
            //console.log(data.responseJSON.feed.entry);
            var dataFeed = data.responseJSON.feed.entry;
            dataFeed.reverse();
            for (var i = 0; i < dataFeed.length; i++) {

                var feedBody = dataFeed[i].gsx$postbody.$t;
                var feedTitle = dataFeed[i].gsx$posttitle.$t;

                var postString = "<li>" + feedBody + '<br>' + feedTitle + "</li>";

                $("#output").append(postString);
            }
                // and loop through it



            }


});

//$.get("https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
//    function (e) {
//    console.log("Get callback");
//    $("#output").html(e);
//});

form.addEventListener("submit", formInput, false);
console.log("I believe in a thing called love");