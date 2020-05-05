<template>
    <div class="section">
        <form @submit.prevent="">
            <div class="file has-name is-fullwidth">
                <label class="file-label">
                    <input class="file-input" type="file" name="resume" @change="onFileChanged">
                    <span class="file-cta">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label">
                        Choose a file…
                    </span>
                    </span>
                    <span class="file-name" v-if="selectedFile !== null" >
                        {{selectedFile.name}}
                    </span>
                </label>
                <button class="button is-primary"  @click="onUpload"> Upload </button>
            </div>

            
            <!-- <input type="file" @change="onFileChanged"> -->
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