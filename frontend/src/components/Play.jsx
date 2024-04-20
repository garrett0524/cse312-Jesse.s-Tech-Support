import React from 'react';
import './Precursor.css';
import './Play.css';
import smallCoin from "../assets/smallCoin.svg"
import coinImage from "../assets/quarter.png"; 


function Play() {
    return (
        <div className="container">

            <div className="sidebar">
                <div className="logo">

                    <div className="logo-background"></div>
                    <div className="logo-foreground"></div>
                </div>
                <div className="title">COIN FLIP</div>
                <div className="smallCoin">
                    <img src={smallCoin} alt="small coin" />
                </div>
                <div className="divider"></div>
                <div className="menu-item">Account</div>
                <div className="menu-item">Leaderboard</div>
                <div className="menu-item">Chat</div>
                <div className="menu-item logout">Log Out</div>
            </div>
            <div className="content">
                <div className="coin-flip-interface">
                    <div className="amount-label">Amount:</div>
                    <div className="coin-container">
                        <button className="coin-button">H</button>
                        <img src={coinImage} alt="coin" className="quarter" />
                        <button className="coin-button">T</button>
                    </div>
                    <div className="amount-options">
                        <button className="amount-option">0.10</button>
                        <button className="amount-option">0.50</button>
                        <button className="amount-option">1.00</button>
                        <button className="amount-option">2.00</button>
                        <button className="amount-option">5.00</button>
                        <button className="amount-option">10.00</button>
                    </div>
                    <button className="flip-button">Flip</button>
                </div>
            </div>
        </div>
    );
}

export default Play;