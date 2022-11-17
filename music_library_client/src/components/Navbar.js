import React, { useContext } from 'react'
import { Menu, Button, Icon } from 'semantic-ui-react'
import AuthContext from '../utils/AuthContext'


const Navbar = () => {
  
  let {user, logoutUser} = useContext(AuthContext)
  console.log(user)
    return (
      <Menu borderless inverted>
        <Menu.Item>
          <Icon.Group size='large'>
            <Icon loading size='big' name='certificate' />
            <Icon name='headphones' color='violet'/>
          </Icon.Group>
        </Menu.Item>
        {user ? (
        <>
          <Menu.Item name='Home' href='/' content='Home'/>
          <Menu.Item name='Playlists'  content='Playlists'/>
        </>
        ):(
        <>
          <Menu.Item name='Home' href='/' content='Home'/>
        </>
        )}
         
        <Menu.Menu position='right'>
          {user ? (
            <>
              <Menu.Item>
                  <p>Welcome, {user.username}</p>
              </Menu.Item>
              <Menu.Item>
                <Button href= "/" color='violet'  content='Logout' onClick={logoutUser}/>
              </Menu.Item>
            </>
          ): (
            <>
              <Menu.Item>
                <Button href= "/register" color='violet' icon='signup' content='Register'/>
              </Menu.Item>
              <Menu.Item>
                <Button href= "/login" color='violet' icon='sign-in' content='Login'/>
              </Menu.Item>
            </>
          )}
        </Menu.Menu>
      </Menu>
    )
  }

export default Navbar;