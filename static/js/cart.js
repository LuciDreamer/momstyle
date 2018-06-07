$(document).ready(function () {
    $(".decrease").click(function () {
        var line = $(this).parent().parent()
        var quantity = Number(line.find(".quantity-input").val());
        var url = $(this).attr("data-url");
        var id = $(this).attr("data-id");
        var size = $(this).attr("data-size");
        data = {};
        data['product-id'] = id;
        data['action'] = 'decrease';
        data['size'] = size

        if (quantity == 1) {
            line.find(".quantity-input").val(quantity);
        } else {
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function (response) {
                    var total_price = response["total_price"];
                    var new_quantity = quantity - 1;
                    line.find(".quantity-input").val(new_quantity);
                    $(".total-price").html(total_price);
                },
                error: function () {
                    console.log('Error');
                }
            })
        }
    })

        $(".increase").click(function () {
        var line = $(this).parent().parent();
        var quantity = Number(line.find(".quantity-input").val());
        var url = $(this).attr("data-url");
        var id = $(this).attr("data-id");
        var size = $(this).attr("data-size");
        console.log(size)
        data  = {}
        data['product-id'] = id
        data['action'] = 'increase';
        data['size'] = size

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                var total_price = response["total_price"];
                var new_quantity = quantity + 1;
                line.find(".quantity-input").val(new_quantity);
                $(".total-price").html(total_price);
            },
            error: function () {
                console.log('Error')
            }
        })
    })

    $(".delete-item").on('click', function (e) {
        e.preventDefault()
        var line = $(this).parent().parent()
        console.log(line)
        var items = Number($(".items-count").html());
        var product_id = $(this).attr("data-id");
        var size = $(this).attr("data-size");
        var data = {}
        data["product_id"] = product_id
        data["size"] = size

        $.ajax({
            url: $(this).attr("href"),
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                var total_price = response["total_price"];
                line.hide()
                $(".total-price").html(total_price)
                $(".items-count").html(items - 1)

            },
            error: function () {
                console.log('Error')
            }
        });
    });

    $(".pre_order").click(function (event) {
        event.preventDefault()
        var items = Number($(".items-count").html());
        if(items == 0){

        }else{
            $(".modal-container").css({"display": "flex"});
        }

    })

    $(".close-btn").click(function (event) {
        event.preventDefault();
        $(".modal-container").css({"display": "none"});
    })

    $(".order-btn").click(function (event) {
        event.preventDefault();

        var name = $(".input-name").val()
        var phone = $(".input-phone").val()
        url = $(this).attr("href")
        data = {}
        data['name'] = name;
        data['phone'] = phone;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function (response) {
                console.log("success");
                $(".modal-container").css({"display": "none"});

            },
            error: function () {
                console.log('Error')
            }

        });

    })

});