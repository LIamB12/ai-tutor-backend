from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from cohere.responses.classify import Example


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
    temperature=0.25,
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


@app.route('/api/classify/<string:input_string>', methods=['GET'])
def classify(input_string):
    response = co.classify(
    model='large',
    inputs=[input_string],
    examples=[Example("What is your favorite color?", "0"), Example("Do you like pizza?", "0"), Example("What is your pet\'s name?", "0"), Example("What is your favorite TV show?", "0"), Example("Have you ever been to Disneyland?", "0"), Example("What is your favorite sports team?", "0"), Example("Do you play any musical instruments?", "0"), Example("What is your favorite video game?", "0"), Example("Have you read any books recently?", "0"), Example("What is your favorite holiday?", "0"), Example("What is your favorite movie?", "0"), Example("What is your dream travel destination?", "0"), Example("Do you enjoy cooking?", "0"), Example("What is your favorite hobby?", "0"), Example("What is your favorite genre of music?", "0"), Example("Have you ever climbed a mountain?", "0"), Example("What is your favorite social media platform?", "0"), Example("Do you prefer coffee or tea?", "0"), Example("What is your favorite season?", "0"), Example("Have you ever attended a live concert?", "0"), Example("What is the capital of France?", "1"), Example("Solve for x: 2x + 5 = 15", "1"), Example("Who wrote the novel \'Pride and Prejudice\'?", "1"), Example("What are the three states of matter?", "1"), Example("What is the chemical symbol for gold?", "1"), Example("Explain the process of photosynthesis.", "1"), Example("What is the quadratic formula?", "1"), Example("What is the meaning of the word \'ambivalent\'?", "1"), Example("Compare and contrast mitosis and meiosis.", "1"), Example("What is the significance of the theory of relativity?", "1"), Example("What is the Pythagorean theorem?", "1"), Example("Describe the process of cellular respiration.", "1"), Example("Who is considered the father of modern physics?", "1"), Example("What is the definition of a derivative?", "1"), Example("Explain the concept of supply and demand.", "1"), Example("What is the role of the Supreme Court?", "1"), Example("Discuss the impact of globalization on the economy.", "1"), Example("What are the major principles of ethics?", "1"), Example("Explain the concept of algorithm complexity.", "1"), Example("What is the significance of the Higgs boson discovery?", "1")])
    print(response.classifications[0].prediction)

    return(response.classifications[0].prediction)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)



    