<template>
    <div class="section">
        <input type="file" @change="onFileChanged">
        <button @click="onUpload"> Upload </button>
        

    </div>
</template>

<script>
export default {
    data(){
        return {
            selectedFile: null
        }
    },
    methods:{
        onFileChanged(event){
            const file = event.target.files[0]
        },
        onUpload(){
            //retunr hash file from rest-api
            //axios.post('localhost/file_upload', this.selectedFile)

        }
    }
}
</script>