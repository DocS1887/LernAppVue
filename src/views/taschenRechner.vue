<template>
            <div class="background">
                <div class="row display">
                    {{displayAusgabe}}
                </div>
                
                <div class="row">
                    <div class="col tastenoperator" @click="clear()">AC</div>
                    <div class="col tastenoperator">C</div>
                    <div class="col tastenoperator">+/-</div>
                    <div class="col tastenoperator" @click="operation('/')">/</div>
                </div>
                <div class="row">
                    <div class="col tastenzahl">7</div>
                    <div class="col tastenzahl">8</div>
                    <div class="col tastenzahl">9</div>
                    <div class="col tastenoperator" @click="operation('*')">x</div>
                </div>
                <div class="row">
                    <div class="col tastenzahl" @click="addNumber(4)">4</div>
                    <div class="col tastenzahl" @click="addNumber(5)">5</div>
                    <div class="col tastenzahl" @click="addNumber(6)">6</div>
                    <div class="col tastenoperator" @click="operation('-')">-</div>
                </div>
                <div class="row">
                    <div class="col tastenzahl">1</div>
                    <div class="col tastenzahl">2</div>
                    <div class="col tastenzahl">3</div>
                    <div class="col tastenoperator" @click="operation('+')">+</div>
                </div>
                <div class="row">
                    <div class="col tastenzahl">0</div>
                    <div class="col tastenzahl">00</div>
                    <div class="col tastenoperator">,</div>
                    <div class="col tastenoperator" @click="calculate()">=</div>
                </div>
            </div>
</template>

<script>
export default {
    data() {
        return {
            displayAusgabe: '0',
            zahlen: [],
            operator: null,
        }
    },
    methods: {
        addNumber(value) {
            this.displayAusgabe = ''
            this.zahlen.push(value);
            this.displayAusgabe = value;
            console.log(this.zahlen)
        },
        clear() {
        this.zahlen = [];
        console.log(this.zahlen)
        this.displayAusgabe = 0;
        },
        operation(operator) {
            this.operator = operator
            console.log(operator)
        },
        calculate(){
            if(this.zahlen.length > 1 && this.operator) {
                let result;
                switch(this.operator) {
                    case '+':
                        result = this.zahlen.reduce((sum, num) => sum + num);
                        break;

                        case '-':
                        result = this.zahlen.reduce((diff, num) => diff - num);
                        break;

                        case '*':
                        result = this.zahlen.reduce((prod, num) => prod * num);
                        break;

                        case '/':
                        result = this.zahlen.reduce((quot, num) => quot / num);
                        break;
                }
                this.displayAusgabe = result
            }
        }
    },

}
</script>

<style scoped>

.tastenzahl {
    width: 80px;
    height: 80px;
    text-align: center;
    background-color: darkgray;
    border-radius: 50%;
    margin: 2%;
    border: 2px solid white;
    display: flex;
    justify-content: center;
    align-items: center;
}
.tastenzahl:hover {
    background-color: gray;
    color: antiquewhite;

}
.tastenoperator {
    width: 80px;
    height: 80px;
    text-align: center;
    background-color: orange;
    border-radius: 50%;
    margin: 2%;
    border: 2px solid white;
    display: flex;
    justify-content: center;
    align-items: center;
}
.tastenoperator:hover {

    background-color: darkorange;
    color: antiquewhite;
}
.display {
    text-align: end;
    justify-content: end;
    border: 2px solid black;
    background-color: antiquewhite;
    margin-bottom: 10%;
    height: 150px;
    align-items: center;
    padding-right: 3%;
    border-radius: 10px;
    font-size: 50px;

}
.background {
    background-color: lightgray;
    padding: 10%;
    border-radius: 10px;
    min-width: 400px;
}
</style>