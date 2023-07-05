import React from "react";
import HardwareItem from "./HardwareItem";

const Home = ({data}) => {
    const hardwarelist = []
    Object.values(data).map((hardware) => {
            hardware.map(item => {
                // console.log(item)
                hardwarelist.push(item)
                return hardwarelist
            })
            return hardware
    })
    // console.log(hardwarelist)
    const displayData = hardwarelist.map(item => {
        // console.log(item)
        return <HardwareItem key = {item.id} name = {item.name} price = {item.price} description ={item.description} category = {item.category}  />
    })
    return(
        <div className="cardlist">
            {displayData}
        </div>
    )
}

export default Home