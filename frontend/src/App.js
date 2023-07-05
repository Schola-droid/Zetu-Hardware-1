import './App.css';
import React, {useEffect, useState} from "react"
import { Route,Routes } from 'react-router';
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
      <Routes>
        <Route path='/login' element={<Login/>}></Route>
        <Route path='/' element={<Home data = {hardwares}/>}></Route>
        <Route path='/signup' element={<Signup />}></Route>
      </Routes>     
    </div>
  );
}

export default App;
