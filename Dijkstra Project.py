import heapq
import time
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def dijkstra(graph, start, end):
    try:
        queue = [(0, start, [])]
        visited = set()
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        while queue:
            (dist, node, path) = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]
            if node == end:
                return dist, path
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_dist = dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor, path))
        return float('inf'), []
    except KeyError as e:
        raise KeyError(f"Node error in Dijkstra: {e}")
    except Exception as e:
        raise Exception(f"Error in Dijkstra computation: {e}")

def generate_report(source, destination, distance, path):
    try:
        report = f"""
=========================================================
        RESOURCE ALLOCATION REPORT
=========================================================
Destination  : {destination}
---------------------------------------------------------
Shortest Path Found :
   {' → '.join(path) if path else 'No path available'}
   Total Distance: {distance:.2f} km 
=========================================================
Summary
=========================================================
Optimal Depot       : {source}
Total Nodes Covered : {len(path)}
Edges Traversed     : {len(path) - 1 if path else 0}
---------------------------------------------------------
"""
        with open('output.txt', 'w', encoding="utf-8") as f:
            f.write(report)
        return report
    except Exception as e:
        raise Exception(f"Error generating report: {e}")

def generate_graph_image(graph, path, filename='graph.png'):
    try:
        G = nx.Graph()
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)
        pos = nx.spring_layout(G, seed=45)  
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold', edge_color='gray', width=2)
        if path:
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)
        edge_labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12)
        plt.title("Graph with Shortest Path Highlighted", fontsize=16)
        plt.axis('off')
        plt.savefig(filename, format='png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Graph image saved as {filename}")
    except Exception as e:
        raise Exception(f"Error generating graph image: {e}") 

if __name__ == "__main__":
    try:
        file_path = "Dataset.csv"
        file_type = "csv"
        if file_type == 'csv':
            df = pd.read_csv(file_path)
        elif file_type == 'excel':
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Invalid file type. Choose 'csv' or 'excel'.")
        required_columns = ['From', 'To', 'Weight']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"File must contain columns: {required_columns}")
        graph = {}
        for _, row in df.iterrows():
            from_node = str(row['From']).upper() 
            to_node = str(row['To']).upper()
            weight = float(row['Weight'])
            if from_node not in graph:
                graph[from_node] = {}
            graph[from_node][to_node] = weight
            if to_node not in graph:
                graph[to_node] = {}
            graph[to_node][from_node] = weight
        start_node = input("Enter start node: ").upper()
        if start_node not in graph:
            raise ValueError(f"Invalid start node: {start_node}")
        end_node = input("Enter end node: ").upper()
        if end_node not in graph:
            raise ValueError(f"Invalid end node: {end_node}")
    except ValueError as ve:
        print(ve)
        exit(1)
    except FileNotFoundError:
        print("File not found. Please check the path.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        exit(1)
    start_time = time.time()
    distance, path = dijkstra(graph, start_node, end_node)
    end_time = time.time()
    computation_time = end_time - start_time
    report = generate_report(graph, start_node, end_node, distance, path, computation_time)
    print(report)
    generate_graph_image(graph, path)
