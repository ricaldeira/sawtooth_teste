<template>
    <div class="section">
        <form @submit.prevent="">
            <input type="file" @change="onFileChanged">
            <button @click="onUpload"> Upload </button>
        </form>
    <DocumentList :loadedDocuments="loadedDocuments" />

    </div>
</template>

<script>
import DocumentList from '@/components/Document/DocumentList'
export default {
    components: {DocumentList},
    middleware: ["auth", "check-auth"],
    data(){
        return {
            selectedFile: null
        }
    },
    
    fetch({store}){
        store.dispatch("documents/getAllDocuments")        
    },
    computed:{
        loadedDocuments(){                        
            return this.$store.getters["documents/loadedDocuments"]
        }
    },
    methods:{
        onFileChanged(event){
            const file = event.target.files[0]
            this.selectedFile = file
        },
        onUpload(){
            this.$store.dispatch("documents/uploadFile", this.selectedFile)
                .then(res => {
                    this.$store.dispatch("documents/getAllDocuments")   
                })
            //retunr hash file from rest-api
            //axios.post('localhost/file_upload', this.selectedFile)

        }
    }
}
</script>