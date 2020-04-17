<template>
  <div class="container">
    <form @submit.prevent="onSave">

      <AppControlInput v-model="agent.name">Agent Name</AppControlInput>
      <AppControlInput v-model="agent.password">Password</AppControlInput>

      <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onSave">
        Save
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
  methods: {
    onSave(agent){
      this.$store.dispatch('agents/createAgent', this.agent)
        .then(() =>{
          console.log("OK");
        })
    }
  },
  data(){
     return {
       agent: {
           name: "",
           password: ""
        }
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
