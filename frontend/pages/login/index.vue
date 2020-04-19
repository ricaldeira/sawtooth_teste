<template>
    
      <div class="section">
        <form @submit.prevent="onSave">

          <AppControlInput v-model="agent.name">Agent Public Key</AppControlInput>
          <AppControlInput type="password" v-model="agent.password">Password</AppControlInput>

          <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onSave">
            Login
          </AppButton>
          
        </form>
        </div> 
    
    
  
</template>

<script>
import AppButton from '@/components/UI/AppButton'
import AppControlInput from '@/components/UI/AppControlInput'

export default {
  components: {
    AppButton, AppControlInput
  },
  // middleware: ["check-auth", "auth"],
  methods: {
    onAgents(){
      this.$router.push("/agents")
    },
    onSave(agent){
      const credentials = {
        public_key: this.agent.name,
        password: this.agent.password
      }
      this.$store.dispatch('agents/login', credentials)
        .then(() =>{
          //console.log("Redirecionando..")
          this.$router.push("/agents")          
        })
        .catch(e => console.log(e))
    }
  },
  data(){
     return {
       agent: {
           name: "025cd0b750de14b3bed2aea51b1c5bc3281808bf9ee1ada3462a025bdcec44619b",
           password: "321"
        }
     }
  }
}
</script>