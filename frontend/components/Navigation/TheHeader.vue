<template>
<nav class="navbar is-light" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
  
    <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">      
      <nuxt-link class="navbar-item" to="/" >Home</nuxt-link>
      <nuxt-link class="navbar-item" to="/documents" >Meus Documentos</nuxt-link>
      <nuxt-link class="navbar-item" to="/agents" >Agentes</nuxt-link>
      <nuxt-link class="navbar-item" to="/blocks" >Blockchain</nuxt-link>
     
<!--  <a class="navbar-item">
        Documentation
      </a>
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          More
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            About
          </a>
          <a class="navbar-item">
            Jobs
          </a>
          <a class="navbar-item">
            Contact
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
      </div> -->
    </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <div v-if="$store.getters['agents/isAuthenticated']"> 
              <AppButton type="button" :class="'is-warning'"                         
                        @click="onLogout">
                        Logout</AppButton>  

            </div>
            <div v-else>
              <AppButton type="button" :class="'is-primary'"
                        @click="onSignUp"> Sign Up </AppButton>  
              <AppButton type="button" :class="'is-light'"
                        @click="onLogin"> Login </AppButton>               
            </div>
            <!-- <div v-show="agents/isAuthenticated">
            </div> -->
            <!-- <div v-show="!agents/isAuthenticated">
              
            </div> -->
        </div>
      </div>
    </div>
    
  </div>
</nav>
<!-- <div class="header-container">
  <header class="the-header">
    <div class="navigation-items">
      <ul class="nav-list">
        <li class="nav-item"><nuxt-link to="/posts">Blog</nuxt-link></li>
        <li class="nav-item"><nuxt-link to="/about">About</nuxt-link></li>
        <li class="nav-item"><nuxt-link to="/admin">Admin</nuxt-link></li>
        <AppButton type="button" style="margin-left: 10px" btn-style="save" @click="onLogout">
        Logout
      </AppButton>
      </ul>
    </div>
  </header>
</div> -->
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: "TheHeader",
  methods:{
    onLogout(){
      this.$store.dispatch('agents/logout')
        .then(() =>{
          this.$router.push("/login")          
        })
        .catch(e => console.log(e))
    },
    onSignUp(){
      this.$router.push("/login")
    },
    onLogin(){
      this.$router.push("/login")
    }
  },
  data(){
    return {
      isAuthenticated:  this.$store.getters['agents/isAuthenticated']      
    }
  },
  // computed: {    
  //     ...mapGetters(['agents/isAuthenticated'])
    
    
  // }
};
</script>



<style scoped>
.header-container {
  height: 60px;
}

.the-header {
  width: 100%;
  position: fixed;
  height: 60px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: black;
  z-index: 100;
  box-sizing: border-box;
  padding: 0 20px;
}

.logo {
  margin: 0 10px;
  font-size: 1.3rem;
}

.logo a {
  text-decoration: none;
  color: white;
}

.spacer {
  flex: 1;
}

.navigation-items {
  display: none;
}

@media (min-width: 768px) {
  .navigation-items {
    display: block;
  }
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

.nav-item {
  margin: 0 10px;
}

.nav-item a {
  text-decoration: none;
  color: white;
}

.nav-item a:hover,
.nav-item a:active,
.nav-item a.nuxt-link-active {
  color: red;
}
</style>
