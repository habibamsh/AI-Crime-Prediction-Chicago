import React from 'react';

const ProductDropdown = ({ products, onChange }) => {
  return (
    <select onChange={onChange}>
      <option value="">Select a Crime Type</option>
      {products.map((product) => (
        <option key={product.crime_code} value={product.crime_code}>
          {product.description}
        </option>
      ))}
    </select>
  );
};

export default ProductDropdown;