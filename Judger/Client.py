import json
from server.Server import JudgeServer
from flask import Flask, request, Response
from server.Validate import Validate
import gevent.monkey
import psutil
from flask_cors import *

gevent.monkey.patch_all()

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/judge',methods=['POST'])
def get_judge_result():
	try:
		data = json.loads(request.get_data().decode('utf-8'))
		validate = Validate(data)
		if(not validate.validateAgrs()):
				error = {
					'error_message':'args are not legal',
					'result':'SE'
				}
				return Response(json.dumps(error), mimetype='application/json')
	except Exception as e:
		error = {
			'error_message':'args cannot be null',
			'result':'SE'
		}
		return Response(json.dumps(error), mimetype='application/json')
	try:
		for item in data['test_cases']:
			index = data['test_cases'].index(item)
			if item['stdin'] == None or len(item['stdin']) == 0:
				data['test_cases'][index]['stdin'] = ''
		sever = JudgeServer(data)
		result = sever.judge()
	except Exception as e:
		error = {
			'result':'SE',
			'error_message':'Client Error: '+str(e)
		}
		return Response(json.dumps(error), mimetype='application/json')
	else:
		return Response(json.dumps(result), mimetype='application/json')

@app.route('/status', methods=['GET'])
def get_status():
	status ={
 		    'memory_percent':str(psutil.virtual_memory().percent)+'%',
            'available_memeory':round(psutil.virtual_memory().available/1024**3,2)
 		}
	return Response(json.dumps(status), mimetype='application/json')

#gunicorn -k gevent -c gunicorn.conf Client:app
if __name__ == '__main__':
	app.run(debug=True)
