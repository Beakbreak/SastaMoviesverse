import React, { useState, useEffect } from "react";
import "./App.scss";
import Header from "./components/Header";
import HomeBanner from "./components/HomeBanner";
import Login from "./components/Login";
import Banner from "./components/Banner";
import List from "./components/List";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  const [arr, setarr] = useState([0]);
  const arr1 = arr.slice(0, 7);
  const arr2 = arr.slice(7, 14);
  const arr3 = arr.slice(14, 21);
  const arr4 = arr.slice(21, 28);
  const arr5 = arr.slice(28, 35);
  const arr6 = arr.slice(35, 42);
  const getmovie = (x) => {
    setarr(x);
  };
  const logon = (x) => {
    setlogged(x);
  };
  const [logged, setlogged] = useState(false);
  useEffect(logon, []);
  return (
    <React.Fragment>
      <Router>
        <Routes>
          <Route
            path="/"
            element={
              <React.Fragment>
                <Header l={logged} />
                <HomeBanner />
              </React.Fragment>
            }
          />
          <Route
            path="/login"
            element={
              <React.Fragment>
                <Header l={logged} />
                <Login movie={getmovie} log={logon} />
              </React.Fragment>
            }
          />
          <Route
            path="/register"
            element={
              <React.Fragment>
                <Header l={logged} />
                <Login movie={getmovie} log={logon} />
              </React.Fragment>
            }
          />
          <Route
            path="/dashboard"
            element={
              <React.Fragment>
                <Header l={logged} />
                <Banner />
                <List
                  title="Recommended For you"
                  param="originals"
                  data={arr1}
                />
                <List title="Trending Now" param="trending" data={arr2} />
                <List title="Now Playing" param="now_playing" data={arr3} />
                <List title="popular" param="popular" data={arr4} />
                <List title="Top Rated" param="top_rated" data={arr5} />
                <List title="Upcoming" param="upcoming" data={arr6} />
              </React.Fragment>
            }
          />
        </Routes>
      </Router>
    </React.Fragment>
  );
}

export default App;
