export default {
    setBlocks(state, blocks){
        console.log("Blocks em state", blocks)
        state.loadedBlocks = blocks
    }
}