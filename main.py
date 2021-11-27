import random

turn_by_turn = random.randint(0,1)
a = [(1,'*'),(2,'*'),(3,'*'),(4,'*'),(5,'*'),(6,'*'),(7,'*'),(8,'*'),(9,'*')]
d = dict(a)

x_history = []
o_history = []

state = True

if turn_by_turn == 1:
  print('the order of O')
elif turn_by_turn == 0:
  print('the order of X')

while state:
  x = int(input('> '))
  if turn_by_turn == 0:
    class XPlayer:
      def __init__(self,x_player):
        self.x_player = x_player
      def set_x(self):
        global turn_by_turn
        if self.x_player in x_history or self.x_player in o_history or self.x_player >= 9 or self.x_player == 0:
          print('Try again !')
        while self.x_player not in x_history and self.x_player not in o_history and self.x_player <= 9 and self.x_player == 0:
          x
          if self.x_player not in x_history and self.x_player not in o_history:
            d[self.x_player] = 'X'
            x_history.append(self.x_player)
            turn_by_turn = 1
            break
    XPlayer(x).set_x()
  elif turn_by_turn == 1:
    class OPlayer():
      def __init__(self,o_player):
        self.o_player = o_player
      def set_o(self):
        global turn_by_turn

        if self.o_player in x_history or self.o_player in o_history or self.o_player >= 9 or self.o_player == 0:
          print('Try again !')
        while self.o_player not in x_history and self.o_player not in o_history and self.o_player <= 9 and self.o_player == 0:
          x
          if self.o_player not in x_history and self.o_player not in o_history:
            d[self.o_player] = 'O'
            o_history.append(self.o_player)
            turn_by_turn = 0
            break

    OPlayer(x).set_o()
  board = f"""
    | {d[1]} | {d[2]} | {d[3]} |\n
    | {d[4]} | {d[5]} | {d[6]} |\n
    | {d[7]} | {d[8]} | {d[9]} |\n
  """
  print(board)
  print(turn_by_turn)

  winning = [[1,2,3],[3,6,9],[2,5,8],[1,4,7],[1,5,9],[3,5,7],[7,8,9],[4,5,6]]

  for i in winning:
    if set(i).issubset(sorted(set(x_history))):
      print('X won')
      state = False
    if set(i).issubset(sorted(set(o_history))):
      print('O won')
      state = False
  if len(x_history) == 5 or len(o_history) == 5:
    print('TIE')
    state = False
