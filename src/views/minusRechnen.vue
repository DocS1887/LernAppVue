<template>
        <h2>Rechnen wir mit Minusaufgaben!</h2>
        <div class="row">
        <div class="aufgabenformat">
          <p>{{ zahlEins }} - {{ zahlZwei }} = <input type="text" v-model="eingabe" ref="inputField" @keydown.enter="pruefen"></p>
        </div>
        <div class="row d-flex justify-content-center auswertung"  v-if="endErgbnis === true">
            <h2>Ergebnis:</h2>
            <div class="col"></div>
            <div class="col d-flex justify-content-center">
              <div class="card text-bg-success mb-3 card-size" style="max-width: 13rem;">
                <div class="card-body">
                  <h5 class="card-title">Richtige</h5>
                  <p class="card-text">{{ istRichtig }}</p>
                </div>
              </div>
            </div>
            <div class="col d-flex justify-content-center">
              <div class="card text-bg-danger mb-3" style="max-width: 13rem;">
                <div class="card-body">
                  <h5 class="card-title">Falsche</h5>
                  <p class="card-text">{{ istFalsch }}</p>
                </div>
              </div>
            </div>
            <div class="col"></div>
            <div class="row" style="justify-content: center; padding-top: 5%;">
              <button type="button" class="btn btn-outline-info" @click="nochmal()">Nochmal?</button>
            </div>
        </div>
      </div>
  
      <div class="row">
        <div class="col-6 offset-3 d-flex justify-content-center">
          <button v-if="startButton === true" type="button" class="btn btn-outline-info smaller-button" @click="starten">Los geht's</button>
        </div>
      </div>
  </template>
  <script>
    export default {
      data() {
        return {
        zahlEins: '?',
        zahlZwei:'?',
        eingabe: '',
        count: 0,
        istRichtig: 0,
        istFalsch: 0,
        startButton: true,
        endErgbnis: false,
        }
      },
      methods: {
        starten() {
        this.zahlengenerator();
        this.startButton = false;
      },
        zahlengenerator() {
          if(this.count < 20){
          let ersteZahl = Math.floor(Math.random() * 20);
          let zweiteZahl = Math.floor(Math.random() * 20);

          if(ersteZahl < zweiteZahl) {
            let temp = ersteZahl;
            ersteZahl = zweiteZahl;
            zweiteZahl = temp;
          }

          this.zahlEins = ersteZahl;
          this.zahlZwei = zweiteZahl;
          this.count++;
          this.isGleich = null;
          this.eingabe = '';
          this.$refs.inputField.focus();
          } else {
            this.endErgbnis = true;
          }
        },
        pruefen() {
          let ergebnis = parseInt(this.eingabe, 10);
          if (ergebnis === this.zahlEins - this.zahlZwei) {
            this.istRichtig++;
          } else {
            this.istFalsch++;
          }
          this.zahlengenerator();
   
        },
        nochmal() {
          window.location.reload();
        }
  
      },
    }
  </script>
  
  <style scoped>
    .inner-content {
      min-height: 500px;
    }
    .aufgabenformat{
    font-size: 100px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  
  .smaller-button {
    font-size: 20px;
    padding: 5px 10px;
    width: auto; 
    margin-top: 10%;
  }
 
  .auswertung {
  justify-content: center;
  text-align: center;
}
  </style>
  