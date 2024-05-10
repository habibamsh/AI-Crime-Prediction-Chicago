const express = require('express');
const cors = require('cors'); // Import the cors middleware

const app = express();

// Configure CORS to allow requests from your React app's domain
app.use(cors());

// Define your routes and route handlers here

const PORT = process.env.PORT || 5001;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

app.post('/predict', (req, res) => {
  // Handle the POST request and return a response
  // You may need to process the request body (req.body) and perform predictions
  // Example: const prediction = predictFunction(req.body);
  const predict = {"Response": "Helllo"}
  // Return the prediction as a response
  res.json({ predict });
});

app.post('/api/predict', (req, res) => {
  // Handle the POST request and return a response
  // You may need to process the request body (req.body) and perform predictions
  // Example: const prediction = predictFunction(req.body);
  const predict = {"Response": "byeee byee"}
  // Return the prediction as a response
  res.json({ predict });
});

