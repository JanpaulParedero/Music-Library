import React from 'react'
import { Card, Image } from 'semantic-ui-react'
import axios from 'axios'

const albumURL = "http://127.0.0.1:8000/api/albums/"

const AlbumLists = () => {
    const [albumList, setAlbumList] = React.useState({
        albums:[],
    });

    React.useEffect(() => {
        axios.get(albumURL).then((response) => {
            console.log(response.data);
            setAlbumList({albums: response.data});
        });
    }, []);

    if (!albumList) return null;

    return (
        <div key = {albumList.albums.albumURI}>
        <Card.Group itemsPerRow={5}>
            {albumList.albums.map((album) => (
                <Card href='#card-example-link-card'> 
                    <Image src= {album.cover_art} wrapped ui={false} />
                    <Card.Content>
                        <Card.Header>{album.name}</Card.Header>
                        <Card.Meta>
                             <span>{album.artist}</span>
                        </Card.Meta>
                    </Card.Content>
                </Card>
                )
            )}
        </Card.Group>
        </div>
    )
}
export default AlbumLists
