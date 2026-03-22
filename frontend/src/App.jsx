import { useEffect } from 'react'
import { Navigate, Route, Routes, useLocation } from 'react-router-dom';
import ManageEntitiesPage from '../pages/ManageEntitiesPage';
import HomePage from '../pages/HomePage';

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
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/manage-entities" element={<ManageEntitiesPage />} />
    </Routes>
  );
}

export default App;