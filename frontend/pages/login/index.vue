<template>
    
      <div class="section">
        <form @submit.prevent="">

          <AppControlInput v-model="agent.name">Agent Public Key</AppControlInput>
          <AppControlInput type="password" v-model="agent.password">Password</AppControlInput>

          <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onSave">
            Login
          </AppButton>          
          <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onSignUp">
            Create Agent
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
    },
    onSignUp(){
      console.log("Iniciando criação")
      this.$store.dispatch('agents/createAgent', this.agent)
        .then(res => {

          this.$router.push("/agents");
        })
    }
  },
  data(){
     return {
       agent: {
           name: "03e0d699b6cdde1082b91ca056cdcdae54a1ee1b0d53a4ddd4480ce69c6b956cad",
           password: "123"
        }
     }
  }
}
</script>