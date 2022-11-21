import React from "react";
import axios from "axios";
import { Button, Form , Input} from "semantic-ui-react";
import { useNavigate } from "react-router-dom";

const PlaylistCreate = () => {

    const allPlaylists = 'http://127.0.0.1:8000/api/playlists/';
    const accessToken = JSON.parse(localStorage.getItem('authTokens'));
    console.log(accessToken);
    let navigate = useNavigate();

    let handleSubmit = async(e) => {
        try{
            e.preventDefault();
            const response = await axios.post(allPlaylists, {name: e.target.name.value,},{headers:{'Authorization': `Bearer ${accessToken}`}})
            console.log(response.data);
            if(response.status === 201){
                navigate("/playlists");
            }
            else{
                alert("Something ain't right!")
            }
        }

        catch (err) {
            console.log(err);
        }
    }
    return (
        <Form onSubmit={handleSubmit}>
                <Form.Field 
                    className = "required"
                    label="name"
                    control={Input}
                    placeholder="name" 
                    name="name"
                    />
                <Button type='submit' content="Create"/>
        </Form>
    )
}

export default PlaylistCreate;