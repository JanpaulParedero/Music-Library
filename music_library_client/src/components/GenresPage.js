import React from "react";
import { useState, useEffect} from "react";
import axios from "axios";
import { Table, Header, Image, Label, Dropdown} from "semantic-ui-react";
import { useParams } from "react-router-dom";
import AuthContext from "../utils/AuthContext";
import { useContext } from "react";


import AddToPlaylist from "./AddToPlaylist";


const GenresPage = () => {
    const { genre_id } = useParams();
    const Genre = "http://127.0.0.1:8000/api/genres/" + genre_id;
    const allGenres = "http://127.0.0.1:8000/api/genres/"

    let {user} = useContext(AuthContext);

    const [genreDetailList, setGenreDetailList] = useState({
        genre:[],
        songs:[],
    });

    const [genreList, setGenreList] = useState({
        genreList:[],
    });

    useEffect(() => {
        axios.get(Genre).then((response) => {
            console.log(response.data);
            setGenreDetailList({genre: response.data,
                                songs: response.data.songs.map(song => song)
            });
        });
    }, [Genre]);

    useEffect(() => {
        axios.get(allGenres).then((response) => {
            //console.log(response.data);
            setGenreList({genreList: response.data});
        });
    }, []);

    return(
    <>
        <Dropdown
        text= {genreDetailList.genre.genre_type}
        floating
        labeled
        button
        icon='filter'
        className='icon'>
           
            <Dropdown.Menu>
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
                        <Table.HeaderCell collapsing></Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {genreDetailList.songs.map((song) => (
                        <Table.Row key = { song.songURI }>
                            <Table.Cell>
                                <Header as='h4' image>
                                    <Image src={song.album.cover_art} rounded size='medium' />
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
export default GenresPage;