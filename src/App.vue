<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="container text-center">
    <div class="row">
        <h1>Hallo Ben und willkommen auf deiner Lernseite</h1>
        <nav>
          <RouterLink to="/">Start</RouterLink>
          <RouterLink to="/lesen">Lesen</RouterLink>
          <RouterLink to="/rechnen">Rechnen</RouterLink>
        </nav>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
h1 {
    text-align: center;
    font-family: Bubblegum;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  margin-top: 2rem;
}
 
nav {
  width: 100%;
  font-size: 2rem;
  text-align: center;
  margin-left: 1rem;  
  margin-bottom: 1rem;
  font-family: Ubuntu;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;

  }
}
</style>
