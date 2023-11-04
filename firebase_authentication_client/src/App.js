import React, { Component } from 'react';
import Navbar from './components/navbar/Navbar.js';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
          <Navbar/>
        <h1>client app</h1>
      </div>
    );
  }
}

export default App;
