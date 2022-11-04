from Neuraline.ObjectiveAI.chatbot import Chatbot
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/chatbot/*": {"origins": "*"}})
chatbot = Chatbot()
chatbot.loadModel("model")
@app.route("/chatbot/insertUser", methods=["POST"])
def insertUser():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		full_name = ""
		user_name = ""
		password = ""
		gender = ""
		administrator = 0
		activated = 1
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: full_name = str(data["full_name"]).strip()
		except: pass
		try: user_name = str(data["user_name"]).strip()
		except: pass
		try: password = str(data["password"]).strip()
		except: pass
		try: gender = str(data["gender"]).strip()
		except: pass
		try: administrator = data["administrator"]
		except: pass
		if int(administrator) <= 0 or str(administrator).strip() == "": administrator = 0
		if type(administrator) == str: administrator = int(administrator)
		try: activated = data["activated"]
		except: pass
		if str(activated).strip() == "": activated = 1
		if type(activated) == str: activated = int(activated)
		chatbot.insertUser(id, full_name, user_name, password, gender, administrator, activated)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "full_name": "", "user_name": "", "password": "", "gender": "", "administrator": 0, "activated": 1}
@app.route("/chatbot/insertRegister", methods=["POST"])
def insertRegister():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		external_user_id = 0
		relationship_id = 0
		question = ""
		answer = ""
		activated = 1
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: relationship_id = data["relationship_id"]
		except: pass
		if int(relationship_id) <= 0 or str(relationship_id).strip() == "": relationship_id = 0
		if type(relationship_id) == str: relationship_id = int(relationship_id)	
		try: question = str(data["question"]).strip()
		except: pass
		try: answer = str(data["answer"]).strip()
		except: pass
		try: activated = data["activated"]
		except: pass
		if str(activated).strip() == "": activated = 1
		if type(activated) == str: activated = int(activated)	
		chatbot.insertRegister(id, external_user_id, relationship_id, question, answer, activated)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "external_user_id": 0, "relationship_id": 0, "question": "", "answer": "", "activated": 1}
@app.route("/chatbot/setDefaultAnswer", methods=["POST"])
def setDefaultAnswer():
	result = [False]
	try:
		data = request.get_json()
		external_user_id = 0
		answer = ""
		try: external_user_id = data["external_user_id"]
		except: pass
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: answer = str(data["answer"]).strip()
		except: pass
		chatbot.setDefaultAnswer(external_user_id, answer)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "answer": "?"}
@app.route("/chatbot/updateUser", methods=["POST"])
def updateUser():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		full_name = ""
		user_name = ""
		password = ""
		gender = ""
		administrator = 0
		activated = 1
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: full_name = str(data["full_name"]).strip()
		except: pass
		try: user_name = str(data["user_name"]).strip()
		except: pass
		try: password = str(data["password"]).strip()
		except: pass
		try: gender = str(data["gender"]).strip()
		except: pass
		try: administrator = data["administrator"]
		except: pass
		if int(administrator) <= 0 or str(administrator).strip() == "": administrator = 0
		if type(administrator) == str: administrator = int(administrator)
		try: activated = data["activated"]
		except: pass
		if str(activated).strip() == "": activated = 1
		if type(activated) == str: activated = int(activated)
		chatbot.updateUser(id, full_name, user_name, password, gender, administrator, activated)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "full_name": "", "user_name": "", "password": "", "gender": "", "administrator": 0, "activated": 1}
@app.route("/chatbot/updateRegister", methods=["POST"])
def updateRegister():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		external_user_id = 0
		relationship_id = 0
		question = ""
		answer = ""
		activated = 1
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: relationship_id = data["relationship_id"]
		except: pass
		if int(relationship_id) <= 0 or str(relationship_id).strip() == "": relationship_id = 0
		if type(relationship_id) == str: relationship_id = int(relationship_id)
		try: question = str(data["question"]).strip()
		except: pass
		try: answer = str(data["answer"]).strip()
		except: pass
		try: activated = data["activated"]
		except: pass
		if str(activated).strip() == "": activated = 1
		if type(activated) == str: activated = int(activated)		
		chatbot.updateRegister(id, external_user_id, relationship_id, question, answer, activated)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "external_user_id": 0, "relationship_id": 0, "question": "", "answer": "", "activated": 1}
@app.route("/chatbot/deleteUser", methods=["POST"])
def deleteUser():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		delete_data = True
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: delete_data = data["delete_data"]
		except: pass
		if delete_data == True or str(delete_data).lower().strip() == "true" or str(delete_data).strip() == "": delete_data = True
		else: delete_data = False
		chatbot.deleteUser(id, delete_data)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "delete_data": true}
@app.route("/chatbot/deleteRegister", methods=["POST"])
def deleteRegister():
	result = [False]
	try:
		data = request.get_json()
		id = 0
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		chatbot.deleteRegister(id)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0}
@app.route("/chatbot/deleteUseridCatches", methods=["POST"])
def deleteUseridCatches():
	result = [False]
	try:
		data = request.get_json()
		external_user_id = 0
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		chatbot.deleteUseridCatches(external_user_id)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0}
@app.route("/chatbot/deleteAllCatches", methods=["POST"])
def deleteAllCatches():
	result = [False]
	try:
		chatbot.deleteAllCatches()
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {}
@app.route("/chatbot/selectAllUsers", methods=["POST"])
def selectAllUsers():
	result = []
	try:
		data = request.get_json()
		order_by = ""
		decreasing = False
		only_activated = False
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectAllUsers(order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectAllRegisters", methods=["POST"])
def selectAllRegisters():
	result = []
	try:
		data = request.get_json()
		order_by = ""
		decreasing = False
		only_activated = False
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectAllRegisters(order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectAllCatches", methods=["POST"])
def selectAllCatches():
	result = []
	try:
		data = request.get_json()
		order_by = ""
		decreasing = False
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		result = chatbot.selectAllCatches(order_by, decreasing)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"order_by": "", "decreasing": false}
@app.route("/chatbot/selectIDUser", methods=["POST"])
def selectIDUser():
	result = []
	try:
		data = request.get_json()
		id = 0
		order_by = ""
		decreasing = False
		only_activated = False
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectIDUser(id, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectIDRegister", methods=["POST"])
def selectIDRegister():
	result = []
	try:
		data = request.get_json()
		id = 0
		order_by = ""
		decreasing = False
		only_activated = False
		try: id = data["id"]
		except: pass
		if int(id) <= 0 or str(id).strip() == "": id = 0
		if type(id) == str: id = int(id)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectIDRegister(id, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"id": 0, "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUseridCatches", methods=["POST"])
def selectUseridCatches():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		order_by = ""
		decreasing = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		result = chatbot.selectUseridCatches(external_user_id, order_by, decreasing)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "order_by": "", "decreasing": false}
@app.route("/chatbot/selectFullnameUser", methods=["POST"])
def selectFullnameUser():
	result = []
	try:
		data = request.get_json()
		full_name = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: full_name = data["full_name"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectFullnameUser(full_name, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"full_name": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUsernameUser", methods=["POST"])
def selectUsernameUser():
	result = []
	try:
		data = request.get_json()
		user_name = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: user_name = data["user_name"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUsernameUser(user_name, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"user_name": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectPasswordUser", methods=["POST"])
def selectPasswordUser():
	result = []
	try:
		data = request.get_json()
		password = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: password = data["password"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectPasswordUser(password, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"password": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUserLOGIN", methods=["POST"])
def selectUserLOGIN():
	result = []
	try:
		data = request.get_json()
		user_name = ""
		password = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: user_name = data["user_name"]
		except: pass
		try: password = data["password"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUserLOGIN(user_name, password, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"user_name": "", "password": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectGenderUser", methods=["POST"])
def selectGenderUser():
	result = []
	try:
		data = request.get_json()
		gender = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: gender = data["gender"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectGenderUser(gender, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"gender": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectAdministratorUser", methods=["POST"])
def selectAdministratorUser():
	result = []
	try:
		data = request.get_json()
		administrator = 0
		order_by = ""
		decreasing = False
		only_activated = False
		try: administrator = data["administrator"]
		except: pass
		if int(administrator) <= 0 or str(administrator).strip() == "": administrator = 0
		if type(administrator) == str: administrator = int(administrator)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectAdministratorUser(administrator, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"administrator": 0, "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectActivatedUser", methods=["POST"])
def selectActivatedUser():
	result = []
	try:
		data = request.get_json()
		activated = 1
		order_by = ""
		decreasing = False
		try: activated = data["activated"]
		except: pass
		if int(activated) <= 0: activated = 0
		if str(activated).strip() == "": activated = 1
		if type(activated) == str: activated = int(activated)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		result = chatbot.selectActivatedUser(activated, order_by, decreasing)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"activated": 1, "order_by": "", "decreasing": false}
@app.route("/chatbot/selectUseridRegister", methods=["POST"])
def selectUseridRegister():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		order_by = ""
		decreasing = False
		only_activated = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUseridRegister(external_user_id, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUseridRelationshipRegister", methods=["POST"])
def selectUseridRelationshipRegister():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		relationship_id = 0
		order_by = ""
		decreasing = False
		only_activated = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: relationship_id = data["relationship_id"]
		except: pass
		if int(relationship_id) <= 0 or str(relationship_id).strip() == "": relationship_id = 0
		if type(relationship_id) == str: relationship_id = int(relationship_id)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUseridRelationshipRegister(external_user_id, relationship_id, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "relationship_id": 0, "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUseridQuestionRegister", methods=["POST"])
def selectUseridQuestionRegister():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		question = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: question = data["question"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUseridQuestionRegister(external_user_id, question, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "question": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUseridAnswerRegister", methods=["POST"])
def selectUseridAnswerRegister():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		answer = ""
		order_by = ""
		decreasing = False
		only_activated = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: answer = data["answer"]
		except: pass
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		try: only_activated = data["only_activated"]
		except: pass
		if only_activated == True or str(only_activated).lower().strip() == "true": only_activated = True
		else: only_activated = False
		result = chatbot.selectUseridAnswerRegister(external_user_id, answer, order_by, decreasing, only_activated)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "answer": "", "order_by": "", "decreasing": false, "only_activated": false}
@app.route("/chatbot/selectUseridActivatedRegister", methods=["POST"])
def selectUseridActivatedRegister():
	result = []
	try:
		data = request.get_json()
		external_user_id = 0
		activated = 1
		order_by = ""
		decreasing = False
		try: external_user_id = data["external_user_id"]
		except: pass
		if int(external_user_id) <= 0 or str(external_user_id).strip() == "": external_user_id = 0
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		try: activated = data["activated"]
		except: pass
		if int(activated) <= 0: activated = 0
		else: activated = 1
		if type(activated) == str: activated = int(activated)
		try: order_by = str(data["order_by"]).lower().strip()
		except: pass
		try: decreasing = data["decreasing"]
		except: pass
		if decreasing == True or str(decreasing).lower().strip() == "true": decreasing = True
		else: decreasing = False
		result = chatbot.selectUseridActivatedRegister(external_user_id, activated, order_by, decreasing)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "activated": 1, "order_by": "", "decreasing": false}
@app.route("/chatbot/deleteUserData", methods=["POST"])
def deleteUserData():
	result = [False]
	try:
		data = request.get_json()
		external_user_id = 0
		try: external_user_id = data["external_user_id"]
		except: pass
		if type(external_user_id) == str: external_user_id = int(external_user_id)
		chatbot.deleteUserData(external_user_id)
		result = [True]
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0}
@app.route("/chatbot/conversation", methods=["POST"])
def conversation():
	result = []
	try:
		data = request.get_json()
		external_user_id = None
		question = ""
		abbreviations = None
		try:
			external_user_id = data["external_user_id"]
			if type(external_user_id) == str: external_user_id = int(external_user_id)
		except: pass
		try: question = str(data["question"]).strip()
		except: pass
		try: abbreviations = str(data["abbreviations"]).strip()
		except: pass
		result = chatbot.conversation(external_user_id, question, abbreviations)
		print(f"RESULT: {result}")
	finally: return jsonify(result)
# Format JSON: {"external_user_id": 0, "question": "", "abbreviations": ""}
if __name__ == "__main__":
	char = "#"*84
	title = "Neuraline Server API"
	algorithm = "Chatbot"
	print(char)
	print(title.center(84, " "))
	print(char)
	print(" * ROUTE: http://127.0.0.1:5000/chatbot")
	print(" * Algorithm: "+algorithm)
	app.run()
