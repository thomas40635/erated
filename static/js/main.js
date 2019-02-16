$(document).ready(function () {
    var body = $('body');

    $('#dynamicBackground').hide();

    body.on("mouseenter", "[data-movie-hover]", function () {
        var dynamicBackground = $('#dynamicBackground');
        dynamicBackground.fadeIn(500);
        document.getElementById("dynamicBackground").src = this.getAttribute("data-movie-hover");
    });

    // body.on("mouseleave", "[data-movie-hover]", function () {
    //     var dynamicBackground = $('#dynamicBackground');
    //     dynamicBackground.fadeOut(500);
    //     document.getElementById("dynamicBackground").src = "";
    // });

});