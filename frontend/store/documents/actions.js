export default {
    uploadFile(context, arquivo){
        const token = localStorage.getItem("token")        
        this.$axios.setToken(token, 'Bearer')
        this.$axios.setHeader('Content-Type', 'multipart/form-data', [
            'post'
          ])
        var formData = new FormData();
        const document_obj = {
            document: arquivo
        }
        formData.append('file', arquivo)
        console.log(formData)
        
        return this.$axios.$post('/api/documents', formData)
            .then(res => {
                console.log("Retornando do POST documentos", res);
            })
    },
    getAllDocuments(context){
        return this.$axios.$get('/api/documents')
            .then(res => {
                console.log("RES GET ALL:::", res)
                const documentsArray = []
                for(const key in res){                    
                    let doc = {
                        id: res[key]['id'],
                        document_hash: res[key]['document_hash'],
                        file_name: res[key]['file_name']
                    }
                    documentsArray.push({...doc})
                }
                context.commit("setDocuments", documentsArray)
            })
            .catch(e => context.error(e) );
    },

    isValid(context, document){
        console.log("Em action", document.document_hash)
        return this.$axios.$get('/api-validator/state/' + document.document_hash)
            .then(res => {
                console.log(res.data)
                console.log(res.data['statusText'])

            })
    }
}