# Ref: https://www.coursera.org/lecture/automated-reasoning-sat/eight-queens-problem-KZzKe
from pysat.formula import CNF
import os
import paramiko
import pathlib
import time


def cnf(username, password, N, show_all):

    # Function to create clauses
    def atLeastOneQueen(propositions, cnf):
        # A11 V A12 V ... V A1N
        # Add clauses to the CNF object
        cnf.append(propositions)

    def atMostOneQueen(propositions, cnf):
        # -A11 V -A12
        # -Aij V -Aik for every j<k
        for k in range(len(propositions)):
            for j in range(k):
                temp = []
                temp.append(-propositions[j])
                temp.append(-propositions[k])
                # Add clauses to the CNF object
                cnf.append(temp)

    # Get the size of the board
    # N = input()
    N = int(N)

    # Created an object of class CNF
    cnf = CNF()
    # Initial variable
    solutions = []
    board = [[(j+(i*N)+1) for j in range(N)] for i in range(N)]

    # Every Row and Column
    for i in range(N):
        propositions_row = []
        propositions_col = []
        for j in range(N):
            propositions_row.append(board[i][j])
            propositions_col.append(board[j][i])
        # At least one queen on every row
        atLeastOneQueen(propositions_row, cnf)
        # At least one queen on every column
        atMostOneQueen(propositions_row, cnf)
        # At least one queen on every column
        atLeastOneQueen(propositions_col, cnf)
        # At most one queen on every column
        atMostOneQueen(propositions_col, cnf)

    # Every Diagonal
    for i in [0, N-1]:
        for j in range(N):
            propositions1 = []
            propositions2 = []
            for i_ in range(N):
                for j_ in range(N):
                    if i == N-1 and j == 0:
                        pass
                    elif i == N-1 and j == N-1:
                        pass
                    else:
                        if i == i_ and j == j_:
                            propositions1.append(board[i_][j_])
                            propositions2.append(board[i_][j_])
                        elif i-j == i_-j_:
                            propositions1.append(board[i_][j_])
                        elif i+j == i_+j_:
                            propositions2.append(board[i_][j_])
            # At most one queen on every diagonal in the first direction \
            atMostOneQueen(propositions1, cnf)
            # At most one queen on every diagonal in the second direction /
            atMostOneQueen(propositions2, cnf)

    # Connect to the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connect = 1
    while(connect):
        try:
            client.connect(hostname="willow.cs.ttu.edu", username=username, password=password, banner_timeout=2000)
            ftp_client = client.open_sftp()
            connect = 0
        except:
            print("[1] Cannot connect to the SSH Server")
            # Close connection
            client.close()
            connect = connect+5
            time.sleep(connect)

    # Find all posible solutions
    while(True):
        while(connect):
            try:
                client.connect(hostname="willow.cs.ttu.edu", username=username, password=password, banner_timeout=2000)
                ftp_client = client.open_sftp()
                connect = 0
            except:
                print("[2] Cannot connect to the SSH Server")
                # Close connection
                client.close()
                connect = connect+5
                time.sleep(connect)
        try:
            # Write CNF file
            cnf.to_file('input.cnf')
            path = str(pathlib.Path().absolute()) + '/input.cnf'
            ftp_client.put(path, 'input.cnf')
            # Read output.txt file
            stdin, stdout, stderr = client.exec_command("./MiniSat_v1.14_linux input.cnf output.txt")
            # stdout.read().decode()
            err = stderr.read().decode()
            if err:
                print(err)
            ftp_client.get('output.txt', 'output.txt')
            f = open('output.txt', 'r')
            if f.readline() == "SAT\n":
                line = f.readline()
                while line:
                    line = line.rstrip()  # strip trailing spaces and newline
                    # process the line
                    t = line.split()
                    clause = []
                    neg_clause = []
                    for i in t:
                        if int(i) == 0:
                            break
                        clause.append(int(i))
                        neg_clause.append(-int(i))
                    solutions.append(clause)
                    cnf.append(neg_clause)
                    line = f.readline()
                f.close()
            else:
                f.close()
                break
            if show_all == False:
                break
        except:
            print("[3] Connect Error")
            # Close connection
            ftp_client.close()
            client.close()
            connect = connect+5
    # Close connection
    ftp_client.close()
    client.close()
    # Print solutions
    print(len(solutions))
    # clear file
    if os.path.exists("input.cnf"):
        os.remove("input.cnf")
    else:
        print("The input.cnf file does not exist.")
    if os.path.exists("output.txt"):
        os.remove("output.txt")
    else:
        print("The output.txt file does not exist.")
    # Return solutions
    return(solutions)


