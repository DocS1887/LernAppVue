<template>
  <h2>Jetzt werden ganze Wörter gelesen</h2>
  <div v-if="!showBreakPage">
  <div class="row">
    <div class="wortformat">
      
        {{zufallswort}}
      
    </div>
  </div>
  
  <div class="row" style="justify-content: center;">
    <button type="button" class="btn btn-outline-info" @click="wortGenerator">Nächstes Wort</button>
  </div>
  </div>

  <div class="row justify-content-center">
  <div class="col text-center">
    <div v-if="showBreakPage">
      <breakPage></breakPage>
      <button class="btn btn-outline-select" @click="pauseEnde">Weiter</button>
    </div>
  </div>
</div>
</template>

<script>
import data from '../assets/data.json'
import BreakPage from '../components/breakPage.vue'
export default {
data() {
  return {
    woerterArray: data.woerterArray,
    zufallswort: 'Bereit?',
    count: 0,
    timermessage: '',
    showBreakPage: false,
  
};
},
components: {
          BreakPage,
        },
methods: {
  wortGenerator() {
    if(this.count < 25 ) {
      const wortIndex = Math.floor(Math.random() * this.woerterArray.length);
      this.zufallswort = this.woerterArray[wortIndex];
      this.count ++;
      if(this.count === 10 ) {
        this.showBreakPage = !this.showBreakPage;
      }
    }
    else {
      this.zufallswort = 'Fertig :)'
    }
  }, 
    pauseEnde() {
    this.showBreakPage = false;
  }
  }
}
</script>

<style scoped>
  .wortformat{
    font-size: 100px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
</style>
