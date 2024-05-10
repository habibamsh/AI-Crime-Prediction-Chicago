import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import datetime
from model import CrimeRiskNN


df = pd.read_csv('./cleaned_dataset.csv')
label_encoder = LabelEncoder()
df['crime_code'] = label_encoder.fit_transform(df['IUCR'])
df['District'] = label_encoder.fit_transform(df['District'])
df['Ward'] = label_encoder.fit_transform(df['Ward'])
df['FBI Code'] = label_encoder.fit_transform(df['FBI Code'])
df['Community Area'] = label_encoder.fit_transform(df['Community Area'])
scaler = StandardScaler()
df[['week_no']] = scaler.fit_transform(df[['week_no']])

df['Arrest'] = df['Arrest'].astype(int)
features = df[['week_no', 'crime_code', 'Arrest', 'District', 'Ward', 'FBI Code']]
target = df['Community Area']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=21)

input_size = features.shape[1]
unique_community_areas = df['Community Area'].nunique()

print(input_size, type(input_size))
print(unique_community_areas, type(unique_community_areas))
model = CrimeRiskNN(input_size, unique_community_areas)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# Training the model
num_epochs = 100
for epoch in range(num_epochs):
    # Convert features and targets to tensors
    inputs = torch.tensor(X_train.values, dtype=torch.float32)
    targets = torch.tensor(y_train.values, dtype=torch.float32)

    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets.view(-1,1))

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


torch.save(model.state_dict(), './crime-prediction-nn.pth')