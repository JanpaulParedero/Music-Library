import { useState } from "react";
import axios from "axios";
import { Form , Input} from "semantic-ui-react";
import { useNavigate } from "react-router-dom";

const url = 'http://127.0.0.1:8000/api/register/';
const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [first_name, setFirstname] = useState('');
    const [last_name, setLastname] = useState('');
    let navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(url, {username , password, first_name, last_name });
            console.log(response.data);
            navigate("/login");
        }
        catch (err) {
            console.log(err);
        }
    };

    return(
            <Form onSubmit={handleSubmit}>
                <Form.Field 
                    icon = "user"
                    className = "required"
                    label="Username"
                    value={username}
                    control={Input}
                    onChange= {(e) => setUsername(e.target.value)} 
                    placeholder="Username" 
                    name="username"
                    />
                <Form.Field 
                    icon = "lock"
                    className = "required"
                    label="Password"
                    value={password}
                    control={Input}
                    onChange= {(e) => setPassword(e.target.value)} 
                    placeholder="Password" 
                    name="password"
                    />
                <Form.Field 
                    className = "required"
                    label="First Name"
                    value={first_name}
                    control={Input}
                    onChange= {(e) => setFirstname(e.target.value)} 
                    placeholder="First Name" 
                    name="firstname"
                    />
                <Form.Field 
                    className = "required"
                    label="Last Name"
                    value={last_name}
                    control={Input}
                    onChange= {(e) => setLastname(e.target.value)} 
                    placeholder="Last Name" 
                    name="lastname"
                    />
                <Form.Button type='submit' content="Submit"/>
            </Form>
    )
}
export default Register;