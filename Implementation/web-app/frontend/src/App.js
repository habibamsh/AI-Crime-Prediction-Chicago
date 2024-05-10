import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios';
import MapComponent from './components/MapComponent';
import ProductDropdown from './components/productDropdown';
import dropDownData from './data/dropDownData';
import data from './data/data';

const App = () => {
  const [date, setDate] = useState('');
  const [crimeType, setCrimeType] = useState('');
  const [highlightedAreas, setHighlightedAreas] = useState([]);
  
  const handleSubmit = async () => {
    try {
      if (date === '' && crimeType === '') {
        console.info("Please select both date and crime type to continue.")
        return
      }
      const response = await axios.get(`http://localhost:4000/predict?date=${date}&crimeType=${crimeType}`);
      const predictedAreas = response.data.prediction[0]
      const selectedValues = predictedAreas.map((code) => {
        return data.hasOwnProperty(code.toString()) ? data[code] : null;
      })
      setHighlightedAreas(selectedValues)
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  const handleDropDownChange = (e) => {
    setCrimeType(e.target.value);
  };

  return (
    <div>
      <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
      <ProductDropdown products={dropDownData} onChange={handleDropDownChange} />
      <button onClick={handleSubmit}>Go</button>
      <MapComponent highlightedAreas={highlightedAreas} />
    </div>
  );
};



export default App;
