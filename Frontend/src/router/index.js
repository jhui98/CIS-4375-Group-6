import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/hardware',
            component: () => import('../views/Hardware.vue')
        },
        {
            path: '/hardwaretype',
            component: () => import('../views/HardwareType.vue')
        },
        {
            path: '/updatehardwaretype/:id',
            name: 'updatehtype',
            component: () => import('../views/updatehtype.vue')
        },
        {
            path: '/merchants',
            component: () => import('../views/Merchants.vue')
        },
        //route to addMerchant vue
        {
            path: '/addMerchant',
            component: () => import('../views/addMerchant.vue')
        },

        {
            path: '/resellers',
            component: () => import('../views/Resellers.vue')
        },
        {
            path: '/updatereseller/:id',
            name: 'updatereseller',
            component: () => import('../views/updatereseller.vue')
        },
        {
            path: '/iso',
            component: () => import('../views/iso.vue')
        },
        {
            path: '/updateiso/:id',
            name: 'updateiso',
            component: () => import('../views/updateiso.vue')
        },
        {
            path: '/orders',
            component: () => import('../views/Orders.vue')
        },
        {
            path: '/reports',
            component: () => import('../views/Reports.vue')
        }
    ]
})

export default router