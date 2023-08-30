import matplotlib.pyplot as plt

def create_line_graph(x_data, y_data):
    plt.plot(x_data, y_data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph')
    plt.show()
