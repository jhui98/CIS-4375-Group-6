import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/home',
            component: () => import('../views/Home.vue')
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
            path: '/updatehardware/:id',
            name: 'updatehardware',
            component: () => import('../views/updatehardware.vue')
        },
        //route to updateMerchant vue
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
         //route to Orders vue
        {
            path: '/Orders',
            component: () => import('../views/Orders.vue')
        },
        //route to updateOrder vue
        {
            path: '/updateOrder/:num',
             name: 'updateOrder',
             component: () => import('../views/updateOrder.vue')
        },
        {
            path: '/updatepart/:id',
            name: 'updatepart',
            component: () => import('../views/updatepart.vue')
        },
        {
            path: '/reports',
            component: () => import('../views/Reports.vue')
        },
        {
            path: '/sevenOneReport/:id',
            name: 'sevenOneReport',
            component: () => import('../views/sevenOneReport.vue')
        }
    ]
})

export default router