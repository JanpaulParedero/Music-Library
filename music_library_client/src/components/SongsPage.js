import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { Table, Header, Image, Label } from "semantic-ui-react";

const allSongs = "http://127.0.0.1:8000/api/songs/"

const SongsPage = () => {
    const [songList, setSongList] = useState({
        songs:[],
    });

    useEffect(() => {
        axios.get(allSongs).then((response) => {
            console.log(response.data);
            setSongList({songs: response.data});
        });
    }, []);

    if (!songList) return null;

    return(
        <Table singleLine color='violet'>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell collapsing></Table.HeaderCell>
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
                                    <Image src={song.cover_art} rounded size='small' />
                                    <Header.Content>
                                    {song.name}
                                    <Header.Subheader>{song.artists}</Header.Subheader>
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
                                <audio controls="controls" src= {`${song.song_preview}`} style= {{width: '100px'}}></audio> 
                            </Table.Cell>
                        </Table.Row>
                    ))}
                </Table.Body>
            </Table>
    )
}
export default SongsPage;