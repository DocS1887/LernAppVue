<template>
  <h2>Ergänze die fehlenden Zahlen!</h2>
  <div v-if="!showBreakPage">
    <div v-for="(number, index) in numberSequence" :key="index" class="number-container">
      <template v-if="inputPositions.includes(index)">
        <input v-model="userInputs[index]" type="text" class="input-field" :style="{ border: '3px solid ' + inputBorders[index] }" @keyup.enter="handleEnterKey($event, index)" /> 
      </template>
      <template v-else>
        <div>
          {{ number }}
        </div>
      </template>
    </div>

    <div>
      <div v-if="fertig === false" class="row" style="justify-content: center;">
        <button v-if="!showBreakPage" class="btn btn-outline-select" @click="checkAnswers">Prüfen!</button>
        <button v-if="showBreakPage" type="button" class="btn btn-outline-info" @click="weiter">Weiter</button>
      </div>
    </div>
    <!--Ausgabe des Ergebnisses-->
    <div class="row d-flex justify-content-center">
        <div class="d-flex justify-content-center mt-5">
          <div class="row auswertung"  v-if="fertig === true">
            <h2>Ergebnis:</h2>
            <div class="col">
              <div class="card text-bg-success mb-3 card-size" style="max-width: 18rem;">
                <div class="card-body">
                  <h5 class="card-title">Richtige</h5>
                  <p class="card-text">{{ reiheRichtig }}</p>
                </div>
              </div>
            </div>
            <div class="col">
              <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
                <div class="card-body">
                  <h5 class="card-title">Falsche</h5>
                  <p class="card-text">{{ reiheFalsch }}</p>
                </div>
              </div>
            </div>
            <p class="d-flex justify-content-center mt-5">
              <button type="button" class="btn btn-outline-info" @click="nochmal()">Nochmal?</button>
            </p>
          </div>
        </div>
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
      numberSequence: [],
      inputPositions: [],
      userInputs: Array(5).fill(''),
      inputBorders: Array(5).fill('wheat'),
      count: 0,
      fertig: false,
      isFalsch: 0,
      reiheRichtig: 0,
      reiheFalsch: 0,
      durchlauf: 0,
      showBreakPage: false,

    };
  },
  components: {
          BreakPage,
        },

  computed: {
    sortetNumberSequence() {
      return [this.numberSequence].sort((a, b) => a - b );
    }
  },

  mounted() {
    this.generateNumberSequence();
  },

  methods: {
    generateNumberSequence() {
      // Anzahl der Durchläufe
      if (this.count < 20) {
        const startNumber = Math.floor(Math.random() * 100) +1;
        this.numberSequence = Array.from({ length: 5}, (_, index) => startNumber + index); 

        // Zufällige Auswahl von Positionen für die Eingabefelder
        this.inputPositions = this.getRandomPositions(3);
        this.count ++;
        // Einbinden der externen break Funktion
        if(this.count === 10) {
          this.showBreakPage = !this.showBreakPage;;
      }
        }
        else {
          this.numberSequence = "Geschafft :)";
          this.fertig = true;
        }

    },
    // Erstellung zufaellige Position der Inputfelder
    getRandomPositions(count) {
      const positions = [];
      while (positions.length < count) {
        const randomPosition = Math.floor(Math.random() * 5);
        if (!positions.includes(randomPosition)) {
          positions.push(randomPosition);
        }
      }
      return positions;
    },
    // Weiter nach Pause
    pauseEnde() {
    this.showBreakPage = false;
  },
    //Noch ohne wirkliche Funktion. Soll mit Enrter Taste ins naechste Feld springen
    handleEnterKey(event, index) {
      try {
        const currentInput = event.currentTarget;
        const nextIndex = index + 1;
        const nextInput = currentInput.parentElement.querySelector(`.input-field:nth-child(${nextIndex})`);

        if (nextInput) {
          nextInput.focus();
        } else {
          console.error(`Element not found or not visible with index: ${nextIndex}`);
        }
      } catch (error) {
        console.error('Error in handleEnterKey:', error);
      }
    },
    // Prueft die Eingabe und zaehlt die richtigen und falschen. 
    checkAnswers() {
      for (let i = 0; i < this.inputPositions.length; i++) {
        const position = this.inputPositions[i];
        const expectedValue = this.numberSequence[position];
        let inputValue = this.userInputs[position];
      
        if (position !== undefined) {
          if (!isNaN(inputValue)) {
            inputValue = parseInt(inputValue, 10);

            const isCorrect = expectedValue === inputValue;
            const borderValue = isCorrect ? 'green' : 'red';
            this.inputBorders[position] = borderValue;

            if(['red', 'green'].includes(borderValue)) {
              this.durchlauf++

              if(borderValue === 'red') {
                this.isFalsch++
              } 

              if(this.durchlauf === 3){
                if(this.isFalsch > 0) {
                  this.reiheFalsch++
                } else {
                  this.reiheRichtig++
                }
                this.durchlauf = 0;
                this.isFalsch = 0;
              }
            }
          } else {
             alert("Du hast nichts eingegeben!")
          }
        } else {
          console.warn("Position ist während des Renderns nicht definiert");
        }
      }
      this.nextTry();
    },
    // Sorgt faduer, das die naechste Reihe nach 2 Sek. generiert wird
    nextTry() {
      setTimeout(() => {
        console.log(this.expectedValue)
        console.log(this.inputValue)
        this.userInputs = [];
        this.inputPositions = [];
        this.inputBorders = [];
        this.$nextTick(() => {
          this.generateNumberSequence();
        });
      }, 2000)
    },
    // Laedt die Seite neu
    nochmal() {
    window.location.reload();
  },
  },


};
</script>

<style>
  .number-container {
    display: inline-block;
    margin-right: 20px;
    font-size: 80px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    justify-content: center;
  }
  .input-field {
    font-size: 80px;
    width: 80px;
  }
  .break-style {
    font-size: 100px;
    text-align: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  }
  .auswertung {
  justify-content: center;
}
</style>

