import React from "react";

const HardwareItem = ({ name, price, description,category }) => {
    // console.log(name)
    return (
        <div>
            {/* <img src={image} alt={name}/> */}
            <p>{name}</p>
            <p>Kshs. {price}</p>
            <p>{description}</p>
            <p>{category}</p>
        </div>
    )

}

export default HardwareItem