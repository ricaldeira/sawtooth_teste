<template>
    <section class="agent-list">
     <div>
      <table class="table">
          <thead>
              <tr>
                  <th>
                      Número
                  </th>

                  <th>
                      Nome
                  </th>

                  <th>
                      Hash
                  </th>
                  <th></th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="document in loadedDocuments" :key="document.document_hash">
                    <td>{{document.id}} </td>
                    <td>{{document.file_name}} </td>
                    <td>{{document.document_hash}} </td>
                    <!-- <td>{{agent.public_key}} </td> -->                    
                    <td> <AppButton @click="onIsValidDocument(document)">Verificar</AppButton> </td>
                    
                    <!-- <td><nuxt-link :to="{name: 'blocks-id', params: {id: block.header_signature} }"> >>  </nuxt-link></td> -->
               </tr>   
          </tbody>
      </table>
  </div>
    
    </section>

</template>

<script>
import {mapMutations, mapGetters} from "vuex"
// import AgentPreview from '@/components/Agent/AgentPreview'
import AppButton from '@/components/UI/AppButton'
export default {   
    components:{
        AppButton
    },
    props: {
        loadedDocuments: {
            type: Array,
            required: true
        }
    },
    methods: {
        onIsValidDocument(document) {            
            this.$store.dispatch("documents/isValid", document)
        }
    },

    mounted(){
        // console.log("loaded", this.loadedDocuments)
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

