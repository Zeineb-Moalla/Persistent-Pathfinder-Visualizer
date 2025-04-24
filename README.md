 
# 🧭 Persistent Pathfinder Visualizer

This project is a Python-based visual tool for exploring Dijkstra’s algorithm on a 2D grid. I created it as a way to better understand pathfinding algorithms in real-time, and to incorporate ideas like versioning and UI interaction using `pygame`.

You can place start/end points, draw obstacles, and visualize the shortest path — with support for undo/redo actions at every stage. It’s an interactive way to see how graph traversal algorithms work under the hood.

---

## 🚀 Key Features

- Interactive grid builder with mouse clicks
- Real-time pathfinding using **Dijkstra's algorithm**
- Fully functional **undo/redo** mechanism for all user actions
- Clear visual feedback with color-coded tiles
- Simple UI using `pygame` — no external frameworks needed

---

## 🧠 Why I Built This

As part of a graduate-level course on advanced data structures, I wanted to implement a practical system that blends classical algorithmic concepts (like Dijkstra's) with ideas like **persistence** (i.e., state-saving). This app is the result: a small sandbox where algorithm logic meets user interaction.

---

## 🎮 Controls & Shortcuts

Action	What to Do
Place Start Point	Left-click (1st click)
Place End Point	Left-click (2nd click)
Draw Obstacles	Left-click + drag
Run Pathfinding	Press Enter
Undo Last Action	Press Z
Redo	Press Y
Restart App	Press Backspace

---

## 🖥️ How to Run It

### 1. Install Python and `pygame`
Make sure Python 3.7+ is installed, then install pygame:

```bash
pip install pygame

