# snake-pygame
A classic Snake game built from scratch in Python with pygame.

<img width="704" height="697" alt="Screenshot 2026-11-25 at 18 28 04" src="https://github.com/user-attachments/assets/38788b8a-4796-4fa7-bf52-8c33469e121a" />

This was my first complete programming project. I built it step by step to learn the fundamentals of game development: the game loop, keyboard input, collision detection and managing state.

**Features**
- The snake moves on a 30 × 30 grid and grows each time it eats
- Food appears at random positions, always aligned with the grid
- Game over when the snake hits a wall or its own body
- U-turns are blocked, so you can't accidentally run into yourself
- Live score display
- Restart instantly with SPACE after a game over

**How to run**
1. Make sure you have Python 3 installed.
2. Download or clone this repository:
   git clone https://github.com/YOUR-USERNAME/snake-pygame.git
   cd snake-pygame
3. Install the dependency:
   pip install -r requirements.txt
4. Start the game:
5. python snake.py
(On some systems, use python3 instead of python)

**Controls**
Key: ← ↑ → ↓	     Action: Change direction
Key: SPACE	       Action: Restart after game over
Key: Close window	 Action: Quit

**How it works**
• Game loop: the game runs in a while loop at 10 frames per second (clock.tick(10)). Each frame, it reads input, updates the snake, checks collisions and redraws the screen.
• Snake body: the snake is stored as a list of (x, y) positions. Each frame, a new head is added at the front and the tail is removed. When the snake eats, the tail is kept, so it grows by one square.
• Collisions: the head is checked against the window edges and against every other square of the body.

**Built with**
Python 3 & pygame on VS

**Possible improvements**
- Save the high score between games
- Increase speed as the score goes up
- Add a start menu
