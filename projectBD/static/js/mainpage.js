
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
        offers.forEach(function(offer) {
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

            var offersRow = document.querySelector(".row");
            offersRow.appendChild(newOffer);
        });

        currentOffset += limit;
    })
    .catch(function(error) {
        console.log(error);
    });

    });
