
// Total Price calculation
$(document).ready(function() {
    var quantityInput = $('#id_quantity');
    var priceInput = $('#id_price');
    var totalInput = $('#id_total_price');
  
    // Calculate the total price on form field changes
    $('#productForm').on('input', function() {
      var quantity = parseFloat(quantityInput.val()) || 0;
      var price = parseFloat(priceInput.val()) || 0;
      var total = quantity * price;
  
      totalInput.val(total.toFixed(2));
    });
});


function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}


// $(document).ready(function () {
//   $('.increment-btn').click(function (e) {
//     e.preventDefault();

//     var inc_value = $(this).closest('.product_data').find('.qty-input').val();
//     var value = parseInt(inc_value,10);
//     value = isNaN(value) ? 0 : value;
//     if(value < 100000)
//     {
//       value++;
//       $(this).closest('.product_data').find('.qty-input').val(value);
//     }
//   });

//   $('.decrement-btn').click(function (e) {
//     e.preventDefault();

//     var dec_value = $(this).closest('.product_data').find('.qty-input').val();
//     var value = parseInt(dec_value,10);
//     value = isNaN(value) ? 0 : value;
//     if(value > 0)
//     {
//       value--;
//       $(this).closest('.product_data').find('.qty-input').val(value);
//     }
//   });

//   $('.qty-update').click(function (e) {
//     e.preventDefault();

//     var product_id = $(this).closest('.product_data').find('.prod_id').val();
//     var product_qty = $(this).closest('.product_data').find('.qty-input').val();
//     var token = $('input[name=csrfmiddlewaretoken]').val();

//     $.ajax({
//       type : "POST",
//       url : "/update_qty",
//       data : {
//         'product_id':product_id,
//         'product_qty':product_qty,
//         csrfmiddlewaretoken:token
//       },
//       dataType : "json",
//       success: function (response) {
        
//       }
//     });
//   });
// });
  