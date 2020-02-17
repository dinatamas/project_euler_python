def text_to_sudoku(text):
  sudoku = [[]]
  for t in text:
    if t == '\n':
      sudoku.append([])
    elif t != ' ':
      sudoku[-1].append(t)
  return sudoku
    

def sudoku_to_text(sudoku):
  text = ''
  for i in range(0, 9):
    text += ' '.join(sudoku[i]) + '\n'
  return text


def is_solved(sudoku):
  for i in range(0, 9):
    if sorted(sudoku[i]) != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      return False
  for i in range(0, 9):
    temp = []
    for j in range(0, 9):
      temp += sudoku[j][i]
    if sorted(temp) != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      return False
  for i in [0, 3, 6]:
    for j in [0, 3, 6]:
      temp = sudoku[i // 3 * 3 : i // 3 * 3 + 3][j // 3 * 3 : j // 3 * 3 + 3]
      print(sudoku[0:3])
      if sorted(temp) != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
  return True


def sudoku_options(sudoku):
  options = []
  for i in range(0, 9):
    options.append([])
    for j in range(0, 9):
      options[i].append([])
      for num in range(1, 10):
        if not (str(num) in sudoku[i] or
         str(num) in [sudoku[0][j] + sudoku[1][j] + sudoku[2][j] + sudoku[3][j] + sudoku[4][j] + sudoku[5][j] + sudoku[6][j] + sudoku[7][j] + sudoku[8][j]] or
         str(num) in sudoku[i // 3 : i // 3 + 3][j // 3 : j // 3 + 3]):
          options[i][j].append(num)
  for i in range(0, 9):
    for j in range(0, 9):
      print(options[i][j], end='')
    print('\n')
  return options


def solve_sudoku(sudoku):
  solution = sudoku
  return solution


if __name__ == '__main__':
  with open('sudoku.txt', 'r') as f:
    sudoku = text_to_sudoku(f.read())
    # sudoku_options(sudoku)
  with open('sudoku-solved.txt', 'r') as f:
    sudoku = text_to_sudoku(f.read())
    print(is_solved(sudoku))