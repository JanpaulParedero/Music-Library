import React from 'react'
import { Table } from 'semantic-ui-react'
import axios from 'axios'
import { useParams } from 'react-router-dom'




const AlbumPage = () => {

    const {albumURI} = useParams();
    const URL = "http://127.0.0.1:8000/api/albums/" + albumURI;
    console.log({albumURI});

    const [albumDetailList, setAlbumDetailList] = React.useState({
        album:[],
        songs:[],
    });

    React.useEffect(() => {
        axios.get(URL).then((response) => {
            console.log(response.data);
            setAlbumDetailList({album: response.data,
                                songs: response.data.songs.map(song => song),
            });
        });
    }, [URL]);

    if (!albumDetailList) return null;

    return (
    <Table singleLine>
        <Table.Header>
            <Table.Row>
                <Table.HeaderCell collapsing>Track</Table.HeaderCell>
                <Table.HeaderCell>Title</Table.HeaderCell>
                <Table.HeaderCell>Artists</Table.HeaderCell>
                <Table.HeaderCell>Duration</Table.HeaderCell>
            </Table.Row>
        </Table.Header>
    </Table>
    )
}
export default AlbumPage;