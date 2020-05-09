export function filterCars(filter, cars){
    let filteredList = [...cars]
    if (filter.status !== 'all'){
        const filtered = filteredList.filter(car => 
             car.chassis === filter.chassis
        )
        filteredList = filtered
    }

    if (filter.search !== ''){
        const searchList = []
        const searchTerm = filter.search.toLowerCase()
        for (let i = 0; i < filteredList.length; i++){
            if (
                (filteredList[i].chassis !== null && 
                        filteredList[i].chassis.toLowerCase().includes(searchTerm))
            ){
                searchList.push(filteredList[i])
            }
        }
        filteredList = searchList
    }
    return filteredList
}