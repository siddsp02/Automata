// import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [symbols, setSymbols] = useState([]);

  return (
    <div>
      <label for="states">States</label>
      <input type="number" name="states" onChange=""></input>
    </div>
  );
}

export default App;
