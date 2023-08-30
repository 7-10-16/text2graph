from cli.argparser import parse_args
from cli.graph_gen import create_graph
from graphs.line import create_line_graph
from graphs.pie import create_pie_chart

def main():
    args = parse_args()

    if args.type == 'line':
        create_line_graph(args.x_data, args.y_data)
    elif args.type == 'pie':
        create_pie_chart(args.x_data, args.y_data, args.labels)
    else:
        print("Invalid graph type.")

if __name__ == "__main__":
    main()
