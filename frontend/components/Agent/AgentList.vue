<template>
    <section class="agent-list">
        <!-- <AgentPreview v-for="agent in agents" 
                :key="agent.public_key"
                :public_key="agent.public_key"
                :name="agent.name"/>
     -->
     <div>
      <table class="table">
          <thead>
              <tr>
                  <th>
                      Nome
                  </th>

                  <th>
                      Public Key
                  </th>
                  <th></th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="agent in agents" :key="agent.public_key">
                    <td>{{agent.name}} </td>
                    <td>{{agent.public_key}} </td>
                    <td><nuxt-link :to="{name: 'agents-id', params: {id: agent.public_key} }"> >>  </nuxt-link></td>
               </tr>   
          </tbody>
      </table>
  </div>
    
    </section>

</template>

<script>
import {mapMutations, mapGetters} from "vuex"
import AgentPreview from '@/components/Agent/AgentPreview'

export default {
    layout: "logged",
    components: { AgentPreview },
    middleware: ["auth", "check-auth"],
    props: {
        agents: {
            type: Array,
            required: true
        }
    },
    computed:{
        getLink(agent){
            return "agents/" + agent.public_key;
        }
    }    
}
</script>


<style scoped>

.agent-list {
  display: flex;
  padding: 20px;
  box-sizing: border-box;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
</style>

