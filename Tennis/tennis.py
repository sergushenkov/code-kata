class Game():
    scores = {
        0: 'love',
        1: '15',
        2: '30',
        3: '40'
    }

    def __init__(self):
        self.pitcher = 0
        self.points = [0, 0]
    
    def set_point(self, is_pitcher_win):
        if is_pitcher_win not in (0, 1):
            raise Exception('ошибка ввода, должен быть 0 или 1')
        if is_pitcher_win:
            self.points[self.pitcher] += 1
            self.pitcher = (self.pitcher + 1) % 2
            return
        self.pitcher = (self.pitcher + 1) % 2
        self.points[self.pitcher] += 1

    def get_score(self):
        score_1, score_2 = self.points
        if max(score_1, score_2) >= 3 and abs(score_1 - score_2) >= 2:
            winner = 1 if score_1 > score_2 else 2
            return f'выиграл Игрок {winner}'
        if min(score_1, score_2) < 3:
            prev_pitcher = (self.pitcher + 1) % 2
            return f' счет: {Game.scores[self.points[prev_pitcher]]} - {Game.scores[self.points[self.pitcher]]}'
        if max(score_1, score_2) >= 3 and score_1 == score_2:
            return 'deuce'
        winner = 1 if score_1 > score_2 else 2
        return f'advantage у Игрока {winner}'
    
if __name__ == '__main__':
    game = Game()
    answer = ''
    while 'выиграл' not in answer:
        is_pitcher_win = int(input())
        game.set_point(is_pitcher_win)
        answer = game.get_score()
        print(answer)
    print('game over')
        
