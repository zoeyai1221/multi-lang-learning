# PyPacGame

A Python-based implementation of the classic Pac-Man game using Processing.py, featuring object-oriented design and interactive gameplay mechanics.

## Overview
PyPacGame recreates the essential elements of Pac-Man, demonstrating key concepts in game development including character animation, collision detection, and basic AI pathfinding. Built with Processing.py, the project showcases Python's capabilities in creating interactive visual applications.

## Features
- Animated Pac-Man character with directional movement
- Ghost AI (Pinky) with player-tracking behavior
- Dot collection system
- Maze navigation
- Edge-wrapping gameplay mechanics
- Object-oriented architecture

## Components
- `pacman.py`: Pac-Man character implementation
- `pinky.py`: Ghost AI and behavior
- `maze.py`: Maze structure and collision detection
- `dots.py`: Dot system management
- `game_character.py`: Base class for game entities

## Technical Highlights
- Processing.py graphics and animation
- Keyboard input handling
- Arc-based character rendering
- Collision detection system
- Basic AI pathfinding
- Object inheritance structure

## Controls
- Up Arrow: Move upward
- Down Arrow: Move downward
- Left Arrow: Move left
- Right Arrow: Move right

## Installation
1. Install Processing.py
2. Clone the repository
3. Run the sketch from Processing IDE

## Testing
Run tests using pytest:
```bash
pytest
```

## Project Structure
```
pypacgame/
├── pacman.py
├── pinky.py
├── maze.py
├── dots.py
├── game_character.py
└── tests/
    └── test_*.py
```

## Implementation Details
- Character animation using Processing's arc() function
- Frame-based animation system
- Coordinate-based movement system
- Intersection-based ghost AI
- Grid-based dot collection

## Skills Demonstrated
- Interactive graphics programming
- Game development fundamentals
- Object-oriented design
- Test-driven development
- Animation systems