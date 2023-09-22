<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useDarkModeStore } from './store/index';
</script>

<template>
  <div :class="{'dark-mode': isDarkMode, 'bg-dark': isDarkMode,}">
    <div class="stickyHeader">
    <div class="banner-top">
      <div class="row">
        <div class="col">
          <div class="form-check form-switch">hell / dunkel
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked  @click="toggleDarkMode">
          </div>        
        </div>
        <div class="col">
          <div class="login d-flex justify-content-end">
            <ul class="nav justify-content-center">
              <li class="nav-item">
                <a class="nav-link"><RouterLink to="/login">anmelden</RouterLink></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <header class="header">
        <div class="container text-center" style="width: 100%">
          <div class="row">
            <div class="col d-flex">
              <h2 style="text-align: left;">Lernen macht Spass</h2>
            </div>
            <div class="col d-flex justify-content-end">
              <ul class="nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page">
                    <RouterLink to="/">Start</RouterLink></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link"><RouterLink to="/lesen">Deutsch</RouterLink></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link"><RouterLink to="/rechnen">Mathe</RouterLink></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link"><RouterLink to="/taschenrechner">Taschenrechner</RouterLink></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link"><RouterLink to="/testen">Testung</RouterLink></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
    </header>
  </div>

    <div class="content">
      <div class="inner-content">
        <RouterView />
      </div>
    </div>
    <footer class="footer">
      <ul class="nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link"><RouterLink to="/#">Impressum</RouterLink></a>
        </li>
      </ul>
    </footer>
  </div>
</template>

<script scoped>
export default {
  data() {
    return {
      isSticky: false,
      }
    },
  computed: {
    isDarkMode() {
      return useDarkModeStore().getDarkModeState;
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
  window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    toggleDarkMode() {
      useDarkModeStore().toggleDarkMode();
    },
    handleScroll(){
    const scrollPosition = window.scrollY;
      if(scrollPosition > 0) {
      this.isSticky = true;
      } else {
      this.isSticky = false;
      };
    },
  }
};
</script>

<style>
body {
  background-color: lightgray;
}
.nav-item {
  align-self: flex-end;
  
}

li a {
  color: black;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a.nav-link {
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

#flexSwitchCheckChecked{
  background-color: darkgray;
  border: none;
}
</style>
