class Game:

    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "_title"):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    def results(self):
        results = Result.all
        return [result for result in results if result.game == self]

    def players(self):
        results = Result.all
        return list(set(result.player for result in results if result.game == self))


    def average_score(self, player):
        results = player.results()
        scores = [result.score for result in results]
        return sum(scores) / len(scores)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
        

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) > 1 and len(username) < 17:
            self._username = username
        else:
            raise ValueError("Username must be between 2 and 16 characters")

    def results(self):
        results = Result.all
        return [result for result in results if result.player == self]

    def games_played(self):
        results = Result.all
        return list(set(result.game for result in results if result.player == self))

    def played_game(self, game):
        results = Result.all
        for result in results:
            if result.player == self and result.game == game:
                return True
        return False

    def num_times_played(self, game):
        results = [result for result in Result.all if result.player == self and result.game == game]
        return len(results)

class Result:

    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and score in range(1, 5001) and not hasattr(self, "_score"):
            self._score = score
        else:
            raise ValueError("Score must be an integer between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise ValueError("Player must be an instance of Player class")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise ValueError("Game must be an instance of Game class")
