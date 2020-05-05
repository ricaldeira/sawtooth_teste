<template>
    <div>
        
        <section class="car-list">
            <CarPreview v-for="car in cars" 
                    :key="car.chassis"
                    :chassis="car.chassis"
                    :license="car.license"/>
        </section>
    </div>

</template>

<script>
// import {mapMutations, mapGetters} from "vuex"
import CarPreview from "@/components/Car/CarPreview"

export default {    
    components: { CarPreview },
    middleware: ["auth", "check-auth"],
    props: {
        cars: {
            type: Array,
            required: true
        }
    }
}
</script>


<style scoped>

.car-list {
  display: flex;
  padding: 20px;
  box-sizing: border-box;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
</style>

