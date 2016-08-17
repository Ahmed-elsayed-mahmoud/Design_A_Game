# Design A Game (Hangman)

A scalable game(hangman) architected as a Web Service API using Google App Engine backed by Google Datastore.

This project provides an endpoints API for a Hangman game, though in theory this project could be easily adapted to work on any set of words. 

## Project Overview

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, within a certain number of guesses.

This implementation is a one player game. The word is provided by the app and player has to guess char in every step, if user is unable to guess the word in 6 steps player looses.

For more information on game, check wikipedia page [here](https://en.wikipedia.org/wiki/Hangman_%28game%29)


## Game Rules

Once a user has created a game, their word will be assigned - they will know how many letters are in the Pokemon's name but nothing more. At any point, the user can choose to guess a single letter in the name or the entire name at once. The user gets 6 "attempts" or "strikes" throughout the game. Incorrect guesses decrease the "attempts" counter - correct guesses do not. An incorrect name guess also increases the "penalty" (see Score Keeping below). If the counter hits 0, the game is over and the user gets a score of 0.0. Alternatively, if the user correctly guesses the name or final letter(s) then the game is over their score is calculated according to the algorithm in the following section.

## Score Keeping

To maximize score it is always advisable to guess the entire name once it is known. A score is defined to be a single decimal floating point number calculated based on the number of blanks remaining when the user guessed the name, relative to the length of the name, minus any penalties. In short, we take (((blanks remaining / length of word) * 10) - penalty) rounded to one decimal place where penalty is the number of inccorect name guesses.

The maximum score is 10.0 and the minimum score is 1.0. If the calculation gives a score less than 1.0, it is ignored and the score is assessed to be 1.0.

## Files Included

`main.py`: Contains handlers that are called by taskqueue and cronjobs
`game.py`: Contains all of the APIs and game logic
`models.py`: Contains all Datastore models and ProtoRPC messages for the game
`utils.py`: Contains utility functions for retrieving Pokemon names and getting an ndb.Model by urlsafe key
`app.yaml`: Contains app configuration
`cron.yaml`: Contains cronjob configuration for reminding users every 24 hours if they have an unfinished game


## How to access APIs

Read full API usage [here](api_usage.md)  


## Design Document

The design document is [here](design.txt)
