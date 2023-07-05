import React from "react";
import { Link } from "react-router-dom";

const HardwareItem = ({ name, price, description,category }) => {
    // console.log(name)
    return (
        <div className="card">
            {/* <img src={image} alt={name}/> */}
            <div className="container">
                <p>{name}</p>
                <p>Kshs. {price}</p>
                <Link>Show more</Link>
                

            </div>
           
            
        </div>
    )

}

export default HardwareItem