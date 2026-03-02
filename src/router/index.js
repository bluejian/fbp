import { createRouter, createWebHashHistory } from 'vue-router'
import ForestView from '../views/ForestView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: ForestView
    },
    {
        path: '/forest',
        name: 'Forest',
        component: ForestView
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
