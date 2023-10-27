<template>
  <h2>Los Ben, lass uns Buchstaben lesen!</h2>
  <div v-if="!showBreakPage">
  <div class="row">
    <div class="letterformat">
        <p>{{randomLetter}}</p>
    </div>
  </div>
  <div class="row" style="justify-content: center;">
    <button v-if="!fertig" type="button" class="btn btn-outline-info" @click="zufallsGenerator">Nächster Buchstabe</button>
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
import data from '../assets/data.json'
import BreakPage from '../components/breakPage.vue'
export default {
  data() {
    return {
      lettersArray: data.lettersArray,
      randomLetter: 'Bereit?',
      count: 0,
      showBreakPage: false,
      fertig: false,
        };
  },
  components: {
          BreakPage,
        },
  methods: {
    // Generate a random Letter from lettersArray in json
    zufallsGenerator() {
      if(this.lettersArray.length > 0) {
        const index = Math.floor(Math.random() * this.lettersArray.length);
        this.randomLetter = this.lettersArray[index];
        this.lettersArray.splice(index, 1);
        this.count++;
        if(this.count === 10) {
            this.showBreakPage = !this.showBreakPage;
        }
      } else {
        this.randomLetter = 'Fertig :)'
        this.fertig = !this.fertig;
      }
    },
    nochmal() {
    window.location.reload();
  },
  pauseEnde() {
    this.showBreakPage = false;
  }
  },
}
</script>

<style scoped>
.letterformat{
  font-size: 100px;
  font-weight: 700;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.btn.btn-outline-info {
  text-align: center;
  justify-content: center;
  align-content: center;
}

</style>
