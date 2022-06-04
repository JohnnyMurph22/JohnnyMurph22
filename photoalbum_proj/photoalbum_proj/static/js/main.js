// make on click search function, run a search when we click on the button, grab with jquery, to search pokemon in  

$("#submit-button").click(function(event){
    $("#card-container").empty();
    event.preventDefault();
    var pokemon = $("#search")
    .val()
    .trim();
    console.log(pokemon)
    $.ajax({
        method: "GET",
        url: "https://api.pokemontcg.io/v2/cards?q=name:"  + pokemon
    })
    .then(function(response){
        for(pokemon of response.data) {console.log(pokemon.images.small)
        // for(var i = 0; i <response.data.length;i++){}
            var pokemonCard = $("<img class='poke-card'>");
            pokemonCard.attr("src", pokemon.images.small);
            $("#card-container").append(pokemonCard);
        }
    });
});

// function to save selected pokemon cards
cardSaveBtn.add