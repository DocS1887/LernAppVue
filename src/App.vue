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
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" :checked="isDarkMode" @change="toggleDarkMode" />
          </div>        
        </div>
        <div class="col">
          <div class="login d-flex justify-content-end">
            <ul class="nav justify-content-center">
              <li class="nav-item">
                <template v-if="isLoggedIn">
                  <span style="display:inline-block;">{{ 'Hallo ' + this.username }}</span>
                  <span style="display: inline-block">
                    <a class="nav-link" @click="logout">ausloggen</a>
                  </span>
                </template>
                <template v-else>
                  <a v-if="!isLoggedIn" class="nav-link"><RouterLink to="/login">anmelden</RouterLink></a>
                  {{message}}
                </template>
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
              <nav ref="nav" @mouseleave="handleNavMouseLeave" @mouseenter="handleNavMouseEnter">
                <div class="slider" :style="{ transform: sliderTransform }"></div>
                <ul>
                  <li v-for="(element, index) in navigationElements" :key="index" @mouseenter="handleMouseEnter(index)">
                    <a><img :src="element.imageSrc" />
                      <router-link :to="element.route">{{ element.label }}</router-link>
                    </a>
                  </li>
                </ul>
              </nav>
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
  import axios from 'axios';
export default {
  data() {
    return {
      isSticky: false,
      username: '',
      isLoggedIn: false,
      message: '',
      isDarkMode: useDarkModeStore().getLocalDarkModeState,
      navigationElements: [
        { label: 'Start', imageSrc: 'https://assets.codepen.io/907368/security.svg', route: '/' },
        { label: 'Deutsch', imageSrc: 'https://assets.codepen.io/907368/learn.svg', route: '/lesen' },
        { label: 'Mathe', imageSrc: 'https://assets.codepen.io/907368/explore.svg', route: '/rechnen' },
        { label: 'Testung', imageSrc: 'https://assets.codepen.io/907368/support.svg', route: '/testen' },
      ],
      sliderTransform: 'translate(0, 0)',
      isAnimating: false,
      }
    },
    created(){
      this.checkloginStatus();

      const storedDarkmode = localStorage.getItem('darkmode');
      if(storedDarkmode !== null) {
        useDarkModeStore().setLocalDarkModeState(JSON.parse(storedDarkmode));
        this.isDarkMode = useDarkModeStore().getLocalDarkModeState;
      }
    },


  mounted() {

    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
  window.removeEventListener('scroll', this.handleScroll);
  },
  

  methods: {
    handleMouseEnter(index) {
      if (!this.isAnimating) {
        
        const element = this.$refs.nav.querySelectorAll('ul li')[index];
        const { x: elmX } = element.getBoundingClientRect();
        const { x: navX } = this.$refs.nav.getBoundingClientRect();

        this.sliderTransform = `translate(${elmX - navX}px, 0)`;
      }
    },
    handleNavMouseLeave() {
      this.isAnimating = true;
      this.$refs.nav.classList.remove('animate');
      setTimeout(() => {
        this.isAnimating = false;
      }, 50);
    },

    handleNavMouseEnter() {
      setTimeout(() => {
        this.isAnimating = true;
        this.$refs.nav.classList.add('animate');
        setTimeout(() => {
          this.isAnimating = false;
        }, 50);
      }, 50);
    },

    toggleDarkMode() {
      useDarkModeStore().toggleDarkMode();
      this.isDarkMode = useDarkModeStore().getLocalDarkModeState;
      localStorage.setItem('darkmode', JSON.stringify(this.isDarkMode));
      
    },
    handleScroll(){
    const scrollPosition = window.scrollY;
      if(scrollPosition > 0) {
      this.isSticky = true;
      } else {
      this.isSticky = false;
      };
    },
    checkloginStatus() {
      const token = localStorage.getItem('authToken');
      if(token) {
        this.isLoggedIn = true;
        this.username = localStorage.getItem('user')
      }
    },
    async logout() {
    try {
      const response = await axios.post('http://127.0.0.1:5000/logout') ;
        console.log(response.data.message);
        this.isLoggedIn = !this.isLoggedIn;
        localStorage.removeItem('user');
        localStorage.removeItem('authToken');
        localStorage.removeItem('user_id')
        window.location.reload();
    } catch (error) {
      console.error(error)
    }
    },

  }
};
</script>

<style>
body {
  background: linear-gradient(to top, lightblue, rgb(173, 182, 230));
}

nav {
  display: flex;
  position: relative;
}

nav.animate .slider {
  transition: all 350ms ease-in-out;
}

nav:hover .slider {
  opacity: 1;
}

nav .slider {
  margin-top: 0.8rem;
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  width: 9em;
  height: 70%;
  background-color: rgb(187, 173, 230);
  border-radius: 0.5rem;
  transition-delay: 150ms;
  transition: opacity 250ms ease;
}
nav ul {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin: 0;
  padding: 0;
}
nav ul li {
  list-style: none;
  position: relative;
}
nav ul li:hover a img {
  scale: 1;
  margin: 0 0.5rem 0 0;
}
nav ul li:hover ul {
  height: 8.5rem;
  opacity: 1;
}
nav ul li a {
  width: 9rem;
  padding: 0.8rem 1rem;
  border-radius: 1rem;
  font-size: 1rem;
  color: black;
  cursor: pointer;
  transition: all 350ms ease-in-out;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}
nav ul li a img {
  width: 1.2rem;
  height: 1.2rem;
  scale: 0;
  margin: 0 -2rem 0 0;
  transform-origin: -0.4rem 50%;
  transition: all 350ms ease-in-out;
}
nav ul li ul {
  position: absolute;
  overflow: hidden;
  top: 110%;
  width: 100%;
  height: 0;
  opacity: 0;
  transition: all 350ms ease-in-out;
  margin: 0;
  display: flex;
  flex-direction: column;
  background-color: white;
  border-radius: 1rem;
  gap: 0.1rem;
  padding: 0.2rem 0;
}
nav ul li ul li {
  padding: 0 0.2rem;
  margin: 0;
  width: 100%;
  list-style: none;
}
nav ul li ul li a {
  width: 100%;
  border-radius: 0.95rem;
  padding: 0.5rem 0.5rem;
}
nav ul li ul li a:hover {
  background-color: rgb(187, 173, 230);
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
