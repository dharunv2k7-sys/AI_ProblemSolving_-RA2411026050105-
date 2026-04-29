from flask import Flask, render_template
from sudoku_solver.sudoku import get_solution
from bfs_navigation.bfs import get_path

app = Flask(__name__)

@app.route('/')
def home():
    sudoku = get_solution()
    path = get_path()
    return render_template("index.html", sudoku=sudoku, path=path)

if __name__ == '__main__':
    app.run(debug=True)
