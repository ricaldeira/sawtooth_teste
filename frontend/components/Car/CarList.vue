<template>
    <div>
        
        <section class="car-list">
            <table class="table is-hoverable is-fullwidth">
                <thead>
                    <tr>
                        <th>Chassis</th>
                        <th>License</th>
                        <th colspan="2"></th>
                    </tr>
                </thead>
                <tfoot>
                    <tr>
                        <th>Chassis</th>
                        <th>License</th>
                        <th colspan="2"></th>
                    </tr>
                </tfoot>
                <tbody>
                    <CarPreview v-for="car in cars" 
                            :key="car.chassis"
                            :chassis="car.chassis"
                            :license="car.license"/>
                </tbody>
            </table>
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

