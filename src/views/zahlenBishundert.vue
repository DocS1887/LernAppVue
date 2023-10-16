<template>
  <h2>Zahlen bis Hundert</h2>
  <div class="row">
    <div class="ausgabeformat">
      <p>{{zahlenAusgabe}}</p>
    </div>
  </div>
  <div class="row" style="justify-content: center;">
    <button type="button" class="btn btn-outline-info" @click="zahlGenerieren">Nächste Zahl</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      zahlenAusgabe: 'Bereit?',
      count: 0,
    }
  },

  methods: {
    zahlGenerieren() {
      if(this.count < 20) {
        const zufallsZahl = Math.floor(Math.random() * 100);
        this.zahlenAusgabe = zufallsZahl;
        this.count ++;
      } else {
        this.zahlenAusgabe = 'Fertig'
      }
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
