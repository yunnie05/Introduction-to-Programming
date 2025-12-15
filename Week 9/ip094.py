'''
# Função para contar os vizinhos vivos de uma célula
def count_alive_neighbors(grid, r, c, rows, cols):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#':
            count += 1
    return count

# Função para calcular a próxima geração do grid
def next_generation(grid, rows, cols):
    new_grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            alive_neighbors = count_alive_neighbors(grid, r, c, rows, cols)
            if grid[r][c] == '#':
                # Regras para célula viva
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[r][c] = '.' 
            else:
                # Regra para célula morta
                if alive_neighbors == 3:
                    new_grid[r][c] = '#'  
    return new_grid

# Função principal para rodar o jogo por K gerações
def game_of_life(rows, cols, k, grid):
    for _ in range(k):
        grid = next_generation(grid, rows, cols)
    return grid

# Função para imprimir o grid final
def print_grid(grid):
    for row in grid:
        print(''.join(row))

# Função para ler os dados de entrada
def read_input():
    rows, cols, k = map(int, input().split())
    grid = [list(input().strip()) for _ in range(rows)]
    return rows, cols, k, grid
  
def main():
    rows, cols, k, grid = read_input()
    result = game_of_life(rows, cols, k, grid)
    print_grid(result)

main()
'''

def main():
    cols,lin, k, grid= read_input()
    
def read_input():
    a= input().split()
    cols= a[0]
    lin= a[1]
    k= 
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              