import './App.css';
import {React, useEffect, useState} from "react"
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/SignUp';

function App() {
  const [data, setData] = useState([])
  useEffect(() => {
    fetch("/hardware")
    .then(res => res.json())
    .then(data => {
      setData(data)
      console.log(data)})
  },[])
  
  
  return (
    <div className="App">
      <Login/>
      <Home data = {data}/>
      <Signup/>
     
    </div>
  );
}

export default App;
