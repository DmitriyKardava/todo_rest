import './App.css';
import React from "react";
import axios from 'axios';
import UsersList from './components/User';
import Menu from './components/Menu';
import Footer from './components/Footer';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': []
    }
  }

componentDidMount(){
  axios.get('http://127.0.0.1:8000/api/users/').then (responce => {
    this.setState(
      {
        'users':responce.data
      }
    )
  }).catch(error => console.error(error))  
}

  render () {
    return (
      <div class="container">
        <Menu/>
        <UsersList users={this.state.users}/>
        <Footer/>
      </div>
    )
  }
}


export default App;
