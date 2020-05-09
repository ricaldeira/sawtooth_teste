<template>
    <div>
        <input
            :value="search"
            @input="handleSearch"
            type="search"/>

        <CarList :cars="loadedCars"/>
       
    </div>
</template>

<script>
import CarList from '@/components/Car/CarList'
import { debounce } from '~/helpers/index'

export default {
    components:{CarList},

    fetch({store}){
        store.dispatch("cars/getCars")        
    },
    methods: {       
        handleSearch: debounce(function (e) {
            this.$store.dispatch('cars/filterSearch', e.target.value)            
            }, 500
        ),
       
    },
    computed:{
        loadedCars(){            
            return this.$store.getters["cars/filteredCars"]
        },
        search(){
            return this.$store.state["cars/filter.search"]
        }
        
    }
   
}
</script>