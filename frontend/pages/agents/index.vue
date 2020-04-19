<template>
    <div>
        <AgentList :agents="loadedAgents"/>
    </div>
</template>

<script>
import {mapMutations, mapGetters} from "vuex"
import AgentList from '@/components/Agent/AgentList'
export default {
    // layout: "logged",
    components: {AgentList},
    middleware: ["auth", "check-auth"],
    
    fetch({store}){
        store.dispatch("agents/loadAgents")
    },  
    computed: {    
        loadedAgents(){
            return this.$store.getters["agents/loadedAgents"]                
        }            
    
    }
    
}
</script>