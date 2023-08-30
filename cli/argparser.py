import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Create simple graphs using a CLI')

    parser.add_argument('--type', choices=['line', 'pie'], required=True, help='Type of graph to create')
    parser.add_argument('--x_data', type=float, nargs='+', required=True, help='X-axis data')
    parser.add_argument('--y_data', type=float, nargs='+', required=True, help='Y-axis data')

    # Additional arguments for specific graph types
    parser.add_argument('--labels', nargs='+', help='Labels for pie chart segments')

    return parser.parse_args()
