import 'bootstrap/dist/css/bootstrap.min.css';  
import {Nav, Navbar, Container, NavDropdown} from 'react-bootstrap';  
import React from 'react';

const MenuItem = ({item}) => {
    return (
        <Nav.Link href={item.url}>{item.name}</Nav.Link>   
    )
}

const Menu = () => {
    const menu = [
        {'url': '#home', 'name': 'Home'},
        {'url': '#projects', 'name': 'Projects'},
        {'url': '#users', 'name': 'Users'},
    ]

    return (
        <Navbar expand="md">  
        <Container>  
        <Navbar.Brand href="#home">Simple TODO</Navbar.Brand>  
        <Navbar.Toggle aria-controls="basic-navbar-nav" />  
        <Navbar.Collapse id="basic-navbar-nav">  
        <Nav className="me-auto">
            {menu.map((item) => <MenuItem item={item}/>)}     
        </Nav>  
      </Navbar.Collapse>  
    </Container>  
  </Navbar>  
  );  
}  

export default Menu