// store/index.js
import { defineStore } from 'pinia';

export const useDarkModeStore = defineStore('darkMode', {
  state: () => ({
    isDarkMode: false,
    localDarkMode: false
  }),
  actions: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      this.localDarkMode = this.isDarkMode;
    },
    setLocalDarkModeState(newState) {
      this.localDarkMode = newState;
    }
  },
  getters: {
    getDarkModeState() {
      return this.isDarkMode;
    },
    getLocalDarkModeState() {
      return this.localDarkMode;
    }
  }
});
