
<template>
    <div class="content">
      <div class="inner-content">
        <h2>Nun werden Zahlen gelesen mein Freund</h2>
        <div class="row">
          <div class="wortformat">
          <p>{{zufallszahl}}</p>
          <input type="text" v-model="eingabe" inputmode="numeric">

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
        zahlWortContainer: data.zahlWortContainer,
        zufallszahl: 'Bereit?',
      };
    },
    methods: {
      zahlenGenerator() {
        if(this.zahlWortContainer.length > 0) {
          const zahlIndex = Math.floor(Math.random() * this.zahlWortContainer.length);
          this.zufallszahl = this.zahlWortContainer[zahlIndex];
          this.zahlWortContainer.splice(zahlIndex, 1);
        }
        else {
          this.zufallszahl = 'Fertig :)'
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .wortformat{
    font-size: 200px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  .inner-content {
    min-height: 500px;
  }
  input {
    width: 20%;
    height: 40%;
    font-size: 180px;
    text-align: center;
  }

  </style>