Dijkstra Shortest Path Visualizer

Description
In this project, Dijkstra’s algorithm is implemented to find the shortest path between two vertices in a graph. The program reads from a dataset file, calculates the optimum route, creates an output report file and visualizes the graph.

Features
- Shortest Path calculation using Dijkstra's algorithm
- Input from CSV/Excel file
- Output report generation (output.txt)
- Graph visualization with emphasis on the shortest path (graph.png)
- Calculation of running time

Project Structure
.
├── Dijkstra Project.py
├── Dataset.csv
├── output.txt       # Output
├── graph.png        # Output
└── README.md

Dependencies
To install dependencies:
pip install networkx matplotlib pandas

Dataset Requirements
The dataset should contain the following fields:

| From | To | Weight |
| ---- | -- | ------ |
| A    | B  | 5      |
| B    | C  | 3      |

- From: Source vertex
- To: Destination vertex
- Weight: Distance/Cost

Usage
python "Dijkstra Project.py"

Provide the following:
Enter start node: A
Enter end node: D

Process
1. Dataset read by pandas
2. Graph creation using adjacency list
3. Application of Dijkstra’s Algorithm
4. Calculation of the shortest path
5. Output of:
   - Report file
   - Graph Visualization

Outputs

Output file (output.txt)
- Shortest path
- Path length/distance
- List of vertices visited
- List of edges used

Output graph (graph.png)
- Visual graph illustration
- Highlighting of the shortest path in red color

Error Handling
- Error if provided nodes do not exist
- Proper handling if no dataset file provided
- Validation of correct dataset structure

Possible Enhancements (Optional)
- GUI for better interaction (Tkinter or PyQt library)
- Functionality for directed graph analysis
- Interactivity in graph visualization
- Arguments in command line instead of input()

Author
Sharvesh

License
This project is meant for educational use only.
