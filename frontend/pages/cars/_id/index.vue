<template>

    <div class="level">
        
        <div class="tile is-ancestor">
            <div class="tile is-vertical is-8">
                <div class="tile">     
                    <div class="tile is-parent">
                        <article class="tile is-child notification is-info">
                            <div class="columns">
                                <div class="column">
                                        <p class="title">Modelo: xxx</p>
                                        <p class="subtitle">Marca: xx</p>
                                        <p class="subtitle">Ano: xxx</p>
                                        <p class="subtitle">Cor: xxx</p>
                                        
                                </div>
                                <div class="column is-one-quarter">
                                    <figure class="image is-128x128">
                                        <img src="https://bulma.io/images/placeholders/128x128.png">
                                    </figure>
                                </div>
                            </div>
                            
                            <p class="subtitle">Chassis # {{car.chassis}}</p>
                            <button class="button is-danger">            Voltar
                                 <span class="has-text-danger">
                                    <fa icon="back" />
                                </span>
                            </button>
                            <button class="button is-danger">            Peças
                                 <span class="has-text-warning">
                                    <fa icon="exclamation-triangle" />
                                </span>
                            </button>
                            
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