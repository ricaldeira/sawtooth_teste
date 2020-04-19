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
    }
}