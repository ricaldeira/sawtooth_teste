<template>
    <div>
       <CarList :cars="loadedCars"/>
       
    </div>
</template>

<script>
import CarList from '@/components/Car/CarList'
export default {
    components:{CarList},

    fetch({store}){
        store.dispatch("cars/getCars")        
    },
    computed:{
        loadedCars(){
            
            return this.$store.getters["cars/loadedCars"]
        }
    }
   
}
</script>