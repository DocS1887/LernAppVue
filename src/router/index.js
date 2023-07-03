import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Lesen from '../views/lesen.vue'
import Rechnen from '../views/rechnen.vue'
import Buchstabenlesen from '../views/BuchstabenLesen.vue'
import Woerterlesen from '../views/Woerterlesen.vue'
import Leseteppich from '../views/LeseTeppich.vue'
import GeschichtenLesen from '../views/geschichtenLesen.vue'
import ZahlenLesen from '../views/zahlenLesen.vue'
import Testung from '../views/testung.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/lesen',
      name: 'Lesen',
      component: Lesen
    },
    {
      path: '/rechnen',
      name: 'Rechnen',
      component: Rechnen
    },
    {
      path: '/testen',
      name: 'Testung',
      component: Testung
    },
    {
      path: '/buchstabenlesen',
      name: 'Buchstabenlesen',
      component: Buchstabenlesen
    },
    {
      path: '/woerterlesen',
      name: 'Woerterlesen',
      component: Woerterlesen
    },
    {
      path: '/leseteppich',
      name: 'LeseTeppich',
      component: Leseteppich
    },
    {
      path: '/geschichtenlesen',
      name: 'GeschichtenLesen',
      component: GeschichtenLesen
    },
    {
      path: '/zahlenlesen',
      name: 'ZahlenLesen',
      component: ZahlenLesen
    },


  ]
})

export default router
