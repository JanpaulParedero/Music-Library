import './App.css';
import React from "react";
import Navbar from './components/Home/Navbar';
import AlbumLists from './components/Home/AlbumLists';
import { Container } from "semantic-ui-react"
import styled from 'styled-components';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AlbumPage from './components/Home/AlbumPage';
import Register from './components/Home/Register';
import Login from './components/Home/Login';
import { AuthProvider } from './utils/AuthContext';
import SongsPage from './components/Songs/SongsPage';
import GenresPage from './components/Songs/GenresPage'; 
import PlaylistPage from './components/Playlist/PlaylistPage';
import PlaylistCreate from './components/Playlist/PlaylistCreate';
import PlaylistSongs from './components/Playlist/PlaylistSongs';


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
              <Route exact path="/" element={<AlbumLists/>} />
              <Route exact path="/:albumURI" element={<AlbumPage/>} />
              <Route exact path="/register" element={<Register/>}/>
              <Route exact path="/login" element={<Login/>}/>
              <Route exact path="/songs" element={<SongsPage/>}/> 
              <Route exact path="/songs/:genre_id" element={<GenresPage/>}/>
              <Route exact path="/playlists" element={<PlaylistPage/>}/> 
              <Route exact path="/playlists/create" element={<PlaylistCreate/>}/>
              <Route exact path="/playlists/:playlist_id" element={<PlaylistSongs/>}/>
            </Routes>
        </AppContainer>
      </AuthProvider>
    </Router>
  );
}
export default App;
