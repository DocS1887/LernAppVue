
<template>
      <h2>Nun werden Zahlen gelesen mein Freund</h2>
      <div class="row">
        <div class="col-6 offset-3 d-flex justify-content-center">
          <div class="wortformat">
            <p>{{ zufallszahl }}</p>
            <span v-if="zufallszahl === 'Fertig'">😊</span>
          </div>
        </div>
      </div>

      <div class="row d-flex justify-content-center">
        <input v-if="inputfield === true" type="text" v-model="eingabe" ref="inputField" @keydown.enter="abgleich">
        <div class="d-flex justify-content-center mt-5">
          <div class="row auswertung"  v-if="ergebnis === true">
            <h2>Ergebnis:</h2>
            <div class="col">
              <div class="card text-bg-success mb-3 card-size" style="max-width: 18rem;">
                <div class="card-body">
                  <h5 class="card-title">Richtige</h5>
                  <p class="card-text">{{ isRichtig }}</p>
                </div>
              </div>
            </div>
            <div class="col">
              <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
                <div class="card-body">
                  <h5 class="card-title">Falsche</h5>
                  <p class="card-text">{{ isFalsch }}</p>
                </div>
              </div>
            </div>
            <div class="row" style="justify-content: center; padding-top: 5%;">
              <button type="button" class="btn btn-outline-info" @click="nochmal()">Nochmal?</button>

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
        eingabe: null,
        zahlWortContainer: data.zahlWortContainer,
        zufallszahl: 'Bereit?',
        isRichtig: 0,
        isFalsch: 0,
        count: 0,
        ergebnis: false,
        inputfield: true,
  
      };
    },
    methods: {
      zahlenGenerator() {
        if(this.count < 20) {
          const zahlIndex = Math.floor(Math.random() * this.zahlWortContainer.length);
          this.zufallszahl = this.zahlWortContainer[zahlIndex];
          this.count ++;
        }
        else {
          this.zufallszahl = 'Fertig';
          this.ergebnis = true;
          this.inputfield = false;
        }
        this.isGleich = null;
        this.$refs.inputField.focus();
      },
      abgleich() {
        const zahl = this.zahlWortContainer.indexOf(this.zufallszahl) + 1;

        if(this.eingabe !== null && Number(this.eingabe) === zahl) {
            this.isRichtig ++;
        } else {
            this.isFalsch ++;
        }
        this.eingabe = '';
        this.zahlenGenerator();
        
      },
      nochmal() {
        window.location.reload();
      }
    },
    mounted () {
        this.zahlenGenerator();
    }
  }
</script>
  
<style scoped>
  
  .wortformat{
  font-size: 100px;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
input {
    font-size: 50px;
    width: 14%;

}

.auswertung {
  justify-content: center;
}
</style>