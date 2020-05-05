<template>

    <div class="level">
        
        <div class="tile is-ancestor">
            <div class="tile is-vertical is-8">
                <div class="tile">     
                    <div class="tile is-parent">
                        <article class="tile is-child notification is-info">
                        <p class="title">Carro</p>
                        <p class="subtitle">{{car.chassis}}</p>
                        <figure class="image is-128x128">
                            <img src="https://bulma.io/images/placeholders/128x128.png">
                        </figure>
                        </article>
                    </div>
                </div>                
            </div>        
        </div>
    </div>
</template>

<script>
export default {
    name: "CarIdPage",
    fetch({store, params}){
        console.log(params)
        store.dispatch("cars/getCarByChassi", params.id)       
    },
    computed:{
        car(){
           return this.$store.getters["cars/car"]
        }
    }
}
</script>