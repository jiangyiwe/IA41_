import numpy as np
import pieces
#Parce que la grille de notre jeu est de 5 rangées et 11 colonnes.


def start_position(num):
    n_rows = 5
    n_cols = 11
    if num == 0:
        # Retourne une grille vide et tous les pieces
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        available_pieces = [
            pieces.pink(),
            pieces.red(),
            pieces.dark_red(),
            pieces.blue(),
            pieces.light_blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.light_green(),
            pieces.dark_green(),
            pieces.purple(),
            pieces.yellow(),
            pieces.orange(),
        ]
        return grid, available_pieces

    if num == 1:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] = grid[:4, :2] + pieces.pink().variants[0]
        grid[2:, :3] = grid[2:, :3] + pieces.blue().variants[0]
        grid[:2, 1:5] = grid[:2, 1:5] + pieces.yellow().variants[0]
        grid[1:4, 2:4] = grid[1:4, 2:4] + pieces.dark_green().variants[0]
        grid[3:, 3:5] = grid[3:, 3:5] + pieces.light_blue().variants[0]
        grid[:3, 4:7] = grid[:3, 4:7] + pieces.orange().variants[0]
        grid[2:, 4:6] = grid[2:, 4:6] + pieces.dark_red().variants[0]
        grid[:2, 6:9] = grid[:2, 6:9] + pieces.dark_blue().variants[0]
        grid[3:, 6:9] = grid[3:, 6:9] + pieces.light_green().variants[0]
        available_pieces = [
            pieces.red(),
            pieces.green(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 2:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] = grid[:3, :2] + pieces.dark_blue().variants[5]
        grid[3:, :3] = grid[3:, :3] + pieces.light_green().variants[0]
        grid[:3, 1:3] = grid[:3, 1:3] + pieces.dark_red().variants[2]
        grid[2:, 2:5] = grid[2:, 2:5] + pieces.purple().variants[0]
        grid[:4, 3:5] = grid[:4, 3:5] + pieces.pink().variants[2]
        grid[:2, 4:8] = grid[:2, 4:8] + pieces.yellow().variants[0]
        grid[1:, 4:6] = grid[1:, 4:6] + pieces.red().variants[0]
        grid[3:, 6:8] = grid[3:, 6:8] + pieces.light_blue().variants[0]
        grid[:2, 8:] = grid[:2, 8:] + pieces.green().variants[0]
        available_pieces = [
            pieces.blue(),
            pieces.orange(),
            pieces.dark_green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 3:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :2] = grid[:2, :2] + pieces.light_blue().variants[0]
        grid[2:, :2] = grid[2:, :2] + pieces.green().variants[1]
        grid[:2, 1:5] = grid[:2, 1:5] + pieces.yellow().variants[4]
        grid[1:4, 1:4] = grid[1:4, 1:4] + pieces.purple().variants[1]
        grid[3:, 2:6] = grid[3:, 2:6] + pieces.red().variants[3]
        grid[1:4, 3:6] = grid[1:4, 3:6] + pieces.orange().variants[4]
        grid[:4, 5:7] = grid[:4, 5:7] + pieces.pink().variants[0]
        grid[:2, 6:9] = grid[:2, 6:9] + pieces.dark_green().variants[3]
        grid[2:, 6:8] = grid[2:, 6:8] + pieces.dark_blue().variants[7]
        available_pieces = [
            pieces.blue(),
            pieces.light_green(),
            pieces.dark_red()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 4:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] = grid[:2, :3] + pieces.dark_green().variants[3]
        grid[1:4, :3] = grid[1:4, :3] + pieces.blue().variants[0]
        grid[3:, :4] = grid[3:, :4] + pieces.red().variants[3]
        grid[:3, 1:4] = grid[:3, 1:4] + pieces.purple().variants[1]
        grid[:4, 3:5] = grid[:4, 3:5] + pieces.yellow().variants[3]
        grid[:3, 5:7] = grid[:3, 5:7] + pieces.green().variants[1]
        grid[3:, 4:7] = grid[3:, 4:7] + pieces.dark_red().variants[1]
        grid[:3, 6:9] = grid[:3, 6:9] + pieces.orange().variants[6]
        grid[3:, 6:8] = grid[3:, 6:8] + pieces.light_blue().variants[1]
        available_pieces = [
            pieces.dark_blue(),
            pieces.light_green(),
            pieces.pink()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 5:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] = grid[:2, :3] + pieces.dark_red().variants[3]
        grid[:2, 2:5] = grid[:2, 2:5] + pieces.light_green().variants[2]
        grid[:4, 4:6] = grid[:4, 4:6] + pieces.pink().variants[6]
        grid[3:, 4:8] = grid[3:, 4:8] + pieces.yellow().variants[2]
        grid[:4, 6:8] = grid[:4, 6:8] + pieces.red().variants[4]
        grid[:3, 8:] = grid[:3, 8:] + pieces.blue().variants[2]
        grid[1:3, 7:10] = grid[1:3, 7:10] + pieces.green().variants[0]
        grid[2:, 7:10] += pieces.orange().variants[0]
        grid[3:, 9:] += pieces.light_blue().variants[2]
        available_pieces = [
            pieces.dark_green(),
            pieces.purple(),
            pieces.dark_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 6:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.green().variants[1]
        grid[:2, 1:5] += pieces.yellow().variants[2]
        grid[:3, 3:6] += pieces.blue().variants[2]
        grid[3:, 5:8] += pieces.light_green().variants[0]
        grid[:3, 6:8] += pieces.dark_blue().variants[5]
        grid[:3, 9:] += pieces.dark_green().variants[2]
        grid[:3, 7:10] += pieces.purple().variants[3]
        grid[2:, 7:10] += pieces.orange().variants[0]
        grid[2:, 9:] += pieces.dark_red().variants[0]
        available_pieces = [
            pieces.pink(),
            pieces.red(),
            pieces.light_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 7:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.light_green().variants[0]
        grid[:2, 2:5] += pieces.dark_green().variants[3]
        grid[:3, 4:7] += pieces.orange().variants[5]
        grid[2:, 4:6] += pieces.dark_blue().variants[3]
        grid[3:, 6:10] += pieces.red().variants[5]
        grid[:2, 6:10] += pieces.pink().variants[5]
        grid[2:4, 7:9] += pieces.light_blue().variants[0]
        grid[:3, 8:] += pieces.blue().variants[2]
        grid[2:, 8:] += pieces.purple().variants[2]
        available_pieces = [
            pieces.yellow(),
            pieces.dark_red(),
            pieces.green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 8:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.green().variants[0]
        grid[:4, 3:5] += pieces.pink().variants[0]
        grid[:3, 4:6] += pieces.dark_blue().variants[3]
        grid[3:, 4:7] += pieces.light_green().variants[4]
        grid[:3, 6:9] += pieces.blue().variants[3]
        grid[:2, 8:] += pieces.dark_red().variants[1]
        grid[1:4, 9:] += pieces.dark_green().variants[2]
        grid[1:4, 7:10] += pieces.purple().variants[0]
        grid[3:, 7:] += pieces.red().variants[5]
        available_pieces = [
            pieces.yellow(),
            pieces.orange(),
            pieces.light_blue()
        ]
        print(pieces.yellow().variants[0])
        print(    pieces.orange().variants[0])
        print( pieces.light_blue().variants[0])
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 9:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :3] += pieces.blue().variants[3]
        grid[1:, :2] += pieces.pink().variants[6]
        grid[3:, 1:5] += pieces.yellow().variants[2]
        grid[1:4, 2:5] += pieces.purple().variants[0]
        grid[:2, 3:5] += pieces.light_blue().variants[0]
        grid[:2, 4:7] += pieces.dark_green().variants[3]
        grid[2:, 4:6] += pieces.dark_blue().variants[3]
        grid[1:3, 6:9] += pieces.dark_red().variants[3]
        available_pieces = [
            pieces.orange(),
            pieces.green(),
            pieces.red(),
            pieces.light_green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 10:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] += pieces.yellow().variants[5]
        grid[3:, :3] += pieces.dark_green().variants[1]
        grid[:4, 1:3] += pieces.pink().variants[0]
        grid[:4, 2:4] += pieces.red().variants[0]
        grid[2:, 3:6] += pieces.orange().variants[4]
        grid[:2, 4:6] += pieces.light_blue().variants[3]
        grid[1:4, 5:7] += pieces.dark_red().variants[0]
        grid[3:, 5:8] += pieces.dark_blue().variants[2]
        available_pieces = [
            pieces.blue(),
            pieces.light_green(),
            pieces.green(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 11:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :4] += pieces.yellow().variants[4]
        grid[1:4, :3] += pieces.orange().variants[7]
        grid[3:, :3] += pieces.green().variants[2]
        grid[1:, 2:4] += pieces.red().variants[0]
        grid[:3, 4:6] += pieces.dark_blue().variants[5]
        grid[2:, 4:7] += pieces.purple().variants[3]
        grid[:2, 5:8] += pieces.dark_red().variants[1]
        grid[3:, 5:7] += pieces.light_blue().variants[1]
        available_pieces = [
            pieces.light_green(),
            pieces.dark_green(),
            pieces.blue(),
            pieces.pink()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 12:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.light_green().variants[2]
        grid[:3, 3:6] += pieces.blue().variants[2]
        grid[:2, 6:9] += pieces.dark_blue().variants[0]
        grid[:2, 7:] += pieces.pink().variants[3]
        grid[2:4, 6:9] += pieces.dark_green().variants[3]
        grid[3:, 6:8] += pieces.light_blue().variants[0]
        grid[1:4, 9:] += pieces.dark_red().variants[2]
        grid[3:, 8:] += pieces.green().variants[2]
        available_pieces = [
            pieces.yellow(),
            pieces.red(),
            pieces.orange(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 13:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.green().variants[1]
        grid[:2, 1:4] += pieces.dark_red().variants[1]
        grid[2:4, :4] += pieces.pink().variants[3]
        grid[3:, :4] += pieces.red().variants[3]
        grid[:2, 4:7] += pieces.dark_green().variants[3]
        grid[1:4, 3:6] += pieces.orange().variants[2]
        grid[3:, 4:6] += pieces.light_blue().variants[1]
        grid[:2, 7:10] += pieces.light_green().variants[2]
        available_pieces = [
            pieces.yellow(),
            pieces.blue(),
            pieces.dark_blue(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 14:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.light_green().variants[3]
        grid[3:, :2] += pieces.light_blue().variants[0]
        grid[:3, 2:4] += pieces.dark_green().variants[0]
        grid[:3, 3:5] += pieces.green().variants[3]
        grid[2:, 1:4] += pieces.purple().variants[0]
        grid[3:, 3:6] += pieces.dark_red().variants[3]
        grid[:3, 5:8] += pieces.blue().variants[3]
        grid[2:, 5:8] += pieces.orange().variants[0]
        available_pieces = [
            pieces.yellow(),
            pieces.red(),
            pieces.pink(),
            pieces.dark_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 15:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :3] += pieces.orange().variants[2]
        grid[1:4, :3] += pieces.blue().variants[0]
        grid[3:, :4] += pieces.red().variants[3]
        grid[:3, 2:4] += pieces.green().variants[3]
        grid[:4, 4:6] += pieces.yellow().variants[5]
        grid[3:, 4:7] += pieces.dark_green().variants[1]
        grid[:2, 5:7] += pieces.light_blue().variants[3]
        grid[1:, 6:8] += pieces.pink().variants[2]
        available_pieces = [
            pieces.dark_red(),
            pieces.light_green(),
            pieces.purple(),
            pieces.dark_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 16:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] += pieces.pink().variants[0]
        grid[2:, :3] += pieces.blue().variants[0]
        grid[:4, 1:3] += pieces.red().variants[0]
        grid[:4, 3:5] += pieces.yellow().variants[5]
        grid[:2, 4:6] += pieces.light_blue().variants[0]
        grid[2:, 3:6] += pieces.purple().variants[1]
        grid[:2, 5:8] += pieces.dark_green().variants[3]
        grid[2:, 5:7] += pieces.dark_blue().variants[7]
        available_pieces = [
            pieces.dark_red(),
            pieces.light_green(),
            pieces.orange(),
            pieces.green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num ==17:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.dark_red().variants[3]
        grid[1:4, :2] += pieces.dark_green().variants[0]
        grid[2:, :3] += pieces.purple().variants[1]
        grid[:2, 2:6] += pieces.pink().variants[7]
        grid[1:, 2:4] += pieces.red().variants[6]
        grid[:3, 5:7] += pieces.dark_blue().variants[3]
        grid[:3, 7:9] += pieces.green().variants[1]
        available_pieces = [
            pieces.light_blue(),
            pieces.light_green(),
            pieces.orange(),
            pieces.yellow(),
            pieces.blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 18:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] += pieces.pink().variants[0]
        grid[2:, :3] += pieces.blue().variants[0]
        grid[:2, 1:4] += pieces.dark_green().variants[3]
        grid[:3, 2:5] += pieces.purple().variants[1]
        grid[3:, 2:5] += pieces.light_green().variants[2]
        grid[:2, 5:9] += pieces.yellow().variants[0]
        grid[:4, 9:] += pieces.red().variants[0]
        available_pieces = [
            pieces.light_blue(),
            pieces.green(),
            pieces.orange(),
            pieces.dark_red(),
            pieces.dark_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 19:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.green().variants[0]
        grid[:2, 3:6] += pieces.light_green().variants[2]
        grid[:3, 6:8] += pieces.dark_blue().variants[5]
        grid[:3, 7:10] += pieces.purple().variants[3]
        grid[:4, -2:] += pieces.pink().variants[4]
        grid[2:, -4:-2] += pieces.dark_red().variants[2]
        grid[2:, -3:] += pieces.blue().variants[1]
        available_pieces = [
            pieces.light_blue(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.red(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 20:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.dark_green().variants[0]
        grid[:2, 1:5] += pieces.yellow().variants[0]
        grid[:3, 5:8] += pieces.blue().variants[2]
        grid[:2, -3:] += pieces.green().variants[0]
        grid[2:, -4:-2] += pieces.dark_red().variants[2]
        grid[1:3, -2:] += pieces.light_blue().variants[0]
        grid[3:, -3:] += pieces.light_green().variants[4]
        available_pieces = [
            pieces.pink(),
            pieces.purple(),
            pieces.orange(),
            pieces.red(),
            pieces.dark_blue()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 21:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] += pieces.yellow().variants[5]
        grid[3:, :3] += pieces.dark_green().variants[1]
        grid[:3, 1:4] += pieces.purple().variants[0]
        grid[:2, 2:4] += pieces.light_blue().variants[2]
        grid[:2, 4:7] += pieces.green().variants[0]
        grid[2:4, -5:-1] += pieces.pink().variants[7]
        available_pieces = [
            pieces.dark_red(),
            pieces.blue(),
            pieces.orange(),
            pieces.red(),
            pieces.dark_blue(),
            pieces.light_green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 22:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.green().variants[1]
        grid[3:, :3] += pieces.light_green().variants[6]
        grid[:3, 2:5] += pieces.purple().variants[2]
        grid[1:3, 1:4] += pieces.dark_red().variants[3]
        grid[3:, 2:4] += pieces.light_blue().variants[1]
        grid[:2, 4:8] += pieces.red().variants[7]
        available_pieces = [
            pieces.yellow(),
            pieces.blue(),
            pieces.orange(),
            pieces.dark_blue(),
            pieces.dark_green(),
            pieces.pink()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 23:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :3] += pieces.blue().variants[3]
        grid[:2, 2:5] += pieces.dark_green().variants[1]
        grid[:2, 4:6] += pieces.light_blue().variants[2]
        grid[:3, -5:-3] += pieces.dark_red().variants[0]
        grid[:2, -4:] += pieces.yellow().variants[0]
        grid[1:3, -3:] += pieces.green().variants[2]
        available_pieces = [
            pieces.red(),
            pieces.purple(),
            pieces.orange(),
            pieces.dark_blue(),
            pieces.light_green(),
            pieces.pink()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num ==24:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.dark_red().variants[0]
        grid[2:, :3] += pieces.blue().variants[0]
        grid[:2, 1:5] += pieces.pink().variants[5]
        grid[:2, 3:6] += pieces.dark_blue().variants[4]
        grid[:2, -5:-1] += pieces.yellow().variants[0]
        grid[2:, 1:4] += pieces.orange().variants[5]
        available_pieces = [
            pieces.red(),
            pieces.purple(),
            pieces.green(),
            pieces.light_blue(),
            pieces.light_green(),
            pieces.dark_green()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 25:
        # Starting position 25
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:4, :2] += pieces.pink().variants[2]
        grid[:2, 1:3] += pieces.light_blue().variants[3]
        grid[:3, 3:6] += pieces.purple().variants[2]
        grid[:2, 5:9] += pieces.yellow().variants[4]
        grid[:2, -3:] += pieces.light_green().variants[4]

        available_pieces = [
            pieces.red(),
            pieces.dark_red(),
            pieces.blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.dark_green(),
            pieces.orange()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 26:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :4] += pieces.yellow().variants[0]
        grid[1:3, :3] += pieces.dark_red().variants[3]
        grid[:3, 3:6] += pieces.purple().variants[3]
        grid[:3, 5:7] += pieces.light_green().variants[1]
        grid[:2, -4:-2] += pieces.light_blue().variants[2]
        available_pieces = [
            pieces.red(),
            pieces.blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.pink()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 27:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)

        grid[:3, :2] += pieces.dark_red().variants[0]
        grid[2:, :2] += pieces.dark_green().variants[0]
        grid[:2, 1:5] += pieces.pink().variants[5]
        grid[:2, 3:7] += pieces.yellow().variants[0]
        grid[1:3, 6:8] += pieces.light_blue().variants[3]
        available_pieces = [
            pieces.red(),
            pieces.blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.light_green(),
            pieces.orange(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 28:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.dark_red().variants[0]
        grid[2:, :2] += pieces.light_green().variants[7]
        grid[:2, 1:3] += pieces.light_blue().variants[2]
        grid[:2, 3:6] += pieces.dark_blue().variants[0]
        grid[:2, 4:8] += pieces.pink().variants[3]
        available_pieces = [
            pieces.red(),
            pieces.blue(),
            pieces.yellow(),
            pieces.green(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 29:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :2] += pieces.light_blue().variants[2]
        grid[:2, 2:5] += pieces.green().variants[0]
        grid[1:3, 2:5] += pieces.dark_green().variants[1]
        grid[2:4, 4:8] += pieces.pink().variants[1]
        available_pieces = [
            pieces.red(),
            pieces.blue(),
            pieces.yellow(),
            pieces.light_green(),
            pieces.dark_blue(),
            pieces.orange(),
            pieces.purple(),
            pieces.dark_red()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num ==30:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :3] += pieces.blue().variants[3]
        grid[:2, 3:5] += pieces.light_blue().variants[2]
        grid[:2, 5:8] += pieces.light_green().variants[6]
        grid[1:4, -4:-2] += pieces.dark_green().variants[0]
        available_pieces = [
            pieces.red(),
            pieces.pink(),
            pieces.yellow(),
            pieces.green(),
            pieces.dark_blue(),
            pieces.orange(),
            pieces.purple(),
            pieces.dark_red()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 31:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)

        grid[:2, :4] += pieces.yellow().variants[0]
        grid[:3, 4:6] += pieces.green().variants[3]
        grid[:3, -5:-2] += pieces.blue().variants[2]
        grid[1:4,2:5] += pieces.purple().variants[3]
        available_pieces = [
            pieces.red(),
            pieces.pink(),
            pieces.light_green(),
            pieces.dark_green(),
            pieces.dark_blue(),
            pieces.orange(),
            pieces.light_blue(),
            pieces.dark_red()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num ==32:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.light_green().variants[0]
        grid[:2, 2:6] += pieces.yellow().variants[4]
        grid[1:3, 4:7] += pieces.dark_red().variants[3]
        grid[:2, -5:-3] += pieces.light_blue().variants[3]
        available_pieces = [
            pieces.red(),
            pieces.pink(),
            pieces.green(),
            pieces.dark_green(),
            pieces.dark_blue(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 33:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.light_green().variants[6]
        grid[:3, 3:5] += pieces.dark_red().variants[0]
        grid[2:4, 5:8] += pieces.dark_blue().variants[4]
        available_pieces = [
            pieces.red(),
            pieces.pink(),
            pieces.green(),
            pieces.dark_green(),
            pieces.light_blue(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 34:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.dark_blue().variants[4]
        grid[:2, 3:7] += pieces.red().variants[7]
        grid[1:4, 5:7] += pieces.light_green().variants[7]
        available_pieces = [
            pieces.dark_red(),
            pieces.pink(),
            pieces.green(),
            pieces.dark_green(),
            pieces.light_blue(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 35:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.light_green().variants[3]
        grid[:2, 2:5] += pieces.green().variants[0]
        grid[2:4, 4:7] += pieces.dark_blue().variants[4]
        available_pieces = [
            pieces.dark_red(),
            pieces.pink(),
            pieces.red(),
            pieces.dark_green(),
            pieces.light_blue(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 36:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :4] += pieces.pink().variants[7]
        grid[:2, 3:6] += pieces.dark_green().variants[3]
        grid[2:4, 2:5] += pieces.light_green().variants[2]
        available_pieces = [
            pieces.dark_red(),
            pieces.green(),
            pieces.red(),
            pieces.dark_blue(),
            pieces.light_blue(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 37:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.dark_blue().variants[6]
        grid[2:4, 2:6] += pieces.red().variants[5]
        available_pieces = [
            pieces.dark_red(),
            pieces.green(),
            pieces.pink(),
            pieces.light_green(),
            pieces.light_blue(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 38:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[2:4, 2:6] += pieces.yellow().variants[4]
        grid[:3, :2] += pieces.dark_blue().variants[1]
        available_pieces = [
            pieces.dark_red(),
            pieces.green(),
            pieces.pink(),
            pieces.light_green(),
            pieces.light_blue(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.red()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 39:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:2, :3] += pieces.dark_blue().variants[4]
        grid[2:4, 2:6] += pieces.red().variants[7]
        available_pieces = [
            pieces.dark_red(),
            pieces.green(),
            pieces.pink(),
            pieces.light_green(),
            pieces.light_blue(),
            pieces.dark_green(),
            pieces.orange(),
            pieces.blue(),
            pieces.purple(),
            pieces.yellow()
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 40:
        grid = np.zeros((n_rows, n_cols), dtype=np.uint8)
        grid[:3, :2] += pieces.light_green().variants[7]
        grid[2:4, 2:6] += pieces.yellow().variants[0]
        available_pieces = [
            pieces.purple(),
            pieces.dark_red(),
            pieces.pink(),
            pieces.red(),
            pieces.orange(),
            pieces.green(),
            pieces.dark_green(),
            pieces.light_blue(),
            pieces.dark_blue(),
            pieces.blue()
        ]
        
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

#grid = start_position(5)
#print(grid)
#pour montrer un exemple
#test=pieces.purple()
#grille = start_position(5)
#print(test.variants)