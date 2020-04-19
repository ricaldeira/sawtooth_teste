<template>

  <nuxt-link to="agents" class="agent-preview">
    <article>      
      <div class="agent-content">
        <h1>{{ public_key }}</h1>
        <p>{{ name }}</p>
      </div>
    </article>
  </nuxt-link>
 
</template>

<script>
export default {
    name: 'AgentPreview',
    props:{
        public_key:{
            type: String,
            required: true,
        },
        name:{
            type: String,
            required: true,
        },
        
    }
}
</script>
<style scoped>
.agent-preview {
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
  .agent-preview {
    width: 400px;
    margin: 10px;
  }
}

.agent-content {
  padding: 10px;
  text-align: center;
}

a:hover .agent-content,
a:active .agent-content {
  background-color: #ccc;
}
</style>
