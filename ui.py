import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog
import itertools
import string
import time
from copy import deepcopy
import numpy as np
from cnf import *
from check_connection import *


class nQueens(object):

    # Ref https://stackoverflow.com/questions/10903176/how-to-print-a-board-in-python
    def format_row(self, row):
        row = ['X' if x > 0 else ' ' for x in row]
        return '\t\t|' + '|'.join('{0:^3s}'.format(str(x)) for x in row) + '|'

    # Ref https://stackoverflow.com/questions/10903176/how-to-print-a-board-in-python
    def format_board(self):
        return '\n'.join(self.format_row(row) for row in self.board)

    # Ref: https://www.youtube.com/watch?v=IbpInH4q4Sg&ab_channel=Codemy.com
    def number(self):
        try:
            N = int(self.input_Size.get())
            if N > 0:
                print(N)
                self.Size = N
                self.Solution_dropdown_setup.set('Only one solution')
                self.Status.config(text="")
            else :
                self.Status.config(text="Please input a positive integer!!!", fg = "red")
        except ValueError:
            self.Status.config(text="Please input a positive integer!!!", fg = "red")

    # Generate GUI's header with corresponding dropdown options
    def generate_first_header(self):
        tk.Label(self.first_header,
                 text="""Choose your way to show solutions:""",
                 justify=tk.LEFT,
                 padx=20).grid(row=1, column=1)
        tk.Radiobutton(self.first_header,
                        text="Board",
                        padx=20,
                        variable=self.showBoard,
                        command=self.change_Radio_Type,
                        value=1).grid(row=1, column=3)
        tk.Radiobutton(self.first_header,
                        text="Text",
                        padx=20,
                        variable=self.showBoard,
                        command=self.change_Radio_Type,
                        value=2).grid(row=1, column=4)
        self.showBoard.set(1)  # initializing the choice, i.e. Show Board
        # Comment
        tk.Label(self.comment, text="Please select show only one solution if select board size more than 8, otherwise it will take more than 2 minutes.", fg = "blue").grid(row=1, column=1)


    def generate_second_header(self):
        self.Status = tk.Label(self.second_header, text="")
        if self.showBoard.get() == 1:
            # init list
            Size_dropdown_list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            Solution_dropdown_list = {'Only one solution', 'All'}
            # Size
            tk.Label(self.second_header, text="Size: ").grid(row=1, column=1)
            self.Size_dropdown_setup = tk.StringVar()
            self.Size_dropdown_setup.set(8)
            Size_dropdown = tk.OptionMenu(
                self.second_header, self.Size_dropdown_setup, *Size_dropdown_list)
            self.Size = int(self.Size_dropdown_setup.get())
            self.Size_dropdown_setup.trace('w', self.change_dropdown_Size)
            Size_dropdown.grid(row=1, column=2)
            # Solution
            tk.Label(self.second_header, text="How many solutions you want to see?: ").grid(
                row=1, column=3)
            self.Solution_dropdown_setup = tk.StringVar()
            self.Solution_dropdown_setup.set('Only one solution')
            Solution_dropdown = tk.OptionMenu(
                self.second_header, self.Solution_dropdown_setup, *Solution_dropdown_list)
            self.all = False
            self.Solution_dropdown_setup.trace('w', self.change_dropdown_Type)
            Solution_dropdown.grid(row=1, column=5)
            # Status text
            self.Status.grid(row=2, column=3)
        else:
            Solution_dropdown_list = {'Only one solution', 'All'}
            # Board size
            tk.Label(self.second_header, text="Please input the size of board: ").grid(row=1, column=1)
            tk.Entry(self.second_header, textvariable=self.input_Size).grid(row=1, column=2)
            self.input_Size.set(8)
            self.Size = 8
            tk.Button(self.second_header, text="Enter", command=self.number).grid(row=1, column=3)
            # Solution
            tk.Label(self.second_header, text="How many solutions you want to see?: ").grid(
                row=1, column=5)
            self.Solution_dropdown_setup = tk.StringVar()
            Solution_dropdown = tk.OptionMenu(
                self.second_header, self.Solution_dropdown_setup, *Solution_dropdown_list)
            self.all = False
            self.Solution_dropdown_setup.trace('w', self.change_dropdown_Type)
            self.Solution_dropdown_setup.set('Only one solution')
            Solution_dropdown.grid(row=1, column=7)
            # Status text
            self.Status.grid(row=2, column=5)
        
    # Generate GUI's Left Side Bar
    def generate_side_left(self):
        for i in range(self.Size):
            label = tk.Label(master=self.side_left,
                             height=3, width=3, text=i + 1)
            label.grid(row=i, column=0, padx=0, pady=3)
        pass

    # Generate GUI's Right Side Bar
    def generate_side_right(self):
        # Select Solution number
        tk.Label(self.side_right, text="Solution No.: ").grid(row=5, column=1)
        self.Sol_no_dropdown_setup = tk.StringVar()
        self.Sol_no_dropdown_setup.set(1)
        Sol_no_dropdown = tk.OptionMenu(self.side_right, self.Sol_no_dropdown_setup, *self.Sol_no_dropdown_list)
        self.solution_no = int(self.Sol_no_dropdown_setup.get())-1
        self.Sol_no_dropdown_setup.trace('w', self.change_dropdown_Solution)
        Sol_no_dropdown.grid(row=5, column=2)

    # Get the list of alphabet
    # Ref: https://stackoverflow.com/questions/42176498/repeating-letters-like-excel-columns/42176541
    def excel_cols(self):
        n = 1
        while True:
            yield from (''.join(group) for group in itertools.product(string.ascii_uppercase, repeat=n))
            n += 1

    # Generate Sub Header -> A B C D
    def generate_board_header(self):
        board_header = list(itertools.islice(self.excel_cols(), self.Size))
        for j in range(self.Size + 1):
            if j == 0:
                label = tk.Label(master=self.board_header, width=0, text=" ")
                label.grid(row=0, column=j)
            else:
                label = tk.Label(master=self.board_header,
                                 width=6, text=board_header[j - 1])
                label.grid(row=0, column=j)

    # Generate Squeeze-It board
    def generate_board(self):
        self.generate_board_header()
        self.generate_side_left()
        for i in range(self.Size):
            for j in range(self.Size):
                self.frame = tk.Frame(
                    master=self.body,
                    relief=tk.RAISED,
                    width=60,
                    height=60,
                    borderwidth=2)
                self.frame.grid(row=i, column=j)
        self.add_element_to_board()

    # Delete piece from board
    def del_element(self, Row, Column):
        widget = self.body.grid_slaves(row=Row, column=Column)[0]
        widget.destroy()
        root.update()
        pass

    # Add piece to board
    def draw_element(self, Row, Column, Color):
        canvas = tk.Canvas(self.body, bg='white', width=50, height=50)
        canvas.grid(row=Row, column=Column)
        canvas.create_oval(5, 5, 50, 50, fill=Color)
        root.update()

    # Add the pieces to board (2D list and GUI)
    def add_element_to_board(self):
        if self.Size <= 40:
            for i in range(self.Size):
                for j in range(self.Size):
                    if self.board[i][j] > 0:
                        self.draw_element(i, j, "red")

    # Trigger event when changing the dropdown
    def change_Radio_Type(self, *args):
        for child in self.second_header.winfo_children():
            child.destroy()
        self.generate_second_header()
        self.root.update()
        for child in self.body.winfo_children():
            child.destroy()
        for child in self.board_header.winfo_children():
            child.destroy()
        for child in self.side_left.winfo_children():
            child.destroy()
        for child in self.side_right.winfo_children():
            child.destroy()
        self.root.update()
        ###################### Init Value ########################################
        self.init_value()

    def change_dropdown_Type(self, *args):
        if self.Solution_dropdown_setup.get() == 'All':
            self.all = True
        else:
            self.all = False
        for child in self.body.winfo_children():
            child.destroy()
        for child in self.board_header.winfo_children():
            child.destroy()
        for child in self.side_left.winfo_children():
            child.destroy()
        for child in self.side_right.winfo_children():
            child.destroy()
        ###################### Init Value ########################################
        self.init_value()

    def change_dropdown_Size(self, *args):
        self.Size = int(self.Size_dropdown_setup.get())
        self.Solution_dropdown_setup.set('Only one solution')

    def change_dropdown_Solution(self, *args):
        self.solution_no = int(self.Sol_no_dropdown_setup.get())-1
        for child in self.body.winfo_children():
            child.destroy()
        self.filled_up_the_board()

    def check_connection(self):
        self.username = tk.simpledialog.askstring(
            "Input", "Enter username:", parent=self.root)
        if self.username is not None:
            self.password = tk.simpledialog.askstring(
                "Password", "Enter password:", show='*', parent=self.root)
            if self.password is not None:
                self.check_connect = check_connection(
                    self.username, self.password)
            else:
                self.root.destroy()
                self.check_connect = 2
        else:
            self.root.destroy()
            self.check_connect = 2
        while(self.check_connect == 1):
            messagebox.showerror(
                "Error", "Cannot connect to the SSH Server. Maybe username or password wrong, Please try again!")
            self.username = tk.simpledialog.askstring(
                "Input", "Enter username:", parent=self.root)
            if self.username is not None:
                self.password = tk.simpledialog.askstring(
                    "Password", "Enter password:", show='*', parent=self.root)
                if self.password is not None:
                    self.check_connect = check_connection(
                        self.username, self.password)
                else:
                    self.root.destroy()
                    self.check_connect = 2
            else:
                self.root.destroy()
                self.check_connect = 2

    # Initial function
    def __init__(self, root):
        self.root = root
        self.username = None
        self.password = None
        # Condition to show solutions
        self.all = False

        self.check_connect = None
        # Check ssh connection
        self.check_connection()
        if self.check_connect == 0:
            # init frame
            self.first_header = tk.Frame(master=self.root, bg="white")
            self.first_header.grid(row=0, column=1)
            self.comment = tk.Frame(master=self.root, bg="white")
            self.comment.grid(row=1, column=1)
            self.second_header = tk.Frame(master=self.root, bg="white")
            self.second_header.grid(row=2, column=1)
            self.side_left = tk.Frame(master=self.root, bg="white")
            self.side_left.grid(row=4, column=0)
            self.side_right = tk.Frame(master=self.root, bg="white")
            self.side_right.grid(row=4, column=2)
            self.board_header = tk.Frame(master=self.root, bg="white")
            self.board_header.grid(row=3, column=1)
            self.body = tk.Frame(master=self.root, bg="white")
            self.body.grid(row=4, column=1, padx=5, pady=5)
            self.Status = tk.Label(self.second_header, text="")
            self.input_Size = tk.StringVar()
            self.Size = None
            self.board = []
            self.solutions = []

            self.showBoard = tk.IntVar()

            # Init variable for dropdown and label on the right side bar
            self.Sol_no_dropdown_list = []
            self.solution_no = None

            # Generate First Header
            self.generate_first_header()
            # Generate Second Header
            self.generate_second_header()
            ###################### Init Value ########################################
            self.init_value()

    # Initial values
    def init_value(self):
        if self.showBoard.get() == 1:
            self.board = [[0]*self.Size]*self.Size
            self.solutions = []
            self.Sol_no_dropdown_list = []
            self.solution_no = 0
            self.Status.config(text="Please wait~~~", fg="blue")
            self.root.update()
            self.solutions = cnf(self.username, self.password, self.Size, self.all)
            self.filled_up_the_board()
            self.generate_side_right()
            self.Status.config(text="")
            self.root.update()
        else:
            self.board = [[0]*self.Size]*self.Size
            self.solutions = []
            self.Status.config(text="Please wait~~~", fg="blue")
            self.root.update()
            self.solutions = cnf(self.username, self.password, self.Size, self.all)
            self.generate_textbox()
            self.filled_up_the_textbox()
            self.Status.config(text="")
            self.root.update()

    def generate_textbox(self):
        scrollbarY = tk.Scrollbar(self.body, orient=tk.VERTICAL)
        scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbarX = tk.Scrollbar(self.body, orient=tk.HORIZONTAL)
        scrollbarX.pack(side=tk.BOTTOM, fill=tk.X)
        self.textbox = tk.Text(self.body, wrap=tk.NONE)
        self.textbox.pack()
        # attach textbox to scrollbarY and scrollbarX
        self.textbox.config(yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
        scrollbarY.config(command=self.textbox.yview)
        scrollbarX.config(command=self.textbox.xview)
    # Filled up the textbox
    def filled_up_the_textbox(self):
        if len(self.solutions) == 0:
            self.textbox.insert(tk.END,"No solution!")
            pass
        else:
            for i in range(len(self.solutions)):
                self.textbox.insert(tk.END,'\nSolution No.:'+str(int(i+1))+'\n')
                self.board = self.to2D(self.solutions[i])
                text = self.format_board() + '\n\n'
                self.textbox.insert(tk.END, text)
                self.textbox.insert(tk.END, 'List: '+str(self.solutions[i])+'\n')

    # Filled up the board
    def filled_up_the_board(self):
        if len(self.solutions) == 0:
            self.board = [[0]*self.Size]*self.Size
            self.Sol_no_dropdown_list = [1]
            pass
        else:
            self.board = self.to2D(self.solutions[self.solution_no])
            self.Sol_no_dropdown_list = [*range(1, len(self.solutions)+1, 1)]
        self.generate_board()

    def to2D(self, l):
        matrix = []
        for i in range(0, len(l), self.Size):
            matrix.append(l[i:i+self.Size])
        return matrix


if __name__ == "__main__":
    root = tk.Tk()
    root.title("N-Queens")
    nQueens(root)
    root.mainloop()
