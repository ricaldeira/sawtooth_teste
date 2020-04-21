<template>
    <section class="agent-list">
     <div>
      <table class="table">
          <thead>
              <tr>
                  <th>
                      Númer
                  </th>

                  <th>
                      Header_Signature
                  </th>
                  <th></th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="block in loadedBlocks.blocks" :key="block.header_signature">
                    <td>{{block.block_num}} </td>
                    <td>{{block.header_signature}} </td>
                    <!-- <td>{{agent.public_key}} </td> -->
                    
                    <td><nuxt-link :to="{name: 'blocks-id', params: {id: block.header_signature} }"> >>  </nuxt-link></td>
               </tr>   
          </tbody>
      </table>
  </div>
    
    </section>

</template>

<script>
import {mapMutations, mapGetters} from "vuex"
// import AgentPreview from '@/components/Agent/AgentPreview'

export default {   
    props: {
        loadedBlocks: {
            type: Object,
            required: true
        }
    },
    mounted(){
        console.log("loaded", this.loadedBlocks)
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

