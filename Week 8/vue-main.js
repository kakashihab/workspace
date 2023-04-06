// create a Vue app

const app = Vue.createApp(
    {
        data()
        {
            return {pagename: "Naruto", 
                    description: "This is a page about Naruto",
                    mainimage: "konoha-naruto.gif",
                    wikilink: "https://en.wikipedia.org/wiki/Naruto",
                    big: true,
                    fighter: 'sakura',
                    bestcharacters: ["Naruto", "Sasuke", "Madara"],
                    /*bestplaces: [{place: "Konoha", district: "Fire nation", image: "konoha-j.jpg"},
                                 {place: "Sand Village", district: "Land of wind", image: "hidden sand.jpg"},
                                 {place: "Rain Village", district: "Fire nation", image: "hidden rain.png"}],*/
                    likes: 0,
                    happy: false
                    }
        },

        methods:
        {
            likesNaruto()
            {
                this.likes++;
                this.happy = true;
            },

            dislikesNaruto()
            {
                this.likes--;
                if (this.likes < 0)
                {
                    this.likes = 0
                    this.happy = false;
                }
                if (this.likes == 0)
                {
                    this.happy = false;
                }
                
            }

            /*placehover(placeimg)
            {
                
                document.getElementById("placeimg").src= placeimg;
            }
            */


            


        }
    })

