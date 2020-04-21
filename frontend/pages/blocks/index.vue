<template>
    <div>
       <BlockList :loadedBlocks="loadedBlocks"/>
       
    </div>
</template>

<script>
import BlockList from '@/components/Block/BlockList'
export default {
    components:{BlockList},

    fetch({store}){
        store.dispatch("validator/getBlocks")
        console.log("dispatching")
    },
    computed:{
        loadedBlocks(){
            console.log("getting loadedBlocks")
            console.log(this.$store.getters["validator/loadedBlocks"])
            return this.$store.getters["validator/loadedBlocks"]
        }
    }
   
}
</script>