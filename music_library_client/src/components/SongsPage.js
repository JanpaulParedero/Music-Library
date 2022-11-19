import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { Table, Header, Image, Label, Dropdown} from "semantic-ui-react";


const allSongs = "http://127.0.0.1:8000/api/songs/"
const allGenres = "http://127.0.0.1:8000/api/genres/"

const SongsPage = () => {

    const [songList, setSongList] = useState({
        songs:[],
    });
    const [genreList, setGenreList] = useState({
        genreList:[],
    });

    useEffect(() => {
        axios.get(allSongs).then((response) => {
            console.log(response.data);
            setSongList({songs: response.data});
        });
    }, []);
    
    useEffect(() => {
        axios.get(allGenres).then((response) => {
            console.log(response.data);
            setGenreList({genreList: response.data});
        });
    }, []);

    if (!songList) return null;

    return(
    <>
        <Dropdown text='Choose A Genre'
            floating
            labeled
            button
            icon='filter'
            className='icon'
            color= 'violet'>
            <Dropdown.Menu>
            <Dropdown.Divider />
            <Dropdown.Header icon='tags' content='Genres' />
            <Dropdown.Menu scrolling>
                {genreList.genreList.map((genre) => (
                    <Dropdown.Item key={genre.id} href={`/songs/${genre.id}`}>
                        {genre.genre_type}
                    </Dropdown.Item>
                ))}
            </Dropdown.Menu>
            </Dropdown.Menu>
        </Dropdown>
        
        <Table singleLine color='violet'>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Title</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Explicit</Table.HeaderCell>
                        <Table.HeaderCell>Duration</Table.HeaderCell>
                        <Table.HeaderCell collapsing>Preview</Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {songList.songs.map((song) => (
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
                        </Table.Row>
                    ))}
                </Table.Body>
            </Table>
        </>
    )
}
export default SongsPage;