import React from "react";
import HardwareItem from "./HardwareItem";

const Home = ({data}) => {
    // var hardwares = Object.values(data)
    console.log(typeof(data))
    // data.map
    // console.log(Object.keys[data])
    // var sample = 
    // const displayData = data.map(hardware => {
    //     // return <HardwareItem name = {hardware.name} price = {hardware.price} description ={hardware.description} category = {hardware.category}  />
    //     console.log(hardware.category)
    //     // console.log(hardware)

    //     // console.log(hardware.price)
    // })
    // console.log(Object.entries(data))
    // const displayData = (data) => Object.entries(data).forEach(([key,value]) => {
    //     console.log(key,value)
    //   })


    return(
        <div>
            {/* {displayData} */}
        </div>
    )

}

export default Home