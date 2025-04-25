 
# 🧭 Persistent Pathfinder Visualizer

This project is a Python-based visual tool for exploring Dijkstra’s algorithm on a 2D grid. I created it as a way to better understand pathfinding algorithms in real-time, and to incorporate ideas like versioning and UI interaction using `pygame`.

You can place start/end points, draw obstacles, and visualize the shortest path; with support for undo/redo actions at every stage. It’s an interactive way to see how graph traversal algorithms work under the hood.

---

## 🚀 Key Features

- Interactive grid builder with mouse clicks
- Real-time pathfinding using **Dijkstra's algorithm**
- Fully functional **undo/redo** mechanism for all user actions
- Clear visual feedback with color-coded tiles
- Simple UI using `pygame` —> no external frameworks needed

---

## 🧠 Why I Built This

As part of a graduate-level course on advanced data structures, I wanted to implement a practical system that blends classical algorithmic concepts (like Dijkstra's) with ideas like **persistence** (i.e., state-saving). This app is the result: a small sandbox where algorithm logic meets user interaction.

---

## 🖥️ How to Run It

### 1. Install Python and `pygame`

Make sure Python 3.7+ is installed, then install pygame:

```bash
pip install pygame
```

### 2. Run the app

```bash
python main.py
```

---

## 🎮 Controls & Shortcuts

Action | What to Do
Place Start Point | Left-click (1st click)
Place End Point | Left-click (2nd click)
Draw Obstacles | Left-click + drag
Run Pathfinding | Press Enter
Undo Last Action | Press Z
Redo | Press Y
Restart App | Press Backspace

---

## 🎨 What the Colors Mean

| Color      | Meaning            |
|------------|--------------------|
|🟩Green      | Start point        |
|🟦 Blue       | Destination point  |
|⬜ Gray       | Walkable cell      |
|⬛Black      | Wall or obstacle   |
|🟥Red        | Final shortest path|
|🟦 Cyan       | Visited node       |


---

## 🧠 Algorithm Used

The core of the application is built around **Dijkstra’s algorithm**, a classical shortest path algorithm that guarantees an optimal path in graphs with non-negative weights.

Each cell in the grid is treated as a node. If the cell is not an obstacle, it's connected to its neighbors (up/down/left/right) with uniform weight = 1. The algorithm uses a custom **priority queue (min-heap)** to always expand the cheapest unexplored node.

On top of that, the app supports **persistent undo/redo** by saving a full snapshot of the grid after every meaningful change (start, destination, obstacle, or path). This is implemented in the `VersionManager.py` class.

---

## Project Structure

```text
.
├── main.py             # Main loop and pygame interface
├── maze.py             # Dijkstra's implementation + graph logic
├── priorityqueue.py    # Custom min-heap priority queue
├── VersionManager.py   # Undo/redo system with version snapshots
├── README.md           # You're reading it!
├── .gitignore          # Files to ignore when pushing to GitHub
└── requirements.txt    # (Optional) pygame dependency
```

---

 ## 💬 Final Thoughts

 I built this tool to help myself (and others) better understand pathfinding and persistence. It could definitely be extended; for example, to support A* search, weighted cells, or even real-time multiplayer editing. But as it stands, I’m proud of it as a functional and educational demo app.
