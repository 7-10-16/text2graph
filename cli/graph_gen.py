from graphs.line import create_line_graph
from graphs.pie import create_pie_chart

def create_graph(x_data, y_data, graph_type, labels=None):
    if graph_type == 'line':
        create_line_graph(x_data, y_data)
    elif graph_type == 'pie':
        create_pie_chart(x_data, y_data, labels)
    else:
        print("Invalid graph type.")
