import React from 'react';
import { useNavigate } from "react-router-dom";
const HomeBanner = () => {
  const navigate = useNavigate();
  const getStartedHandler = () => {
    if (localStorage.getItem('token-info')) {
      navigate('/dashboard')
    } else {
      navigate('/login');
    }

  }
  return (
    <div className="home-banner">
      <div className="our-story">
        <h1 className="our-story-card-title" data-uia="hero-title">Unlimited movies, TV shows and more.</h1>
        <h2 className="our-story-card-subtitle" data-uia="our-story-card-subtitle">Watch anywhere. Cancel anytime.</h2>
        <p className="email-form-title">Ready to watch? Sign up or Login to Explore the universe of Movies.</p>
        <div className="input-group">

          <button className="input-group-button" onClick={getStartedHandler}>Get Started</button>
        </div>
      </div>
      <div className="shadow"></div>
      <img className="concord-img vlv-creative" src="https://assets.nflxext.com/ffe/siteui/vlv3/6e32b96a-d4be-4e44-a19b-1bd2d2279b51/ee068656-14b9-4821-89b4-53b4937d9f1c/IN-en-20220516-popsignuptwoweeks-perspective_alpha_website_small.jpg" alt=""></img>
    </div>
  )
}

export default HomeBanner;