
<template>
    <div class="content">
      <div class="inner-content">
        <h2>Nun werden Zahlen gelesen mein Freund</h2>
          <div class="row">
            <div class="col-6 offset-3 d-flex justify-content-center">
              <div class="wortformat">
                <p>{{ zufallszahl }}</p>
              </div>
            </div>
          </div>
          
          <div class="row d-flex justify-content-center">
              <input type="text" v-model="eingabe" ref="inputField" @keydown.enter="abgleich">
              <div v-if="eingabe !== null && isGleich === true">
                <div class="card text-bg-success mb-3 card-size" style="max-width: 18rem;">
                  <div class="card-body">
                    <h5 class="card-title">Super !!!</h5>
                    <p class="card-text">Das war richtig :)</p>
                  </div>
                </div>
            </div>
              <div v-else-if="eingabe !== null && isGleich === false">
                <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
                  <div class="card-body">
                    <h5 class="card-title">Oh Nein...</h5>
                    <p class="card-text">Das war wohl nix</p>
                  </div>
                </div>
            </div>
          </div>

          <div class="row">
            <div class="col-6 offset-3 d-flex justify-content-center">
              <button type="button" class="btn btn-outline-info smaller-button" @click="zahlenGenerator">Nächste Zahl</button>
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
        isGleich: null,
        count: 0,
  
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
          this.zufallszahl = 'Fertig :)'
        }
        this.isGleich = null;
        this.$refs.inputField.focus();
      },
      abgleich() {
        const zahl = this.zahlWortContainer.indexOf(this.zufallszahl) + 1;

        if(this.eingabe !== null && Number(this.eingabe) === zahl) {
            this.isGleich = true;
        } else {
            this.isGleich = false;
        }
        this.eingabe = '';
        
      }
    },
    mounted () {
        this.zahlenGenerator();
    }
  }
  </script>
  
  <style scoped>
  .inner-content {
    min-height: 500px;
  }
  .wortformat{
  font-size: 200px;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
input {
    font-size: 85px;
    width: 20%;
    height: auto;
    text-align: center;
    border: 3px solid lightblue;
}

.smaller-button {
  font-size: 20px;
  padding: 5px 10px;
  width: auto; 
  margin-top: 10%;
}


  </style>