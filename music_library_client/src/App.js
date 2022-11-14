import './App.css';
import React from "react";
import Navbar from './components/Navbar';
import AlbumLists from './components/AlbumLists';
import { Container } from "semantic-ui-react"
import styled from 'styled-components';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AlbumPage from './components/AlbumPage';

const AppContainer = styled(Container)`
  margin: 15px;
`
const App = () => {

  return (
    <Router>
      <AppContainer>
        <Navbar />
          <Routes>
            <Route path="/" element={<AlbumLists/>} />
            <Route path="/:albumURI" element={<AlbumPage/>} />
          </Routes>
      </AppContainer>
    </Router>
  );
}
export default App;
