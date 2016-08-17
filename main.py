import webapp2
from google.appengine.api import mail, app_identity
from game import PokemonHangmanAPI

from models import User, Game


class SendReminderEmail(webapp2.RequestHandler):
	def get(self):
		"""Send a reminder email to each User with an unfinished game.
		Called every hour using a cron job"""
		app_id = app_identity.get_application_id()
		users = User.query(User.email != None)
		for user in users:
			user_games = Game.query(ancestor=user.key)
			unfinished = user_games.filter(Game.game_over == False).get()
			if unfinished:
				subject = 'This is a reminder!'
				body = 'Hello {}, you have an unfinished game of Pokemon Hangman!'.format(user.name)
				mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
							   user.email,
							   subject,
							   body)


class UpdateAverageMovesRemaining(webapp2.RequestHandler):
	def post(self):
		"""Update game listing announcement in memcache."""
		PokemonHangmanAPI._cache_average_attempts()
		self.response.set_status(204)


app = webapp2.WSGIApplication([
	('/crons/send_reminder', SendReminderEmail),
	('/tasks/cache_average_attempts', UpdateAverageMovesRemaining),
], debug=True)
