import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    user_input = { "raw_document": { "text": text_to_analyse } }
 
    response = requests.post(url, json = user_input, headers=header)
    formatted_response = json.loads(response.text)

    emotions_dictionary = {}

    # Emotions required to be in the returned dictionary
    emotions = ["anger", "disgust", "fear", "joy", "sadness"]

    # Used to track which emotion has the highest value
    dominant_emotion = ""

    for emotion in emotions:

        # Finds the value of the emotion and stores it in a variable
        emotion_value = formatted_response["emotionPredictions"][0]["emotion"][emotion]

        # Adds emotion and its value to the dictionary
        emotions_dictionary[emotion] = emotion_value

        # Checks if the dominant emotion is empty or if its value is less than the current emotion's value
        if dominant_emotion == "" or emotions_dictionary[dominant_emotion] < emotion_value:
            dominant_emotion = emotion

    # Adds another pair to the dictionary to indicate the dominant emotion
    emotions_dictionary["dominant_emotion"] = dominant_emotion

    return emotions_dictionary

