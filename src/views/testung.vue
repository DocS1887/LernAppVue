<template>
    <div>
      <h1>Meine App</h1>
      <Button />
    </div>
  </template>
  
  <script>
  import Button from '../components/testSeite.vue';
  
  export default {
    components: {
      Button
    },
    methods: {
      handleClick() {
        console.log("Funktion in der App-View aufgerufen!");
      }
    }
  }
  </script>
  