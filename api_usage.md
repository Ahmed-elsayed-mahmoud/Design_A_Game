# API Documentation

The API contains the following endpoints:

#### `create_user`
- Path: `'user'`
- Method: `POST`
- Parameters: `user_name`, `email` (optional)
- Returns: Message confirming the creation of new `User`
- Description: Creates a user from a given username and email (optional) - only one account allowed per email and no duplicate usernames allowed

####`new_game`
- Path: `'game'`
- Method: `POST`
- Parameters: `user_name`
- Returns: Message confirming creation of new `Game`
- Description: Creates a new game for the user with the supplied username. Username must exist - will raise `NotFoundException` if not. Also adds a task to a task queue to update the average moves remaining for active games.

#### `get_game`
- Path: `'game/{urlsafe_game_key}'`
- Method: `GET`
- Parameters: `urlsafe_game_key`
- Returns: Message confirming that game was found and prompting user to guess a letter.
- Description: Returns a game form message for the game with the supplied urlsafe key

#### `guess_letter`
- Path: `'game/{urlsafe_game_key}/letter'`
- Method: `PUT`
- Parameters: `urlsafe_game_key`, `guess`
- Returns: Message stating whether the guessed letter is in the word or not.
- Description: Allows the user to guess a letter in the game with the suppled urlsafe key - only one letter may be guessed at a time from this endpoint. If the guess ends the game (either by completing the word or running out of guesses), the game is terminated and a score is added. Users cannot guess the same letter twice.

#### `guess_word`
- Path: `'game/{urlsafe_game_key}/word'`
- Method: `PUT`
- Parameters: `urlsafe_game_key`, `guess`
- Returns: Message stating whether the guessed word is correct.
- Description: Allows the user to guess the entire name in the game with the supplied urlsafe key - a penalty is assessed for incorrect guesses. If the guess ends the game, the game is terminated and a score is added. Users cannot guess the same word twice.

#### `get_scores`
- Path: `'scores'`
- Method: `GET`
- Parameters: none
- Returns: Messages stating the scores of all completed games in the database
- Description: Returns all scores for all completed games

#### `get_user_scores`
- Path: `'scores/user/{user_name}'`
- Method: `GET`
- Parameters: `user_name`, `email` (optional)
- Returns: Messages stating the scores of all completed games in the database tied to the given username
- Description: Returns all scores for all of the user's completed games

####`get_average_attempts`
- Path: `'games/average_attempts'`
- Method: `GET`
- Parameters: none
- Returns: Message stating the average number of attempts remaining across all active games
- Description: Returns the average number of attempts remaining

#### `get_user_games`
- Path: `'games/user/{user_name}'`
- Method: `GET`
- Parameters: `user_name`
- Returns: Messages reporting the state of all games tied to the given username
- Description: Returns a series of game form messages for all games tied to the given user

####`cancel_game`
- Path: `'game/{urlsafe_game_key}/cancel'`
- Method: `DELETE`
- Parameters: `urlsafe_game_key`
- Returns: Message confirming cancellation of the game
- Description: Cancels and deletes a game from the database

#### `get_high_scores`
- Path: `'high_scores'`
- Method: `GET`
- Parameters: `number_of_results` (optional)
- Returns: Highest scores up to `number_of_results`
- Description: Returns the n highest score where n is given as `number_of_results` - if `number_of_results` is not given, it's default value is 5

#### `get_user_rankings`
- Path: `'user_rankings'`
- Method: `GET`
- Parameters: none
- Returns: All users ranked by their total score across all games
- Description: Returns all of the registered users ranked by their total completed game score

####`get_game_history`
- Path: `'game/{urlsafe_game_key}/history'`
- Method: `GET`
- Parameters: `urlsafe_game_key`
- Returns: Messages containing all moves and results in the given game
- Description: Returns a history of all the moves made in a game along with their results

Also contained in this project is a cron job to send an hourly email to all users with an unfinished game in the Datastore.
