import React from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
const Logout = () => {
    const navigate = useNavigate()
    const loggingout = (e) => {
        e.preventDefault();
        fetch('/logout', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(),
        })
          .then((response) => {
            if (response.ok){
              alert("User has been logged out")
              navigate("/login")
              return response.json()
            }
          })
          .then((data) => {
            console.log(data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      };

      return(
        <div>
            <Link onClick={loggingout}>Logout</Link>
            
        </div>
      )

}

export default Logout
