export default {
    setAgents (state, agents){
        state.loadedAgents = agents;
    },
    setToken (state, token){
        state.token = token;
    },
    clearToken(state){
        state.token = null;
    },    

}