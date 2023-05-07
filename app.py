from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

import cohere
co = cohere.Client('avqgNUNwZIDVuC3Pmi7nffUlXaibIJoRpr5WQKja')




app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/api/data/<string:input_string>', methods=['GET'])

def answer_question(input_string):
    inputs = input_string.split("_")
    userQuestion = inputs[0]
    userGrade = inputs[1]
    tutor_prompt = "Write a detailed solution in the words of a tutor, to the question: " + userQuestion + ", and cater your response to a student in" + userGrade
    
    response = co.generate(
    model='command-nightly',
    prompt= tutor_prompt,
    max_tokens=300,
    temperature=0.1,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return('{}'.format(response.generations[0].text))


@app.route('/api/sayhi/<string:input_string>', methods=['GET'])

def say_hi(input_string):
    response = co.generate(
    model='command-xlarge-nightly',
    prompt= "Say hi to" + input_string + " and briefly introduce yourself as an online AI tutor ",
    max_tokens=300,
    temperature=0.1,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return('{}'.format(response.generations[0].text))

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)



    