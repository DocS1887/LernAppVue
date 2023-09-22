
<template>
      <h2>Jetzt werden ganze Wörter gelesen</h2>
      <div class="row">
        <div class="wortformat">
        <p>{{zufallswort}}</p>
      </div>
      </div>
      <div class="row" style="justify-content: center;">
        <button type="button" class="btn btn-outline-info" @click="wortGenerator">Nächstes Wort</button>
      </div>
</template>

<script>
import data from '../assets/data.json'
export default {
  data() {
    return {
    woerterArray: data.woerterArray,
    zufallswort: 'Bereit?',
    count: 0
    };
  },
  methods: {
    wortGenerator() {
      if(this.count < 25 ) {
        const wortIndex = Math.floor(Math.random() * this.woerterArray.length);
        this.zufallswort = this.woerterArray[wortIndex];
        this.count ++;
      }
      else {
        this.zufallswort = 'Fertig :)'
      }
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