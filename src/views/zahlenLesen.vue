
<template>
    <div class="content">
      <div class="inner-content">
        <h2>Nun werden Zahlen gelesen mein Freund</h2>
        <div class="row">
          <div class="wortformat">
          <p>{{zufallszahl}}</p>
          <input type="number" v-model="eingabe" @keydown.enter="abgleich">
          <button @click="abgleich">Pruefen</button>
            <p v-if="eingabe !== null && isGleich === true">Jaa, das ist richtig. Super!</p>
            <p v-else-if="eingabe !== null && isGleich === false">Oje. Das war wohl nix...</p>
        </div>
        </div>
        <div class="row">
          <button type="button" class="btn btn-outline-info" @click="zahlenGenerator">Nächste Zahl</button>
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
        if(this.count <= 20) {
          const zahlIndex = Math.floor(Math.random() * this.zahlWortContainer.length);
          this.zufallszahl = this.zahlWortContainer[zahlIndex];
          this.count ++;
            
        }
        else {
          this.zufallszahl = 'Fertig :)'
        }
      },
      abgleich() {
        const zahl = this.zahlWortContainer.indexOf(this.zufallszahl) + 1;

        if(this.eingabe !== null && Number(this.eingabe) === zahl) {
            this.isGleich = true;
        } else {
            this.isGleich = false;
        }

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
 

  </style>