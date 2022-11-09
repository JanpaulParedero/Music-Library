import React, { Component } from 'react'
import { Menu } from 'semantic-ui-react'

export default class Navbar extends Component {
  state = {}

  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state

    return (
      <Menu>
        <Menu.Item
          name='Albums'
          active={activeItem === 'Albums'}
          onClick={this.handleItemClick}
        >
          Albums
        </Menu.Item>

        <Menu.Item
          name='Songs'
          active={activeItem === 'Songs'}
          onClick={this.handleItemClick}
        >
          Songs
        </Menu.Item>

        <Menu.Item
          name='Playlists'
          active={activeItem === 'Playlists'}
          onClick={this.handleItemClick}
        >
          Playlists
        </Menu.Item>
      </Menu>
    )
  }
}