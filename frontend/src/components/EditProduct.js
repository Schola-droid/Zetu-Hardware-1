import React, {useState}from "react";
import { useParams } from "react-router-dom";

const EditProduct = ({editProduct}) =>{
    const { id } = useParams()

    const [name, setName] = useState("")
    const [category, setCategory] = useState("")
    const [image, setImage] = useState("")
    const [price, setPrice] = useState("")
    const [description, setDescription] = useState("")
    const [customer_id, setCustomerID] = useState("")
    const [manufacturer_id, setManufacturerID] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        editProduct(id, name, category,image, price, description,customer_id,manufacturer_id)
    }
   
    
    return(
        <form onSubmit={handleSubmit}>
            <h3 style={{textAlign:"center"}}>Edit Product</h3>
            <label>name</label>
            <input type="text" id = "name" value = {name} onChange={e => setName(e.target.value)}/>
            <label>category</label>
            <input type="text" id = "category" value = {category} onChange={e => setCategory(e.target.value)}/>
            <label>image</label>
            <input type="text" id = "image" value = {image} onChange={e => setImage(e.target.value)}/>
            <label>price</label>
            <input type="text" id = "price" value = {price} onChange={e => setPrice(e.target.value)}/>
            <label>description</label>
            <input type="text" id = "description" value = {description} onChange={e => setDescription(e.target.value)}/>
            <label>customer_id</label>
            <input type="text" id = "customer_id" value = {customer_id} onChange={e => setCustomerID(e.target.value)}/>
            <label>manufacturer_id</label>
            <input type="text" id = "manufacturer_id" value = {manufacturer_id} onChange={e => setManufacturerID(e.target.value)}/>
            <button type="submit">Submit</button>

        </form>
    )
}

export default EditProduct