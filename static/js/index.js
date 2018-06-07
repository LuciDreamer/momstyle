$(document).ready(function () {
    $(".question").click(function (event) {
        event.preventDefault();
        $(this).next().toggleClass("d-none");
    })
})