<template>
  <div class="content">
    <div class="inner-content">
      <h2>Hier rechnen Profis. Plus und Minus gemischt!</h2>
      <div class="row">
        <div class="aufgabenformat">

            <p>{{ zahlEins }} {{operator}} {{ zahlZwei }} = <input type="text" v-model="eingabe" ref="inputField" @keydown.enter="pruefen"></p>



          <div v-if="count === 20">
            <div class="row d-flex justify-content-center">
              <h2>Ergebnis:</h2>
              <div class="row d-flex justify-content-center">
                <div class="col ergebnisformat" style="border: 3px solid; border-color: green;">Richtig: {{istRichtig}}</div>
                <div class="col ergebnisformat" style="border: 3px solid; border-color: red;">Falsch: {{istFalsch}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row d-flex justify-content-center">
        <div class="d-flex justify-content-center mt-5">
          <div v-if="isGleich === true">
            <div class="card text-bg-success mb-3 card-size" style="max-width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">Super !!!</h5>
                <p class="card-text">Das war richtig :)</p>
              </div>
            </div>
          </div>
          <div v-else-if="isGleich === false">
            <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">Oh Nein...</h5>
                <p class="card-text">Das war wohl nix</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-6 offset-3 d-flex justify-content-center">
          <button type="button" class="btn btn-outline-info smaller-button" @click="zahlengenerator">Aufgabe stellen</button>
        </div>
      </div>
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
      isGleich: null,
      count: 0,
      istRichtig: 0,
      istFalsch: 0,
      operatorArray: ['+', '-'],
      operator: '',
    }
  },
  methods: {
    zahlengenerator() {
      if(this.count < 20){
        let ersteZahl = Math.floor(Math.random() * 20);
        let zweiteZahl = Math.floor(Math.random() * 20);
        let operatorindex = Math.floor(Math.random() * this.operatorArray.length);
        this.operator = this.operatorArray[operatorindex];
        if(this.operator === '-') {
          if (ersteZahl < zweiteZahl) {
            let temp = ersteZahl;
            ersteZahl = zweiteZahl;
            zweiteZahl = temp;
          }
        }
        if(this.operator === '+') {
          let sum = ersteZahl + zweiteZahl
          if(sum > 20) {
            ersteZahl = Math.floor(Math.random() * 10);
            zweiteZahl = Math.floor(Math.random() * 10);
          }
        }
        this.zahlEins = ersteZahl;
        this.zahlZwei = zweiteZahl;
        this.count++;
        this.isGleich = null;
        this.eingabe = '';
        this.$refs.inputField.focus();
      }
    },
    pruefen() {
      let ergebnis = parseInt(this.eingabe, 10);
      if(this.operator === '-') {
        if (ergebnis === this.zahlEins - this.zahlZwei) {
          this.isGleich = true;
          this.istRichtig++;
        } else {
          this.isGleich = false;
          this.istFalsch++;
        }
      } else {
        if (ergebnis === this.zahlEins + this.zahlZwei) {
          this.isGleich = true;
          this.istRichtig++;
        } else {
          this.isGleich = false;
          this.istFalsch++;
        }
      }
    }

  },
}
</script>

<style scoped>
.inner-content {
  min-height: 500px;
}
.aufgabenformat{
  font-size: 150px;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
input {
  font-size: 150px;
  width: 34%;
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
.ergebnisformat {
  text-align: center;
  font-size: 35px;
  margin: 2%;

}
h2 {
  text-align: center;
  padding-bottom: 2%;
  font-family: Bubblegum;
}
</style>
