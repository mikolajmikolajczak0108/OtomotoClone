$(document).ready(function() {

    loadMore();

});

$(document).ready(function() {
    var filter = document.getElementById("filter-btn");
    console.log(filter)
   console.log("Filter button clicked");
  filter.addEventListener("click", function() {
    var brand = $("#brand-select").val();
    var model = $("#model-select").val();
    var production_year = $("#production-year-select").val();
    var price = $("#price-select").val();
    var mileage = $("#mileage-select").val()
    var is_garaged = $("#is_garaged-checkbox").is(":checked");
    var is_damaged = $("#is_damaged-checkbox").is(":checked");
    var is_after_accident = $("#is_after_accident-checkbox").is(":checked");
    var is_electric_seats = $("#is_electric_seats-checkbox").is(":checked");
    var is_cruise_control = $("#is_cruise_control-checkbox").is(":checked");
    var is_usb_port = $("#is_usb_port-checkbox").is(":checked");
    var is_abs = $("#is_abs-checkbox").is(":checked");
    var air_conditioning = $("#air_conditioning-select").val();
    var roof_type = $("#roof_type-select").val();
    var upholstery = $("#upholstery-select").val();
    console.log("hujostatni")
$.ajax({
  type: "GET",
  url: "/filter",
  data: {
    brand: brand,
    model: model,
    production_year: production_year,
    price: price,
    mileage: mileage,
    is_garaged: is_garaged,
    is_damaged: is_damaged,
    is_after_accident: is_after_accident,
    is_electric_seats: is_electric_seats,
    is_cruise_control: is_cruise_control,
    is_usb_port: is_usb_port,
    is_abs: is_abs,
    air_conditioning: air_conditioning,
    roof_type: roof_type,
    upholstery: upholstery
  },
  success: function(response) {

    $('#filtered-offers').html(response);
         window.location.href = "/filtered_offers?offers=" + encodeURIComponent(JSON.stringify(response));
         console.log("AJAX success");
console.log("Response: " + response);
    console.log("Huj zmieniaj strone")
  },
  error: function(error) {
    console.log(error)
        console.log("huj blad")
  },

});
  });
});


function loadMore() {
    var currentOffset = 20;
    var limit = 20;
    var loadMoreBtn = document.getElementById("load-more-offers-btn");
    loadMoreBtn.addEventListener("click", function() {

    fetch(`/?offset=${currentOffset}&limit=${limit}`, {
        method: "get",
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(function(response) {
            return response.json();
        })
        .then(function(offers) {
            // Use offers to update the page
            offers['recent_offers'].forEach(function(offer) {
                var newOffer = document.createElement('div');
                newOffer.className = "col-xl-3 col-lg-6 col-md-6 col-sm-12";

                var card = document.createElement('div');
                card.className = "card";

                var img = document.createElement('img');
                img.src = offer.image1; // offer[6] when images ready
                img.className = "card-img-top img-fluid";
                img.alt = "offer image";
                card.appendChild(img);

                var cardBody = document.createElement('div');
                cardBody.className = "card-body";

                var title = document.createElement('h5');
                title.className = "card-title";
                title.innerHTML = offer[2] + " " + offer[1] + " " + offer[3];
                cardBody.appendChild(title);

                var text = document.createElement('p');
                text.className = "card-text";
                text.innerHTML = offer[4];
                cardBody.appendChild(text);

                card.appendChild(cardBody);
                newOffer.appendChild(card);

                var offersRow = document.querySelector(".recent_offers");
                offersRow.appendChild(newOffer);
            });
            currentOffset += limit;
        })
        .catch(function(error) {
            console.log(error);
        });

        });

}
