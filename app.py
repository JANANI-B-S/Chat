
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Initialize ChatBot
chatbot = ChatBot('ChatBot')

# Train ChatBot with English language corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_bot_response():
    user_text = request.args.get('msg')
    if user_text:
        response = chatbot.get_response(user_text)
        return jsonify({"response": str(response)})
    else:
        return jsonify({"response": "No message provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
