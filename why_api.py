import falcon
import simplejson as json

from matlabwhy import MatlabWhy

class WhyResource(object):
	def __init__(self):
		self.matlab = MatlabWhy()

	def on_get(self, request, response):
		response.status = falcon.HTTP_200
		response.body = json.dumps("I am a mighty developer and Slack is my bitch!").encode('utf-8')

	def on_post(self, request, response): 
		sentence = self.matlab.construct_sentence()
		response.status = falcon.HTTP_200
		body = {"response_type": "in_channel", "text": sentence}
		response.body = json.dumps(body).encode('utf-8')

"""instantiate API"""
api = application = falcon.API()

"""instantiate resource and configure URL"""
why = WhyResource()
api.add_route('/why', why)