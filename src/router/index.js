import { createRouter, createWebHashHistory } from 'vue-router'
import DisneyView from '../views/DisneyView.vue'
import PixarView from '../views/PixarView.vue'
import GhibliView from '../views/GhibliView.vue'
import PacmanView from '../views/PacmanView.vue'
import LegoView from '../views/LegoView.vue'
import MarioView from '../views/MarioView.vue'

const routes = [
    {
        path: '/',
        redirect: '/disney'
    },
    {
        path: '/disney',
        name: 'Disney',
        component: DisneyView
    },
    {
        path: '/pixar',
        name: 'Pixar',
        component: PixarView
    },
    {
        path: '/ghibli',
        name: 'Ghibli',
        component: GhibliView
    },
    {
        path: '/pacman',
        name: 'Pacman',
        component: PacmanView
    },
    {
        path: '/lego',
        name: 'Lego',
        component: LegoView
    },
    {
        path: '/mario',
        name: 'Mario',
        component: MarioView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
