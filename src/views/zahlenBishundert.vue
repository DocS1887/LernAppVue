<template>
  <h2>Zahlen bis Hundert</h2>
  <div v-if="!showBreakPage">
  <div class="row">
    <div class="ausgabeformat">
      <p>{{zahlenAusgabe}}</p>
    </div>
  </div>
  <div class="row" style="justify-content: center;">
    <button v-if="!fertig" type="button" class="btn btn-outline-info" @click="zahlGenerieren">Nächste Zahl</button>
    <button v-if="fertig" type="button" class="btn btn-outline-info" @click="nochmal">Nochmal?</button>

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
import BreakPage from '../components/breakPage.vue'
export default {
  data() {
    return {
      zahlenAusgabe: 'Bereit?',
      count: 0,
      showBreakPage: false,
      fertig: false,
    }
  },
  components: {
          BreakPage,
        },
  methods: {
    zahlGenerieren() {
      if(this.count < 20) {
        const zufallsZahl = Math.floor(Math.random() * 100);
        this.zahlenAusgabe = zufallsZahl;
        this.count ++;
        if(this.count === 10) {
            this.showBreakPage = !this.showBreakPage;
        }
      } else {
        this.zahlenAusgabe = 'Fertig'
        this.fertig = !this.fertig
      }
    },
    nochmal() {
    window.location.reload();
  },
  pauseEnde() {
    this.showBreakPage = false;
  }
  }
}
</script>

<style>
.ausgabeformat {
  font-size: 100px;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, san-serif;
}
</style>
