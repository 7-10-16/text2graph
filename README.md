# Text-2-Graph

A command-line tool for creating simple graphs using Python.

## Features

- Create line graphs and pie charts.
- Easily specify X-axis and Y-axis data.
- Customize pie chart segments with labels.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/7-10-16/text2graph.git
   ```

2. Navigate into the new directory:
   ```bash
   cd text2graph
   ```

3. Make sure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

## Usage:
### 📈 Line Graph:
  ```bash
  python main.py --type line --x_data 1 2 3 4 --y_data 10 20 30 40
```
### 🥧 Pie Chart:
```bash
python main.py --type pie --x_data 1 2 3 --y_data 30 40 50 --labels Label1 Label2 Label3
```

## Contributing

Contributions are welcome! Please follow these steps:

1. 🍴 Fork the repository.
2. 🌲 Create a new branch: `git checkout -b feature/your-feature-name`.
3. 💒 Commit your changes: `git commit -m 'Add X feature'`.
4. 🫸 Push to the branch: `git push origin feature/your-feature-name`.
5. 🙏 Submit a pull request.

## Acknowledgements

- [argparse](https://docs.python.org/3/library/argparse.html) for command-line argument parsing.
- [matplotlib](https://matplotlib.org/stable/gallery/index.html) for graph generation.



