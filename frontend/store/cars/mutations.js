import * as Filters from '~/helpers/filters'
export default{
    setCars(state, cars){
        state.loadedCars = cars;
    },
    setCar(state, car){
        state.car = car
    },

    filterCars(state){
        const cars = [...state.loadedCars]
        state.filteredCars = cars
        state.filteredCars = Filters.filterCars(state.filter, cars)
    },
    setFilterSearch (state, search) { 
        state.filter.search = search 
    },



    
}