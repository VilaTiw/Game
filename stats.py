class Stats():

    def init(self):
        """ініціалізація статистики"""
        self.reset_stats()
        self.run_game = True

        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика, що змінюється під час гри"""
        self.guns_left = 2
        self.score = 0