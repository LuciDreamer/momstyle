$(document).ready(function () {
    $(".question").click(function (event) {
        event.preventDefault();
        console.log('jquery works')
        var answer = $(this).next()
        console.log(answer)
        answer.toggleClass("disp_none")
    })
})