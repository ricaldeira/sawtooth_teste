<template>
    <tr>
        <td>{{chassis}}</td>
        <td>{{license}}</td>
        <td>
            <nuxt-link :to="carLink">
            <span class="icon has-text-danger">
                <fa icon="ban" />
            </span>
            </nuxt-link>
            <span class="has-text-warning">
                <fa icon="exclamation-triangle" />
            </span>
        </td>
    </tr>

  <!-- <nuxt-link to="cars">
      <div class="card">
          <div class="card-content">
              <div class="content">
                    Chassis {{chassis}}
              </div>
              <div class="content">
                     Licença {{license}}
              </div>
          </div>
      </div> -->
    <!-- <article>      
      <div class="car-content">
        <span class="has-text-info">
            <fa icon="info-circle" />
        </span>
        <span class="has-text-warning">
            <fa icon="exclamation-triangle" />
        </span>
        <span class="icon has-text-danger">
            <fa icon="ban" />
         </span>
        
      </div>
    </article> -->
  
 
</template>

<script>

export default {
    name: 'CarPreview',
    props:{
        
        chassis:{
            type: String,
            required: true,
        },
        license:{
            type: String,
            required: false,
        },        
    },
    computed:{
        carLink() {
            return "/cars/" + this.chassis
        }
    }

}
</script>
