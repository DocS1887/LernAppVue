<template>
    <button @click="handleClick">Klick mich!</button>
  </template>
  
  <script>
  export default {
    methods: {
      handleClick() {
        console.log("Button wurde geklickt!");
      }
    }
  }
  </script>
  