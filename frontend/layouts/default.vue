<template>
    <div>
            <TheHeader/>
            <div class="container">
                <nuxt />
            </div>

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