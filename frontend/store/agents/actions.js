import Cookie from "js-cookie";

export default {
    getAgents(context){
        return this.$axios.$get('/api/agents')
            .then(res => {
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
    gravaToken(token){
        context.commit("setToken", token)
        localStorage.setItem("token", token)    
        const expirationDate = new Date().getTime() + 3600
        localStorage.setItem("tokenExpiration", expirationDate)
        Cookie.set("jwt", token)
        Cookie.set("tokenExpiration", expirationDate)
    },
    createAgent(context, agent){
        console.log("Criando agente")
        return this.$axios.post("/api/agents", agent)
            .then(data => {
                const token = data['authorization'];
                context.commit("setToken", token)
                localStorage.setItem("token", token)    
                const expirationDate = new Date().getTime() + 3600
                localStorage.setItem("tokenExpiration", expirationDate)
                Cookie.set("jwt", token)
                Cookie.set("tokenExpiration", expirationDate)     
            }).catch(e => {
                console.log("Erro",e.error )
            })  
    },
    loadAgents(context){
        return this.$axios.get("/api/agents")
            .then(res => {                
                const agents = [];
                for ( const key in res.data ){
                    let new_agent = {
                        public_key: res.data[key]["public_key"],
                        name: res.data[key]["name"]
                    }
                    agents.push(new_agent)
                }
                context.commit("setAgents", agents)
            })        
    },

    initAuth(vuexContext, req){
        let token;
        if (req){
            if (!req.headers.cookies){
                return;
            }
            const jwtCookie = req.headers.cookie.split(";")
                .find(c => c.trim().startsWith("jwt="));
            if (!jwtCookie){
                return;
            }
            token = jwtCookie.split("=")[1];
        }
        else if (process.client){
            token = localStorage.getItem("token");
            if (!token){
                vuexContext.dispatch("logout")
                return;
            }         
        }
        vuexContext.commit("setToken", token);
    },

    logout(vuexContext){
        vuexContext.commit("clearToken");
        Cookie.remove("jwt");
        Cookie.remove("tokenExpiration");
        if (process.client){
            localStorage.removeItem("token")
            localStorage.removeItem("tokenExpiration")
        }
    },

    login(context, credentials){
        return this.$axios.$post("/api/authentication", credentials)        
            .then(data => {
                //gravaToken(data['authorization']);
                //vuexContext.redirect("/agents")
                const token = data['authorization'];
                context.commit("setToken", token)
                localStorage.setItem("token", token)    
                const expirationDate = new Date().getTime() + 3600
                localStorage.setItem("tokenExpiration", expirationDate)
                Cookie.set("jwt", token)
                Cookie.set("tokenExpiration", expirationDate) 
            })
            .catch(e => console.log("erro", e));
    }
}