<template>
    <div class="content">
      <div class="inner-content">
        <h2>{{ headline }}</h2>
        <div class="row">  
            <div class="col">
                <div class="card text-bg-success mb-3" type="button" v-if="!content" @click="content= true, nextWord('a')" style="max-width: 18rem;">
                    <div class="card-header"></div>
                    <div class="card-body">
                    <h5 class="card-title">Ben und Kater Fridolin</h5>
                    </div>
                </div>
            </div>

            <div class="col">
                <div class="card text-bg-danger mb-3" type="button" v-if="!content" @click="content= true, nextWord('b')" style="max-width: 18rem;">
                    <div class="card-header"></div>
                    <div class="card-body">
                    <h5 class="card-title">Der Junge in der Nacht</h5>
                    </div>
                </div>
            </div>

            <div class="col">
                <div class="card text-bg-warning mb-3" type="button" v-if="!content" @click="content= true, nextWord('c')" style="max-width: 18rem;">
                    <div class="card-header"></div>
                    <div class="card-body">
                    <h5 class="card-title">Was ist im Zimmer passiert?</h5>
                    </div>
                </div>
            </div>
            <div class="wortformat">
                <p>{{geschichte}}</p>
                <button type="button" class="btn btn-outline-info" v-if="content" @click="nextWord(weiter)">Weiter</button>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
import data from '../assets/data.json'
export default {
    data() {
        
        return {
                geschichteEins: data.geschichteEins,
                geschichteZwei: data.geschichteZwei,
                geschichteDrei: data.geschichteDrei,
                geschichte: '',
                count: 0,
                content: false,
                headline: 'Eine von drei spannenden Geschichten',
                
        }
    },
    methods: {
        nextWord(auswahl) {
            const geschichten = {
                'a': this.geschichteEins,
                'b': this.geschichteZwei,
                'c': this.geschichteDrei
            };
            const headlines = {
                'a': 'Ben und Fridolin',
                'b': 'Der Junge in der Nacht',
                'c': 'Was ist im Zimmer passiert?'
            };
            if(this.count < geschichten[auswahl].length) {
            this.weiter = auswahl;
            this.geschichte = geschichten[auswahl][this.count];
            this.count ++;}
            else {
                this.geschichte = "Willst du noch eine Geschichte?";
                this.content = false;
                this.count = 0;
            }

   
            this.headline = headlines[auswahl];            
        },
    },
}
</script>
<style scoped>
.wortformat {
    text-align: center;
    font-size: 70px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    padding-top: 10%;
}
.card-title{
    font-family: Bubblegum;
    font-size: 25px;
}

</style>