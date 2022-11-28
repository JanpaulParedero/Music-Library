import React from "react";
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import { Table, Header, Image, Label, Button, Icon} from "semantic-ui-react";


const PlaylistSongs = () => {

    const {playlist_id} = useParams();

    const [playlist, setPlaylist] = useState({
        playlist:[],
        songs:[],
    });

    const accessToken = JSON.parse(localStorage.getItem('authTokens'));
    console.log(accessToken);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/playlists/" + playlist_id +'/', 
        { headers:{'Authorization': `Bearer ${accessToken}`}})
        .then((response) => {
            console.log(response.data);
            setPlaylist({playlist: response.data,
                         songs: response.data.songs.map(song => song),
            });
        });
    }, [accessToken, playlist_id]);

    let DeleteFromPlaylist = ( playlistID, songID) => {
        const url = 'http://127.0.0.1:8000/api/playlists/' + playlistID +'/simple/';
        console.log(url);
        axios.get(url, { headers:{'Authorization': `Bearer ${accessToken}`}})
        .then((response) => {
        console.log(response.data);
        const playlist = response.data;
        const song = songID
        const index = playlist.songs.indexOf(song);
        if (index > -1) {
            playlist.songs.splice(index, 1);
        }
            console.log(playlist);
            axios.patch(url, playlist, { headers:{'Authorization': `Bearer ${accessToken}`}})
            .then((response) => {
                console.log(response.data);
                window.location.reload(false);
            }
            )
        });
    }

    if (!playlist) return null;

    return(
    <>
        <Button fluid color="violet" href = '/playlists/' icon labelPosition="left">
                <Icon name="arrow left" />  
                   {playlist.playlist.name}
        </Button> 


        <Table singleLine color='violet'>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Title</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Explicit</Table.HeaderCell>
                        <Table.HeaderCell>Duration</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Preview</Table.HeaderCell>
                        <Table.HeaderCell collapsing></Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {playlist.songs.map((song) => (
                        <Table.Row key = { song.songURI }>
                            <Table.Cell>
                                <Header as='h4' image>
                                    <Image src={song.album.cover_art} rounded size='small' />
                                    <Header.Content>
                                    {song.name}
                                    <Header.Subheader>
                                    {song.artists.map((artist, index) => (
                                        <span key = {artist.artistURI} >
                                            {(index ? ', ': '') + artist.name } 
                                        </span>
                                    ))}
                                    </Header.Subheader>
                                    </Header.Content>
                                </Header>
                            </Table.Cell>
                            {song.explicit === true &&
                                <Table.Cell><Label>E</Label></Table.Cell>
                            }
                            {song.explicit === false &&
                                <Table.Cell></Table.Cell>
                            }
                            <Table.Cell>
                                {0|(song.duration_ms/1000/60)}:{('0'
                                +(0|(song.duration_ms/1000)%60)).slice(-2)}
                            </Table.Cell>
                            <Table.Cell>
                                <audio controls="controls" src= {`${song.song_preview}`} style= {{width: '200px'}}></audio> 
                            </Table.Cell>
                            <Table.Cell>
                                <Button color="red" onClick={() => DeleteFromPlaylist(playlist.playlist.id, song.songURI)} icon='trash'/>
                            </Table.Cell>
                        </Table.Row>
                    ))}
                </Table.Body>
            </Table>
        </>
    )
}
export default PlaylistSongs;

