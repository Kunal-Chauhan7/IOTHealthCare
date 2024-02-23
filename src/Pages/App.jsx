import React from 'react'
import { Routes, Route } from 'react-router-dom';
import LoginPage from '../Pages/LoginPage';
import MainPage from './MainPage';
const App = () => {
  return (
    <>
        <Routes>
            <Route path="/" element={<LoginPage/>}/>
            <Route path='/dashboard' element={<MainPage/>}/>
        </Routes>
    </>
  )
}

export default App