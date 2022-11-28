import { useEffect, useState } from "react";
import axios from "axios";
import { Button, Table, Label, Header, Icon} from "semantic-ui-react";

const PlaylistPage = () => {
    const allPlaylists = 'http://127.0.0.1:8000/api/playlists/';
    
    const [playlist, setPlaylist] = useState({
        playlist: [],
    });

    const accessToken = JSON.parse(localStorage.getItem('authTokens'));
    console.log(accessToken);

    useEffect(() => {
        axios.get(allPlaylists,
            { headers:{'Authorization': `Bearer ${accessToken}`}})
            .then((response) => {
            console.log(response.data);
            setPlaylist({ playlist: response.data });
        });
    }, [accessToken]);

    let deletePlaylist = (playlistID) => {
        const url = 'http://127.0.0.1:8000/api/playlists/' + playlistID +'/';
        axios.delete(url, { headers:{'Authorization': `Bearer ${accessToken}`}}).then((response) => {
            console.log(response);
            console.log(response.data);
            if (response.status === 204) {
                window.location.reload(false);
            }
            else {
                alert("Something ain't right!")
            }
        });
        
    }

    if (!playlist) return null;

    return (
        <>
            <Button fluid color="violet" href = '/playlists/create' icon labelPosition="left">
                <Icon name="plus" />  
                   Create Playlist
            </Button> 
            <Table>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Playlists</Table.HeaderCell>
                        <Table.HeaderCell>Name</Table.HeaderCell>
                        <Table.HeaderCell># of Songs</Table.HeaderCell>
                        <Table.HeaderCell collapsing>View</Table.HeaderCell>
                        <Table.HeaderCell collapsing></Table.HeaderCell>
                    </Table.Row>
                </Table.Header>
                <Table.Body>
                    {playlist.playlist.map((playlist) => (
                        <Table.Row key={playlist.id}>
                            <Table.Cell >
                                <Label circular size="big" icon='music'>
                                </Label>
                            </Table.Cell>
                            <Table.Cell selectable> 
                                <Header href = {`/playlists/${playlist.id}`}>
                                    { playlist.name.charAt(0).toUpperCase() + playlist.name.slice(1)}
                                </Header>
                            </Table.Cell>
                            <Table.Cell> 
                                {playlist.songs.length} songs 
                            </Table.Cell>
                            <Table.Cell> 
                                <Button color="violet" href = {`/playlists/${playlist.id}`}>View</Button>
                            </Table.Cell>
                            <Table.Cell> 
                                <Button color="red" onClick={() => deletePlaylist(playlist.id)} icon='trash'>
                                </Button>
                            </Table.Cell>
                        </Table.Row>

                    ))}
                </Table.Body>
            </Table>
        </>
        

        
    )
}

export default PlaylistPage;