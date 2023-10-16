<template>
  <h2>Zahlen der groesse nach sortieren</h2>
    <div class="aufgabenformat">
      <div class="row">
        <div class="col zahlenformat">{{ generierteZahlenArray }}</div>
        <div class="col zahlenformat">{{ inputArray }}</div>

      </div>

      <div class="row">
        <div class="col">
          <input class="inputfield" type="text" v-model="inputZahleins" />
        </div>
        <div class="col">
          <input class="inputfield" type="text" v-model="inputZahlzwei" />
        </div>
        <div class="col">
          <input class="inputfield" type="text" v-model="inputZahldrei" />
        </div>
        <div class="col">
          <input class="inputfield" type="text" v-model="inputZahlvier" />
        </div>
      </div>
    </div>



    <button type="button" class="btn btn-outline-select" @click="zahlengenerator">Klick mich</button>
</template>

<script>
  export default {
    data() {
      return {
        count: 0,
        generierteZahlenArray: '',
        inputArray: [],
        inputZahleins: '',
        inputZahlzwei: '',
        inputZahldrei: '',
        inputZahlvier: '',
      };
    },
    methods: {
      zahlengenerator() {
        if(this.count < 20) {
          const generierteZahlenArray = [];
            
          for (let i = 0; i < 4; i++) {
            const generierteZahlen = Math.floor(Math.random() * 100) + 1;
            generierteZahlenArray.push(generierteZahlen) 
            this.generierteZahlenArray = generierteZahlenArray.join(" ");
          }
        }
      },


    },
  }
  
</script>

<style scoped>
  .aufgabenformat {
    font-size: 80px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  .zahlenformat {
    margin: 1%;
    padding: 1%;
    border: 1px solid black;
    width: 80px

  }
  .inputfield {
    font-size: 80px;
    width: 80px;
  }
</style>
