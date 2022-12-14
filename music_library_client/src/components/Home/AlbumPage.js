import { Table, Grid, GridColumn, Header, Segment, Image, Label,} from 'semantic-ui-react'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import AddToPlaylist from '../Playlist/AddToPlaylist'
import AuthContext from '../../utils/AuthContext'
import React, {useContext} from 'react'

const AlbumPage = () => {

    const { albumURI } = useParams();
    const URL = "http://127.0.0.1:8000/api/albums/" + albumURI;
    let {user} = useContext(AuthContext);

    const [albumDetailList, setAlbumDetailList] = React.useState({
        album:[],
        songs:[],
        artists:[]
    });

    React.useEffect(() => {
        axios.get(URL).then((response) => {
            console.log(response.data);
            setAlbumDetailList({album: response.data,
                                songs: response.data.songs.map(song => song),
                                artists: response.data.artists.map(artist => artist),
            });
        });
    }, [URL]);
    
    if (!albumDetailList) return null;

    return (
    <>
        <Segment placeholder color='violet'>
            <Grid columns = {2} relaxed = 'very' stackable textAlign='center'>
            <Grid.Row verticalAlign='middle'>
                <Grid.Column> 
                    <Image src={albumDetailList.album.cover_art} size='medium' centered = {true} rounded/>
                </Grid.Column>
                <GridColumn>
                    <Header as = 'h1' centered = {true}> {albumDetailList.album.name} </Header>
                    <Header size = 'medium' centered = {true}>
                        {albumDetailList.artists.map((artist, index) => (
                            <span key = {artist.artistURI} >
                                {(index ? ', ': '') + artist.name }
                            </span>
                        ))}
                    </Header>
                    <Header size = 'small' centered = {true}> {albumDetailList.album.release_date} </Header>
                </GridColumn>
            </Grid.Row>
            </Grid>
        </Segment>
            <Table singleLine color='violet'>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell collapsing>Track</Table.HeaderCell>
                        <Table.HeaderCell>Title</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Explicit</Table.HeaderCell>
                        <Table.HeaderCell>Duration</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Preview</Table.HeaderCell>
                        <Table.HeaderCell collapsing></Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {albumDetailList.songs.map((song) => (
                        <Table.Row key = { song.songURI }>
                            <Table.Cell>
                                <Label circular color='violet'>
                                    { song.track_number }
                                </Label>
                            </Table.Cell>
                            <Table.Cell>
                            <Header as= 'h4'>
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
                            {user ? (
                                <AddToPlaylist songID={song.songURI}/>
                            ):(
                                <></>
                            )}
                                
                            </Table.Cell>
                        </Table.Row>
                    ))}
                </Table.Body>
            </Table>
    </>
    )
}
export default AlbumPage;