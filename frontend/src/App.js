import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import Nav from './Components/Nav/Nav';
import { authenticate } from './Store/session';

function App() {
  // Setup for user
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch()

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  return (
    <BrowserRouter>
      <Nav />
    </BrowserRouter>
  );
}

export default App;
