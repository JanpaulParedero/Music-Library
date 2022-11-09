import './App.css';
import React from "react";
import Navbar from './components/Navbar';
import AlbumLists from './components/AlbumLists';
import { Container } from "semantic-ui-react"
import styled from 'styled-components';

const AppContainer = styled(Container)`
  margin: 15px;
`
const App = () => {

  return (
    <AppContainer>
      <Navbar />
      <AlbumLists />
    </AppContainer>
   
  );
}
export default App;
