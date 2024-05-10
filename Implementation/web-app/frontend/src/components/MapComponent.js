import React from 'react';
import { MapContainer, TileLayer, Polygon } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const MapComponent = ({ highlightedAreas }) => {
  const centerOfChicago = [41.8781, -87.6298]; // Latitude and Longitude of Chicago

  return (
    <MapContainer center={centerOfChicago} zoom={11} style={{ height: '500px', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {highlightedAreas.map(area => (
        <Polygon positions={area} color="blue" />
      ))}
    </MapContainer>
  );
};

export default MapComponent;
