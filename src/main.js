import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { useDarkModeStore } from './store'

const pinia = createPinia(useDarkModeStore);
const app = createApp(App)

app.use(router);
app.use(pinia);
app.mount('#app')

