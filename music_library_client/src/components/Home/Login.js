import { useContext } from "react";
import { Form , Input} from "semantic-ui-react";
import AuthContext from '../../utils/AuthContext'

const Login = () => {
    let {loginUser} = useContext(AuthContext)
    return(
            <Form onSubmit={loginUser}>
                <Form.Field 
                    icon = "user"
                    className = "required"
                    label="Username"
                    control={Input}
                    placeholder="Username" 
                    name="username"
                    />
                <Form.Field 
                    icon = "lock"
                    className = "required"
                    label="Password"
                    type="password"
                    control={Input}
                    placeholder="Password" 
                    name="password"
                    />
                <Form.Button type='submit' content="Submit"/>
            </Form>
    )
}
export default Login;