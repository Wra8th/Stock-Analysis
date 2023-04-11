import './App.css';
import Form from './components/form';
import React, {useState, useEffect} from 'react';
function App() {

    const [data, setcurrentQuote] = useState([]);

    useEffect(() => {
      fetch("/data")
      .then(response => response.json()
      .then(data => {
        setcurrentQuote(data)
        console.log(data)
      })
    )}, []);

  return (
    <div>
      {/* {data.buy.map((element, index )=> {
        return (
        <div key = {index}>
          <h2>{element}</h2>
          </div>
          )
     })} */}
     <h1>change: {data.change}</h1>
     <h2></h2>
     <Form />
    </div>
  );
}

export default App;
