GENERATION_PATTERN = """Generation {turn}:
{height} {width}
{grid}"""


class Life:

    def __init__(self, file="life_start.txt"):
        with open(file) as fd:
            self.turn = int(fd.readline().strip(":\n").split(" ")[1])
            self.height, self.width = map(int, fd.readline().strip().split())
            self.grid = []
            for _ in range(self.height):
                row = []
                for ch in fd.readline().strip():
                    x = 0 if ch == "." else 1
                    row.append(x)
                self.grid.append(row)

    def check_neighbor(self, coordinates):
        x, y = coordinates
        return (0 <= x < self.height) and (0 <= y < self.width)

    def show_generation(self):
        visual_grid = "\n".join(
            ["".join(("*" if x else "." for x in row)) for row in self.grid]
        )
        rez = GENERATION_PATTERN.format(
            turn=self.turn, width=self.width, height=self.height, grid=visual_grid
        )
        return rez

    def count_alive_neighbors(self, x, y):
        delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        neighbors = ((x + dx, y + dy) for dx, dy in delta)
        alive = 0
        neighbors = list(filter(self.check_neighbor, neighbors))
        for xx, yy in neighbors:
            if self.grid[xx][yy]:
                alive += 1
        return alive

    def next_generation(self):
        next_grid = [[0 for __ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                cell = self.grid[x][y]
                if cell and self.count_alive_neighbors(x, y) in (2, 3):
                    next_grid[x][y] = 1
                    continue
                if not cell and self.count_alive_neighbors(x, y) == 3:
                    next_grid[x][y] = 1
        self.grid = next_grid
        self.turn += 1


if __name__ == "__main__":
    life = Life()
    while 1:
        print(life.show_generation())
        input()
        life.next_generation()
