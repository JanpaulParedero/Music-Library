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
        <Card.Group centered itemsPerRow={5} >
            {albumList.albums.map((album) => (
                    <Card fluid color='violet' href={`/${album.albumURI}`} key = {album.albumURI}> 
                        <Image src= {album.cover_art} wrapped ui={false} />
                        <Card.Content>
                            <Card.Header>{album.name}</Card.Header>
                            <Card.Meta>
                            {album.artists.map((artist, index) => (
                                    <span key = {artist.artistURI} >
                                        {(index ? ', ': '') + artist.name } 
                                    </span>
                                ))}
                            </Card.Meta>
                        </Card.Content>
                    </Card>
                )
            )}
        </Card.Group>
    )
}
export default AlbumLists
