import { createContext, useState} from "react";
import axios from "axios";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext()

export default AuthContext;

export const AuthProvider = ({children}) => {
    
    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let navigate = useNavigate();
    

    let loginUser = async ( e )=> { 
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/token/', 
                {username: e.target.username.value , password : e.target.password.value});
            console.log(response.data)
            console.log (response.data.access)
            if(response.status === 200){
                setAuthTokens(response.data)
                setUser(jwt_decode(response.data.access))
                localStorage.setItem('authTokens', JSON.stringify(response.data.access))
                
                navigate("/");
            }
            else{
                alert("Something ain't right!")
            }
        }
        catch (err) {
         console.log(err);
        }
    }


    let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        navigate("/");
    }

    let contextData = {
        user:user,
        loginUser:loginUser,
        logoutUser:logoutUser,
    }
    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}

