import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider } from 'react-router-dom';
import './App.css'
import './forTailwind.css';
import RootLayout from './rootLayout'
import AdminDashboard from './component/Admin/adminDashboard';
import HomePage from './component/Admin/home';
import Attendance from './component/Admin/attendance';


function App() {
  
  const router=createBrowserRouter(
    createRoutesFromElements(
      <Route path='/' element={<RootLayout/>}>
        <Route path='admin/dashboard' element={<AdminDashboard/>}>
          <Route index element={<HomePage/>}/>
          <Route path='attendance' element={<Attendance/>}/>
        </Route>
      </Route>
    )
  )
  return (
    
      <RouterProvider router={router} />
   
  )
}

export default App
