import './App.css';
import React, {useEffect, useState} from "react"
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/SignUp';

function App() {
  const [hardwares, setHardwares] = useState([])
  useEffect(() => {
    fetch("/hardware")
    .then(res => res.json())
    .then(data => {
      setHardwares(data)
      // console.log(hardwares)
    })
  },[])
  
  
  return (
    <div>
      {/* <Login/> */}
      <Home data = {hardwares}/>
      {/* <Signup/> */}
     
    </div>
  );
}

export default App;
