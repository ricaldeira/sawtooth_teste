
export default {

    getBlocks(context){        
        return this.$axios.$get('/api-validator/blocks')
            .then(res => {
                var loadedBlocks = {
                    blocks: [],
                    link: "",
                    head: ""
                }
                
                loadedBlocks.link = res.link;
                loadedBlocks.head = res.head;          
                for (const key in res.data){
                    var  block = {
                        header_signature: null,
                        block_num: 0
                    }
                    block.header_signature = res.data[key]['header_signature'];
                    block.block_num = res.data[key]['header']['block_num'];
                    loadedBlocks.blocks.push(block)                    
                }                    
                context.commit("setBlocks", loadedBlocks)
            });
    }
}