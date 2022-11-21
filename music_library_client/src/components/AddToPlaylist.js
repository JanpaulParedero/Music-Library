import React from "react";
import axios from "axios";
import { useEffect, useState } from "react";
import { Dropdown } from "semantic-ui-react";
import jwtDecode from "jwt-decode";

const AddToPlaylist = ({songID}) => {

    const allPlaylists = 'http://127.0.0.1:8000/api/playlists/';

    const [playlist, setPlaylist] = useState({
        playlist: [],
    });

    const accessToken = JSON.parse(localStorage.getItem('authTokens'));
    console.log(accessToken);
    const user = jwtDecode(accessToken)
    console.log(user.user_id);

    useEffect(() => {
        axios.get(allPlaylists,
            { headers:{'Authorization': `Bearer ${accessToken}`}})
            .then((response) => {
            console.log(response.data);
            setPlaylist({ playlist: response.data });
        });
    }, [accessToken]);

    let addSongToPlaylist = ( playlistID, songID) => {
        const url = 'http://127.0.0.1:8000/api/playlists/' + playlistID +'/';
        console.log(url);
        axios.get(url, { headers:{'Authorization': `Bearer ${accessToken}`}})
        .then((response) => {
        console.log(response.data);
        const playlist = response.data;
        const song = songID
        const res = {
            ...playlist,
                songs: [...playlist.songs, song]
            }
            console.log(res);
            axios.patch(url, res, { headers:{'Authorization': `Bearer ${accessToken}`}})
            .then((response) => {
                console.log(response.data);
            }
            )
        });
    }
    
    return(
        <Dropdown
            icon = 'add'
            floating
            button
            className='icon'
        >
            <Dropdown.Menu>
            <Dropdown.Header  content='Playlists' />
            <Dropdown.Divider />
            {playlist.playlist.map((playlist) => (
                <Dropdown.Item key={playlist.id} onClick={() => addSongToPlaylist(playlist.id, songID, playlist.name)}>
                    {playlist.name}
                </Dropdown.Item>
            ))}
            </Dropdown.Menu>
        </Dropdown>                                       
    )
}

export default AddToPlaylist;