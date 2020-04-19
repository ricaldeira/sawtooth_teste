export default {
    loadedAgents(state){
        return state.loadedAgents;
    },
    
    isAuthenticated(state){
        //console.log("STATE IS AUTH", state)
        return state.token != null
    }
}