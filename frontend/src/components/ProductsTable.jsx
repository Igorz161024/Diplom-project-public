import React, { useEffect, useState } from 'react';
import { getProductsData } from '../api/products';

const ProductsTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getProductsData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Products</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.productName}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default ProductsTable;
