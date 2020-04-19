<template>
    <div class="section">
        <form @submit.prevent="">
            <input type="file" @change="onFileChanged">
            <button @click="onUpload"> Upload </button>
        </form>

    </div>
</template>

<script>
export default {
    middleware: ["auth", "check-auth"],
    data(){
        return {
            selectedFile: null
        }
    },
    methods:{
        onFileChanged(event){
            console.log("Arquivo selectionado")
            console.log(this.selectedFile)
            const file = event.target.files[0]
            this.selectedFile = file
        },
        onUpload(){
            console.log("Arquivo selectionado")
            console.log(this.selectedFile)
            this.$store.dispatch("documents/uploadFile", this.selectedFile)
                .then(res => {
                    console.log("Retornando na página de upload", res)
                })
            //retunr hash file from rest-api
            //axios.post('localhost/file_upload', this.selectedFile)

        }
    }
}
</script>