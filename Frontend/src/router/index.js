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
            path: '/Merchants',
            component: () => import('../views/Merchants.vue')
        },
        
        //route to updateMerchant vue
        {
            path: '/updateMerchant/:id',
             name: 'updateMerchant',
             component: () => import('../views/updateMerchant.vue')
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
        },
        {
            path: '/sevenOneReport',
            name: 'sevenOneReport',
            component: () => import('../views/sevenOneReport.vue')
        }
    ]
})

export default router