import matplotlib.pyplot as plt

def create_pie_chart(x_data, y_data, labels):
    plt.pie(y_data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart')
    plt.show()
