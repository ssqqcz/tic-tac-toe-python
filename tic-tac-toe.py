a = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def game():
  print("\n")
  print(a[0], " | ", a[1], " | ", a[2])
  print("---+-----+---")
  print(a[3], " | ", a[4], " | ", a[5])
  print("--+-----+---")
  print(a[6], " | ", a[7], " | ", a[8], "\n")


def winner():
  win = [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4,
                                                     7], [2, 5,
                                                          8], [0, 4,
                                                               8], [2, 4, 6]
  for index in win:
    if a[index[0]] == a[index[1]] == a[index[2]] != "":
      return a[index[0]]
  return None


turn = "X"
over = False
game()

while not over:
  try:
   b = int(input(f"Turn for {turn}, Choose a number btw 0-8: "))
   if b>8 or b<0:
      print('Enter number between 0 to 8')
      continue
   elif a[b] not in ["X", "O"]:
      a[b] = turn
      game()
      won = winner()
      if won:
        print(f"Winner is {won}, Congratulations!!")
        break
      elif all(r in ["X", "O"] for r in a):
        print("Its a draw")
        over = True
        break
      else:
        turn = "O" if turn == "X" else "X"
   else:
      print("This place is occupied!, Enter another number between 0-8")

  except ValueError:
    print("print an integer")