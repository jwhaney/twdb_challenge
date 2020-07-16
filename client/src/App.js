import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import {fetchEmails} from './emails/fetchEmails';

function App() {

  const [loading, setLoading] = useState(true)
  const [emails, setEmails] = useState() 

  useEffect(() => {
    setEmails( fetchEmails() )
  }, [])

  return (
    <div className="App">
      {
        loading ? (<p>...loading</p>) : (emails) 
      }
    </div>
  );
}

export default App;
