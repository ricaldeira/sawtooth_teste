export default {
    getAgents(context){
        return this.$axios.$get('/api/agents')
            .then(res => {
                console.log("*** Recuperando ***")
                console.log(res.data)
                const agentsArray = []
                for(const key in res.data){
                    console.log(res.data[key])
                    agentsArray.push({...res.data[key], id: key})
                }
                vueContext.commit("setAgents", agentsArray)
            })
            .catch(e => context.error(e) );
    },

    editAgent(context,agent){
        console.log("Em actions editAgente")
        console.log(context)
        console.log(agent)
        const createdAgent = {
            ...agent
        }
        this.$axios.$post("/api/agents", createdAgent)
            .then(data => {
                context.commit("addAgent", {...createdPost, id: data.name})
            })
    },

    createAgent(context, agent){
        this.$axios.$post("/api/agents", agent)
            .then(data => {
                context.commit("addAgent", {...agent, id: data.name})
            })  
    }
}