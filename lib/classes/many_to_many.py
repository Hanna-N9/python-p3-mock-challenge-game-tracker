class Game:
    all = []
    
    def __init__(self, title):
        self.title = title
        Game.all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and len(title) > 0:
            self._title = title
    
    #Object Relationship Methods and Properties
    #Returns a list of all results for that game, Results must be of type Result
    def results(self):
        return [result for result in Result.all if result.game is self]

    #Object Relationship Methods and Properties
    #Returns a unique list of all players that played a particular game, Players must be of type Player
    def players(self):
        return list({result.player for result in self.results()})

    #Object Relationship Methods and Properties
    #Receives a player object as argument, Returns the average of all the player's scores for a particular game instance, Reminder: you can calculate the average by adding up all the results' scores of the player specified and dividing by the number of those results
    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores)





class Player:
    all = []
    
    def __init__(self, username):
        self.username = username
        Player.all.append(self)
        
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    #Object Relationship Methods and Properties
    #Returns a list of all results for that player, Results must be of type Result
    def results(self):
        return [result for result in Result.all if result.player is self]

    #Object Relationship Methods and Properties
    #Returns a unique list of all games played by a particular player, Games must be of type Game
    def games_played(self):
        return list({result.game for result in self.results()})
   
    #Aggregate and Association Methods
    #Receives a game object as argument, Returns True if the player has played the game object provided, Returns False otherwise
    def played_game(self, game):
        return game in self.games_played()

    #Aggregate and Association Methods
    #Receives a game object as argument, Returns the number of times the player has played the game instance provided, Returns 0 if the player never played the game provided 
    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])






class Result:
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

             
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
     
    #Object Relationship Methods and Properties       
    #Returns the player object for that result, Must be of type Player
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
    
    #Object Relationship Methods and Properties       
    #Returns the game object for that result, Must be of type Game
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game