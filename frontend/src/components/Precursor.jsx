import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Precursor.css';
import smallCoin from "../assets/smallCoin.svg"

function Precursor() {

  const navigate = useNavigate();

  const navigateToPlay = () => {
    navigate('/play'); 
  };

  return (
    <div className="container">
      
      <div className="sidebar">
        <div className="logo">
          
          <div className="logo-background"></div>
          <div className="logo-foreground"></div>
        </div>
        <div className="title">COIN FLIP</div>
        <div className="smallCoin">
          <img src={smallCoin} alt="small coin"/>
        </div>
        <div className="divider"></div>
        <div className="menu-item">Account</div>
        <div className="menu-item">Leaderboard</div>
        <div className="menu-item">Chat</div>
        <div className="menu-item logout">Log Out</div>
      </div>
      <div className="content">
        <div className="box">
          <div className="list-item">
            <div className="username">JoshaneTheDestroyer</div>
            <div className="choice">Heads</div>
            <div className="amount">$50,000</div>
          </div>
          <div className="list-item">
            <div className="username">JoshaneTheDestroyer</div>
            <div className="choice">Heads</div>
            <div className="amount">$50,000</div>
          </div>
          <div className="list-item">
            <div className="username">JoshaneTheDestroyer</div>
            <div className="choice">Heads</div>
            <div className="amount">$50,000</div>
          </div>
        </div>
        <div className="box">
          <div className="balance">Balance: $250,000</div>
          <div className="wins">Wins: 24</div>
          <div className="losses">Losses: 2</div>
          <button className="create-game" onClick={navigateToPlay}>Create Game</button>
        </div>
      </div>
    </div>
  );
}

export default Precursor;