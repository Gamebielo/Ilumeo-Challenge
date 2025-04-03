import React from 'react';
import ConversionChart from './components/ConversionChart';

function App() {
  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1 style={{ marginBottom: '2rem' }}>📈 Evolução da Taxa de Conversão</h1>
      <ConversionChart />
    </div>
  );
}

export default App;
