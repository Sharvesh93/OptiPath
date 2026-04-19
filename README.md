# 🚀 Dijkstra Shortest Path Visualizer

## 📌 Overview

This project implements **Dijkstra's Algorithm** to find the shortest path between two nodes in a graph.
It reads data from a dataset file, computes the optimal path, generates a report, and visualizes the graph.

---

## ⚙️ Features

* ✅ Shortest path calculation using Dijkstra's algorithm
* 📊 Reads graph data from CSV / Excel
* 📝 Generates a detailed output report (`output.txt`)
* 📈 Visualizes graph with highlighted shortest path (`graph.png`)
* ⏱️ Measures computation time

---

## 📂 Project Structure

```
.
├── Dijkstra Project.py
├── Dataset.csv
├── output.txt        # Generated
├── graph.png         # Generated
└── README.md
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install networkx matplotlib pandas
```

---

## 📊 Dataset Format

Your dataset must contain the following columns:

| From | To | Weight |
| ---- | -- | ------ |
| A    | B  | 5      |
| B    | C  | 3      |

* `From` → Source node
* `To` → Destination node
* `Weight` → Distance / cost

---

## ▶️ How to Run

```bash
python "Dijkstra Project.py"
```

Then enter:

```
Enter start node: A
Enter end node: D
```

---

## 🧠 How It Works

1. Loads dataset using **pandas**
2. Builds graph using adjacency list
3. Applies **Dijkstra’s Algorithm**
4. Finds shortest path + distance
5. Generates:

   * 📄 Report file
   * 🖼️ Graph visualization

---

## 📤 Output

### 🔹 Report (output.txt)

* Shortest path
* Total distance
* Nodes covered
* Edges traversed

### 🔹 Graph (graph.png)

* Full graph visualization
* Shortest path highlighted in **red**

---

## ⚠️ Error Handling

* Invalid nodes → raises error
* Missing dataset → handled
* Incorrect columns → validation included

---

## 🛠️ Improvements (Optional)

* Add GUI (Tkinter / PyQt)
* Support directed graphs
* Interactive graph visualization
* CLI arguments instead of input()

---

## 👨‍💻 Author

Sharvesh

---

## 📜 License

This project is for educational purposes.
