import './App.css';
import React from "react";
import Navbar from './components/Navbar';
import AlbumLists from './components/AlbumLists';
import { Container } from "semantic-ui-react"
import styled from 'styled-components';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AlbumPage from './components/AlbumPage';
import Register from './components/Register';
import Login from './components/Login';
import { AuthProvider } from './utils/AuthContext';
//import PrivateRoute from './utils/PrivateRoute';


const AppContainer = styled(Container)`
  margin: 15px; 
`
const App = () => {

  return (
    <Router>
      <AuthProvider>
        <AppContainer>
          <Navbar />
            <Routes>
              <Route path="/" element={<AlbumLists/>} />
              <Route path="/:albumURI" element={<AlbumPage/>} />
              <Route path="/register" element={<Register/>}/>
              <Route path="/login" element={<Login/>}/>
            </Routes>
        </AppContainer>
      </AuthProvider>
    </Router>
  );
}
export default App;
