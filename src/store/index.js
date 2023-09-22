// store/index.js
import { defineStore } from 'pinia';

export const useDarkModeStore = defineStore('darkMode', {
  state: () => ({
    isDarkMode: false
  }),
  actions: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
    }
  },
  getters: {
    getDarkModeState() {
      return this.isDarkMode;
    }
  }
});
