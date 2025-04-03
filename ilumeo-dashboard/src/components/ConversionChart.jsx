import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  LineChart, Line, XAxis, YAxis, Tooltip, Legend,
  CartesianGrid, ResponsiveContainer
} from 'recharts';

const canaisDisponiveis = ['email', 'MOBILE', 'push', 'wpp'];

const ConversionChart = () => {
  const [data, setData] = useState([]);
  const [canal, setCanal] = useState('');
  const [dataInicio, setDataInicio] = useState('');
  const [dataFim, setDataFim] = useState('');

  const fetchData = async () => {
    let url = 'http://localhost:8000/conversao/';
    const params = [];

    if (canal) params.push(`canal=${canal}`);
    if (dataInicio) params.push(`data_inicio=${dataInicio}`);
    if (dataFim) params.push(`data_fim=${dataFim}`);

    if (params.length > 0) {
      url += '?' + params.join('&');
    }

    const res = await axios.get(url);

    const grouped = {};
    res.data.forEach(entry => {
      const { data, canal, taxa_conversao } = entry;
      if (!grouped[data]) grouped[data] = { data };
      grouped[data][canal] = taxa_conversao;
    });

    setData(Object.values(grouped));
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <div style={{ marginBottom: '1rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
        <label>
          Canal:
          <select value={canal} onChange={e => setCanal(e.target.value)}>
            <option value="">Todos</option>
            {canaisDisponiveis.map(c => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </label>

        <label>
          Data Início:
          <input type="date" value={dataInicio} onChange={e => setDataInicio(e.target.value)} />
        </label>

        <label>
          Data Fim:
          <input type="date" value={dataFim} onChange={e => setDataFim(e.target.value)} />
        </label>

        <button onClick={fetchData}>Filtrar</button>
      </div>

      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data}>
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="data" />
          <YAxis domain={[0, 1]} tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
          <Tooltip formatter={(v) => `${(v * 100).toFixed(2)}%`} />
          <Legend />
          {canaisDisponiveis.map((c, i) => (
            <Line key={c} type="monotone" dataKey={c} strokeWidth={2} stroke={
              ['#8884d8', '#82ca9d', '#ff7300', '#00c49f'][i]
            } />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ConversionChart;
