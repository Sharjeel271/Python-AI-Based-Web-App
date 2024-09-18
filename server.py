'''The application is deployed using Flask. This file contains all the routes'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detectior")

@app.route("/emotionDetector")
def detector():
    '''Takes the input from the user and send it to the API via the emotion_detector function.
    Afterwards, it shows the emotion values of the input on the page'''
    user_input_text = request.args.get("textToAnalyze")
    response = emotion_detector(user_input_text)

    anger_val = response["anger"]
    disgust_val = response["disgust"]
    fear_val = response["fear"]
    joy_val = response["joy"]
    sadness_val = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger_val}, 'disgust': {disgust_val}, 'fear': {fear_val}, 'joy': {joy_val} and 'sadness': {sadness_val}. The dominant emotiom is {dominant_emotion}"

@app.route("/")
def render_index_page():
    ''' Renders the index page to the user'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
