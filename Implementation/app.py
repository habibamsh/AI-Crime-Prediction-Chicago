from flask import Flask, request, jsonify
from flask_cors import CORS
from model import CrimeRiskNN
from sklearn.preprocessing import LabelEncoder, StandardScaler
import torch
import pandas as pd
from datetime import datetime

app = Flask(__name__)
CORS(app)

input_size = 6 # from model
output_size = 77 
model = CrimeRiskNN(input_size, output_size)

model.load_state_dict(torch.load('./crime-prediction-nn.pth'))
model.eval()
crime_label_encoder = LabelEncoder()
scaler = StandardScaler()

def predict_top_community_area(week_no, original_crime_code, k=4):
    # Convert original crime code to encoded value
    # encoded_crime_code = crime_label_encoder.transform([original_crime_code])[0]
    
    # Prepare and normalize input data
    input_data = pd.DataFrame([[week_no, original_crime_code, 1, 0, 0, 0]], 
                              columns=['week_no', 'crime_code', 'Arrest', 'District', 'Ward', 'FBI Code'])
    # input_data['week_no'] = scaler.transform(input_data[['week_no']])
    
    input_tensor = torch.tensor(input_data.values, dtype=torch.float32)

    prediction = model(input_tensor)
    ttop_k_values, top_k_indices = torch.topk(prediction, k)
    
    top_k_community_areas = top_k_indices.tolist()

    return top_k_community_areas

# Define your API endpoint for predictions

def get_week_number(date_str):
    try:
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        # Extract the week number using strftime
        week_number = int(date_obj.strftime('%U'))

        return week_number
    except ValueError:
        # Handle invalid date format
        return None
    
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Return the prediction as a JSON response
        date = request.args.get('date')
        crimeType = request.args.get('crimeType')
        return jsonify({'prediction': predict_top_community_area(week_no=get_week_number(date),original_crime_code=int(crimeType))})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=4000)
