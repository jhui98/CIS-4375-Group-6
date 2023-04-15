<template>
    <aside :class="`${is_expanded ? 'is-expanded' : ''}`">
        <div class="logo">
            <img src="../assets/ovvi final.png" alt="Vue">
        </div>
        
         <!-- <div class="menu-toggle-wrap">
            <button class="menu-toggle" @click="ToggleMenu">
                <span class="material-icons">keyboard_double_arrow_right </span>
            </button>
         </div> -->
        <br>
         <h3>Menu</h3>
         <div class="menu">
            <router-link class="button" to="/home">
                <span class="material-icons">home</span>
                <span class="text">Home</span>
            </router-link>
            <router-link class="button" to="/orders">
                <span class="material-icons">shopping_bag</span>
                <span class="text">Orders</span>
            </router-link>
            <br>
            <br>
            <router-link class="button" to="/merchants">
                <span class="material-icons">store</span>
                <span class="text">Merchants</span>
            </router-link>
            <router-link class="button" to="/resellers">
                <span class="material-icons">storefront</span>
                <span class="text">Resellers</span>
            </router-link>
            <router-link class="button" to="/iso">
                <span class="material-icons">business_center</span>
                <span class="text">ISOs</span>
            </router-link>
            <br>
            <br>
            <router-link class="button" to="/hardware">
                <span class="material-icons">memory</span>
                <span class="text">Hardware</span>
            </router-link>
            <router-link class="button" to="/hardwaretype">
                <span class="material-icons">category</span>
                <span class="text">Hardware Type</span>
            </router-link>
         </div>

    </aside>
</template>

<script setup>
import {ref} from 'vue'




const is_expanded = ref(localStorage.getItem("is_expanded") === "true")

const ToggleMenu = () => {
    is_expanded.value = !is_expanded.value

    localStorage.setItem("is_expanded", is_expanded.value)
}




</script>

<style lang="scss" scoped>
aside {
    display: flex;
    flex-direction: column;
    width: calc(2rem + 32px);
    overflow: hidden;
    min-height: 100vh;
    padding: 1rem;
    
    background-color: var(--dark);
    color: var(--light);

    transition: 0.2s ease-out;

    .logo {
        margin-bottom: 2rem;

        img {
            width: 5rem;
        }
    }

    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 1rem;

        position:relative;
        top:0;
        transition: 0.2s ease-out;

        .menu-toggle {
            transition: 0.2s ease-out;

            .material-icons {
                font-size: 2rem;
                color: var(--light)
            }

            &:hover {
                .material-icons {
                    color: var(--primary);
                    transform: translateX(0.5rem);
                    transition: 0.2s ease-out;
                }
            }
            
        }
    }

    h3, .button .text {
        opacity: 0;
        transition: 0.3s ease-out;
    }

    h3 {
        color: var(--grey);
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }

    .menu {
        margin: 0 -1rem;

        .button {
            display: flex;
            align-items: center;
            text-decoration: none;

            padding: 0.5rem 1rem;
            transition: 0.2 ease-out;

            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 0.2s ease-out;
            }

            .text {
                color: var(--light);
            }

            &:hover, &.router-link-exact-active {
                background-color: var(--dark-alt);

                .material-icons, .text {
                    color: var(--primary);
                }
            }

            &.router-link-exact-active {
                border-right: 5px solid var(--primary);
            }

        }
    }


    &.is-expanded {
        width: var(--sidebar-width);

        .menu-toggle-wrap {
            top: -3rem;
            .menu-toggle{
            transform: rotate(-180deg);
            }
        }

        h3, .button .text{
        opacity: 1;
        }
        .button {
            .material-icons {
                margin-right: 1rem;
            }
        }
    }

    
    
    @media (max-width: 786px) {
        position: fixed;
        z-index: 99;
    }
}
</style>
