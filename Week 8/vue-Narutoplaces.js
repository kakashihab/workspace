app.component("villages",
{
    template:
    `<div>
        <div>
            <p> Famous places in the Naruto-universe v2</p>
            <div v-for="bestplace in bestplaces" v-on:mouseover="placehover(bestplace.image);">
            <p class="borded_para">
                {{ bestplace.place }} : {{ bestplace.district }}
            </p>
        
            </div>
        <img id="placeimg" src="" style="width: 350px; height: 200px; background-color: grey;">
        </div>
    </div>`,

    data()
    {
        return {

            bestplaces: [{place: "Konoha", district: "Fire nation", image: "konoha-j.jpg"},
                         {place: "Sand Village", district: "Land of wind", image: "hidden sand.jpg"},
                         {place: "Rain Village", district: "Fire nation", image: "hidden rain.png"}],
        }
    },

    methods: 
    {
        placehover(placeimg)
            {
                
                document.getElementById("placeimg").src= placeimg;
            }
    }
})