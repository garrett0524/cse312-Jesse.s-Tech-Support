# CSE312 - Coinflip Website
This website is designed to host virtual coinflip wagers between users, managed with virtual currency. We plan to incorporate statistics for each user, a leaderboard, rewards and more.


## How To Run App:
- Navigate to the /virtualEnv/coinflip directory and run "docker-compose up"
- Please be patient while database is ready for web to connect (May take up to 30 seconds). Thank you in advance! 
## How To Access Database:
- Once you are at localhost:8080
- Navigate to localhost:8080/admin
- Credentials:
  user: admin
  password: password
- Navigate any of the tables
## Team Members:
- Christopher Pena
- Nethan Weerasinghe
- Garrett Davis
- Joshane Fernando
## Websockets:
The core functionality of the project takes place inside the "play" button which takes you to the core gameplay. Here we use websocket interactions between users to get the latest game created from another user. When created a user can click to play, and test their luck. 
## Figma:
https://www.figma.com/proto/mRjCJZBPmhgYFBwkociLj0/Coin-Flip-Game?node-id=1-2
## Tech Stack:
- Backend: Django/Python
- Database: MySQL
- Frontend: React
## Coinflip Features:
- Two-player matchups
- Wagers with equal amounts of virtual currency
- Heads or tails selection
- Global Chat
- Game creation (picking a side)
- Joining existing games (picking the opposite side)
## Stats Page:
- Win rate (percentage)
- Total wins/losses
- Virtual currency balance
## Leaderboard:
- List of users
- Sorted by virtual currency balance
