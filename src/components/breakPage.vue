<template>
  <div class="break-style">
    <p>{{ randomBreak}}</p> 
    <p>{{ timermessage }}</p>
  </div>
</template>

<script>
import data from '../assets/data.json'
  export default {
    data() {
      return {
        breakContainer: data.breakContainer,
        timermessage: '',
        randomBreak: {},
  
      }
    },
    mounted() {
      this.breakGenerator()
    },
      methods: {
        breakGenerator() {
            const index = Math.floor(Math.random() * this.breakContainer.length);
            this.randomBreak = this.breakContainer[index];
            this.isBreak = true;

            const timer = () => {
                let durationInSeconds
                
                if(index === 0) {
                     durationInSeconds = 30;
                } else {
                     durationInSeconds = 60;
                }
                
                let remainingTime = durationInSeconds
                const timerInterval = setInterval(() => {
                remainingTime-- ;
                this.timermessage = `${remainingTime}`;
                if(remainingTime <= 0) {
                    clearInterval(timerInterval);
                    this.timermessage = ''
                    this.randomBreak = 'Weiter geht´s'
                    
                }
            }, 1000);
            };
            if(index === 0 || index === 2) {
                timer(index);
            }
        },

    },
    
  }
</script>
