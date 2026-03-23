import { useEffect } from 'react'
import { Navigate, Route, Routes, useLocation } from 'react-router-dom';
import ManageEntitiesPage from '../pages/ManageEntitiesPage';
import HomePage from '../pages/HomePage';
import SimulatePage from '../pages/SimulatePage';
import SimulateGamePage from '../pages/SimulateGamePage';
import SimulatePlayerSeasonPage from '../pages/SimulatePlayerSeasonPage';
import {Toaster} from 'sonner';

const routeBodyClassMap = {
  '/': 'home',
  '/manage-entities': 'manage-entities',
};

function App(props) {
  const location = useLocation();

  useEffect(() => {
    const allClasses = Object.values(routeBodyClassMap);
    document.body.classList.remove(...allClasses);

    const bodyClass = routeBodyClassMap[location.pathname];
    if (bodyClass) {
      document.body.classList.add(bodyClass);
    }
  }, [location.pathname]);

  return (
    <>
      <Toaster position="top-center" richColors="true" toastOptions={{style: {scale: 1.3}}}/>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/simulate" element={<SimulatePage />} />
        <Route path="/simulate/game" element={<SimulateGamePage />} />
        <Route path="/simulate/season" element={<SimulatePlayerSeasonPage />} />
        <Route path="/manage-entities" element={<ManageEntitiesPage />} />
      </Routes>
    </>
  );
}

export default App;