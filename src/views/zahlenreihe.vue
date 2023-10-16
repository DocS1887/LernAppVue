<template>
  <h2>Ergänze die fehlenden Zahlen!</h2>
  <div>
    <div v-for="(number, index) in numberSequence" :key="index" class="number-container">
      <template v-if="inputPositions.includes(index)">
        <input v-model="userInputs[index]" type="text" class="input-field" :style="{ border: '3px solid ' + inputBorders[index] }" @keyup.enter="handleEnterKey(index)" /> 

      </template>
      <template v-else>
        {{ number }}
      </template>
    </div>
    <div>
        <button class="btn btn-outline-select" @click="checkAnswers">Check it out!</button>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      numberSequence: [],
      inputPositions: [],
      userInputs: Array(5).fill(''),
      inputBorders: Array(5).fill('wheat'),
    };
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
      const startNumber = Math.floor(Math.random() * 100) +1;
      this.numberSequence = Array.from({ length: 5}, (_, index) => startNumber + index); 

      // Zufällige Auswahl von Positionen für die Eingabefelder
      this.inputPositions = this.getRandomPositions(3);
      console.log(this.numberSequence);
      console.log(this.inputPositions);


    },
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

    handleEnterKey(index) {
      if(index < this.inputPositions.length -1) {
        this.$refs[`input${index + 2}`].focus();
      } else {
        this.checkAnswers();
      }
    },

    checkAnswers() {
      for (let i = 0; i < this.inputPositions.length; i++) {
        const position = this.inputPositions[i];
        const expectedValue = this.numberSequence[position];
        let inputValue = this.userInputs[position];

        console.log(`Zahl ${i + 1} an Position ${position} - Erwartet: ${expectedValue}, Eingegeben: ${inputValue}`);
      
        if (position !== undefined) {
          if (!isNaN(inputValue)) {
            inputValue = parseInt(inputValue, 10);

            if(expectedValue === inputValue) {
              this.inputBorders[position] = 'green';
              console.log("das ist richtig");
            } else {
              this. inputBorders[position] = 'red';
              console.log("das ist falsch");
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
    }
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
  }
.input-field {
  font-size: 80px;
  width: 80px;
}

</style>
