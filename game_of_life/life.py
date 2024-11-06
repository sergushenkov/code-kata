import os

TEMPLATE_OUT = """Generation {num}
{high} {width}
{grid}"""


class Life:
    grid = None
    gen_num = None
    high = None
    width = None

    def __init__(self, file_name="life_start"):
        this_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(this_file_path)
        os.chdir(current_dir)

        with open(file_name) as fd:
            self.gen_num = int(fd.readline().split()[1][:-1])
            self.high, self.width = map(int, fd.readline().split())
            self.grid = []
            for str_row in fd.readlines():
                self.grid.append([x for x in str_row.strip()])

    def show(self):
        grid = "\n".join(("".join(row) for row in self.grid))
        return TEMPLATE_OUT.format(
            num=self.gen_num, high=self.high, width=self.width, grid=grid
        )

    def turn(self):
        new_grid = []
        for y in range(self.high):
            new_row = []
            for x in range(self.width):
                living_cnt = self.count_living_nearby(y, x)
                if self.grid[y][x] == "." and living_cnt == 3:
                    new_row.append("*")
                    continue
                if self.grid[y][x] == "*" and living_cnt in {2, 3}:
                    new_row.append("*")
                    continue
                if self.grid[y][x] == "." and living_cnt != 3:
                    new_row.append(".")
                    continue
                if self.grid[y][x] == "*" and living_cnt < 2:
                    new_row.append(".")
                    continue
                if self.grid[y][x] == "*" and living_cnt > 3:
                    new_row.append(".")
                    continue
            new_grid.append(new_row)
        self.grid = new_grid
        self.gen_num += 1

    def count_living_nearby(self, y, x):
        delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        cnt = 0
        for dy, dx in delta:
            if (
                0 <= y + dy < self.high
                and 0 <= x + dx < self.width
                and self.grid[y + dy][x + dx] == "*"
            ):
                cnt += +1
        return cnt


if __name__ == "__main__":
    life = Life()
    while True:
        print(life.show())
        life.turn()
        input()
