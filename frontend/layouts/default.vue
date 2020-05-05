<template>
    <div>
            <TheHeader/>            
            <section class="section">
            <div class="container">                                
                <nuxt />
            </div>           
            </section>

    </div>
</template>

<script>
import TheHeader from '@/components/Navigation/TheHeader'
export default {
    components:{
        TheHeader
    }
}
</script>

<style>
html {
    font-family: 'Open Sans', sans-serif;
}

body {
    margin:0;
}
</style>