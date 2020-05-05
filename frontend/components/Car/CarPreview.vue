<template>
  <nuxt-link to="cars" class="car-preview">
    <article>      
      <div class="car-content">
        <h1>{{ chassis }}</h1>
        <p>{{ license }}</p>
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
    </article>
  </nuxt-link>
 
</template>

<script>
import { faJs } from '@fortawesome/free-brands-svg-icons'

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
    computed: {
    fab () {
      return {
        faJs
      }
    }
  }
}
</script>
<style scoped>
.car-preview {
  border: 1px solid #ccc;
  box-shadow: 0 2px 2px #ccc;
  background-color: white;
  width: 90%;
}

a {
  text-decoration: none;
  color: black;
}

@media (min-width: 850px) {
  .car-preview {
    width: 400px;
    margin: 10px;
  }
}

.car-content {
  padding: 10px;
  text-align: center;
}

a:hover .car-content,
a:active .car-content {
  background-color: #ccc;
}
</style>
