from graphviz import Digraph

def create_decision_tree():
    dot = Digraph()
    
    # Nodos
    dot.node('A', 'Presupuesto < $20,000?')
    dot.node('B', 'No compra')
    dot.node('C', 'Presupuesto > $30,000?')
    dot.node('D', 'Compra')
    dot.node('E', 'Tipo de coche = SUV?')
    dot.node('F', 'Compra')
    dot.node('G', 'No compra')
    
    # Conexiones
    dot.edge('A', 'B', 'Sí')
    dot.edge('A', 'C', 'No')
    dot.edge('C', 'D', 'Sí')
    dot.edge('C', 'E', 'No')
    dot.edge('E', 'F', 'Sí')
    dot.edge('E', 'G', 'No')
    
    return dot

# Crear y mostrar el árbol
decision_tree = create_decision_tree()
decision_tree.view()
