# CSE312 - Coinflip Website
This website is designed to host virtual coinflip wagers between users, managed with virtual currency. We plan to incorporate statistics for each user, a leaderboard, rewards and more.

## Website:
https://flipduel.me/

## How To Run App:
- Navigate to the /virtualEnv/coinflip directory and run "docker-compose up"

## Objective 1 & 2 Note:
- Objective 1 is in our Play feature, where it says "Farm Money". Timing is set via cooldown to avoid spamming the farm + Active Farmers List showed to everyone (Inital 4 Second Bug due to a difference in the server-side and client-side timing)
- Objective 2 DoS Protection triggers after 50 refreshes, each page load only counts as 1 request.
## Objective 3:
For this objective we have added the ability to view the profiles of other users in the game list!
### Testing:
1. Navigate to the /virtualEnv/coinflip directory
2. Start your server using docker compose up
3. Navigate to http://localhost:8080/
4. Register an account following the criteria
5. Login into the account you just created
6. Click Play
7. Create new game of 10000 with head side
8. Verify that the name next to player is yours and clickable
9. Click on it
10. Verify you are redirected to Profile Page of your user
11. Change Url to a different username
12. Verify it says "User does not exist"
13. Click back to home
14. Click profile
15. Edit profile
16. Open up new browser and navigate to http://localhost:8080/
17. Repeat steps 4-6
18. View 1st browser's profile by checking out their profile
19. Verify it is the correct profile 

## Team Members:
- Christopher Pena
- Nethan Weerasinghe
- Garrett Davis
- Joshane Fernando
## Objective:
The first few weeks will be dedicated to research and planning. Many of the tools we will be using are new to us, so we will work to have a good understanding of them and implement them to a good standard. Our aim is to create a fun and engaging coinflip platform, fostering a sense of community while we develop our skills with real-world technologies.
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
