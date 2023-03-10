
import Home from './components/Homepage/Home'
import Dashboard from './components/Dashboard';
import { Route, Routes } from 'react-router-dom';
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/Dashboard" element={<Dashboard />} />

      </Routes>


    </>
  );
}

export default App;
