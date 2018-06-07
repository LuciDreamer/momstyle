$(document).ready(function () {
    $("#product-image").magnify();

    $(".cart-form").submit(function (e) {
        e.preventDefault();
        var form = $(this)
        var btn = $(this).find(".cart-btn");
        var product_id = btn.data("product_id");
        var quantity = $(this).find(".number-input").val();
        var size = $(".size-input option:selected").text();
        console.log(size)
        var data = {};
        data["product_id"] = product_id;
        data["quantity"] = quantity;
        data['size'] = size;

        var url = form.attr("action");
        console.log(data);
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            dataType: 'json',
            success: function (response) {
                var items = response["cart"]
                console.log(items)
                $(".items-count").html(items);
                console.log("passed")

            },
            error: function () {
		        console.log('Error')
	        }
        })

    });
    

    $(".description-link").each(function () {
        $(this).click(function (e) {
            e.preventDefault();
            $(this).addClass("active")
                .siblings().removeClass("active");


            var selector = $(this).attr("tab");

            $('#' + selector)
                .removeClass("d-none")
                .siblings().addClass("d-none");

        })

    })


})