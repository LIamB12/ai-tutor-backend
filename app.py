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
    tutor_prompt = "As a " + userGrade + " tutor, please help me solve the following homework question: " + userQuestion + '''

    To solve this question, we can follow these steps:

    1. Analyze the given problem and identify the key information.
    2. Break down the problem into smaller steps or sub-questions.
    3. Apply the relevant concepts or formulas to solve each step.
    4. Show all the calculations and provide clear explanations along the way.
    5. Double-check the solution for accuracy and make sure it aligns with the original problem.

    Based on the given homework question, let's work through the solution together:

    [Provide guidance, step-by-step explanations, and calculations based on the specific homework question]

    Please let me know if you have any questions or need further clarification. I'm here to help you understand and solve the problem effectively.'''
    
    response = co.generate(
    model='command-xlarge-nightly',
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



    