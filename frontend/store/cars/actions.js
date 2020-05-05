export default{
    getCars(context){
        return this.$axios.$get('/api/cars')
            .then(res => {
                const carsArray = []
                 for (const key in res){
                     carsArray.push(res[key])
                }
                context.commit("setCars", carsArray);
            })
            .catch(e => {
                context.error(e);
            })
    },

    getCarByChassi(context, chassi){
        return this.$axios.$get('/api/cars/' + chassi)
            .then(res => {
                console.log("Getting CAR:::")
                let car = {
                    chassis: res.chassis,
                    license: res.license                
                }                
                context.commit("setCar", car)                
            })
        
    }
}