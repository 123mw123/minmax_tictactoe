import random

tie_game = 0
ai_player = 1
human_player = 2
no_val =0
move = {}



def print_board(board):
    for i in range(len(board)):
        print board[i],
        if ((i + 1) % 3 == 0):
            print "\n"


def deploy(board, i,player):
    if(player == ai_player):
        board[i] = 'O'
    elif(player == human_player):
        board[i] = 'X'
    elif(player == no_val):
        board[i] = '-'


def isValid_move(board, position):
    valid = False
    if(board[position] == '-'):
        valid = True
        return valid
    else:
        return valid


def goal_condition(board):
    if ((board[0] == board[1] == board[2] == 'X') or
            (board[0] == board[1] == board[2] == 'O') or
            (board[0] == board[4] == board[8] == 'X') or
            (board[0] == board[4] == board[8] == 'O') or
            (board[0] == board[3] == board[6] == 'X') or
            (board[0] == board[3] == board[6] == 'O') or
            (board[1] == board[4] == board[7] == 'X') or
            (board[1] == board[4] == board[7] == 'O') or
            (board[2] == board[5] == board[8] == 'X') or
            (board[2] == board[5] == board[8] == 'O') or
            (board[3] == board[4] == board[5] == 'X') or
            (board[3] == board[4] == board[5] == 'O') or
            (board[2] == board[6] == board[4] == 'X') or
            (board[2] == board[6] == board[4] == 'O') or
            (board[6] == board[7] == board[8] == 'X') or
            (board[6] == board[7] == board[8] == 'O')):
        return True
    else:
        return False



def check_winner(board):


    if ((board[0] == board[1] == board[2] == 'X') or

            (board[0] == board[4] == board[8] == 'X') or

            (board[0] == board[3] == board[6] == 'X') or

            (board[1] == board[4] == board[7] == 'X') or

            (board[2] == board[5] == board[8] == 'X') or

            (board[3] == board[4] == board[5] == 'X')  or

            (board[2] == board[6] == board[4] == 'X')  or

            (board[6] == board[7] == board[8] == 'X') ):

        return human_player


    elif(
            (board[0] == board[1] == board[2] == 'O') |

            (board[0] == board[4] == board[8] == 'O') |

            (board[0] == board[3] == board[6] == 'O') |

            (board[1] == board[4] == board[7] == 'O') |

            (board[2] == board[5] == board[8] == 'O') |

            (board[3] == board[4] == board[5] == 'O') |

            (board[2] == board[6] == board[4] == 'O') |

            (board[6] == board[7] == board[8] == 'O')):
        return ai_player
    if '-' not in board:
        return tie_game
    else:
        return -1


def minimax(board,d,a,b,player):
    global move

    if (check_winner(board) == ai_player):

        return 100.0 + float(random.uniform(0,1))-float(d)

    elif (check_winner(board) == human_player):

        return 0.0 + float(random.uniform(0,1))+float(d)
    elif (check_winner(board) == tie_game):

        return 50.0+float(random.uniform(0,1))-float(d)



    if (player == ai_player):
        v = float(-99999999)

        for i in range(0, len(board)):

            if (isValid_move(board, i)):

                deploy(board, i, player)


                v1= minimax(board, d + 1, a, b, human_player)
                v = max(v,v1)

                '''if (v > b):

                    deploy(board, i, no_val)

                   
                    break'''
                if (d == 1):
                    move[i] = v1

                #a = max(a, v)
                deploy(board, i, no_val)

        return v
    elif (player == human_player):
        v = float(99999999)

        for i in range(0, len(board)):

            if (isValid_move(board, i)):

                deploy(board, i, player)

                v2 = minimax(board, d + 1, a, b, ai_player)
                v = min(v, v2)
                '''if (a>v):
                    
                    deploy(board, i, no_val)

                    break
                b = min(b, v)'''
                deploy(board, i, no_val)
        return v


board = ['-' for x in range(0, 9)]
print_board(board)
while(goal_condition(board) != True):
    print "Human's Turn"
    var = int(raw_input("Please Enter 0-8: "))
    if (isValid_move(board, var) == True):
        deploy(board, var, human_player)
        print_board(board)

    if ('-' in board):
        print "searching..."
        minimax(board, 1, float(-99999999), float(99999999), True)
        print move

        j = None
        u=[]
        for i in move.keys():
            u.append(move[i])
        for i in move.keys():
            if move[i] == max(u):
                j = i
                print i
        move = {}

        deploy(board, j, ai_player)
        print_board(board)


