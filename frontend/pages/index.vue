<template>
  <div class="container">
    <form @submit.prevent="onSave">

      <AppControlInput v-model="editedAgent.name">Agent Name</AppControlInput>

      <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onSave">
        Save
      </AppButton>

       <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="other">
        Other
      </AppButton>
    </form>
    <ul>
      <li v-for="agent in loadedAgents" :key="agent.id">
          {{agent.id}} | {{agent.name}}
      </li>
    </ul>
  </div>
</template>

<script>

import AppButton from '@/components/UI/AppButton'
import AppControlInput from '@/components/UI/AppControlInput'
export default {
  components: {
    AppButton, AppControlInput
  },
  asyncData(context){
    //return this.$store.state.agents.loadedAgents
  },
  methods: {
    async other(){
      this.$store.dispatch('agents/getAgents');
    },
    onSave(editedAgent){
      this.$store.dispatch('agents/editAgent', this.editedAgent)
        .then(() =>{
          console.log("OK");
        })
    }
  },
  computed:{
    loadedAgents(){
      console.log("Retornando loadedAgents")
      //this.$store.d
      const loadedAgents = [];
      //return loadedAgents
      return this.$store.state.agents.loadedAgents
    }    
  },
  props: {
    agent: {
      type: Object,
      required: false
    }
  },
   data(){
     return {
       editedAgent: this.agent ? {... this.agent } : {name: ""}
     }
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
