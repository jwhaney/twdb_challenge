import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom'
import EmailList from './Components/EmailList'
import DomainList from './Components/DomainList'
import Navbar from './Components/Navbar'

import './App.css';

function App() {

  return (
    <div className="App">
      
      <Router>
      <Navbar />
        <Switch>
          <Route exact path="/" component={EmailList} />
          <Route exact path="/domains" component={DomainList} />
        </Switch>  
      </Router>
      
    </div>
  );
}

export default App;
