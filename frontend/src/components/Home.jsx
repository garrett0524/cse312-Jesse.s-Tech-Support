import React from 'react';
import './Home.css';
import { useNavigate } from 'react-router-dom';
import LargeCoin from '../assets/3dicons.png';
import smallCoin from '../assets/smallCoin.svg';

const Home = () => {

  const navigate = useNavigate(); 

  const navigateToPrecursor = () => {
    navigate('/precursor');  
  };

  return (
    <div className="home">
      <div className="gradient-lines">
        {Array.from({ length: 16 }).map((_, index) => (
          <div key={index} className="line"></div>
        ))}
      </div>
      <div className="home-header">
        <h1>COIN FLIP</h1>
        <div className='small-coin'>
          <img src={smallCoin} alt="small-coin" />
        </div>
      </div>
      <div className="home-content">
      <div className="play-button">
          <span className="play-text" onClick={navigateToPrecursor}>Play</span>
          <span className="how-to-play-text">How to Play</span>
        </div>
        <div className="coin-image">
          <img src={LargeCoin} alt="Coin" />
        </div>
        <div className="circle circle-small-orange"></div>
        <div className="circle circle-medium-orange"></div>
        <div className="circle circle-small-yellow"></div>
        <div className="circle circle-medium-yellow"></div>
        <div className="circle circle-small-green"></div>
        <div className="circle circle-medium-green"></div>
        <div className="circle circle-large-blue"></div>
        <div className="circle circle-medium-red"></div>
        <div className="circle circle-small-purple"></div>
        <div className="circle circle-extra-large-green"></div>
        <div className="circle circle-large-yellow"></div>
        <div className="circle circle-extra-large-orange"></div>
        <div className="circle circle-small-red"></div>
        <div className="circle circle-medium-blue"></div>
        <div className="circle circle-large-purple"></div>
        <div className="circle circle-medium-green-low"></div>
        <div className="circle circle-medium-orange-second"></div>
        <div className="circle circle-small-yellow-second"></div>
        <div className="circle circle-large-green-second"></div>
        <div className="circle circle-small-blue"></div>
        <div className="circle circle-large-red"></div>
      </div>
    </div>
  );
};

export default Home;
