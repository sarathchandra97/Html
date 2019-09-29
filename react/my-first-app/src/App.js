import React, { Component } from 'react';
import './App.css';
import './components/simple';
import Simple from './components/simple';

class App extends Component {
  render() {
    return (
      <div className="container-fluid">
       <div className="jumbotron"><h1>Hello there</h1></div>
      </div>
      
    );
  }
}

export default App;
