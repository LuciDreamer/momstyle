$(document).ready(function () {
    var first_slide = $(".card:first")
    first_slide.removeClass("d-none")

    $(".controller").click(function () {
        var present_slide = first_slide;
        console.log("present slide", present_slide)

        if ($(this).hasClass("previous")){
            console.log("previous works")

        }else{
            present_slide.animate({opacity: 0}, 1000)
            present_slide.addClass("d-none")

            var next_slide = present_slide.next();
            console.log("next slide", next_slide);
            next_slide.removeClass("d-none");
        }
        present_slide = present_slide.next();

    });
})