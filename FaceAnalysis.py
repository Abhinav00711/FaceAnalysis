import cv2
import gradio as gr
from deepface import DeepFace

def analyze_face(image):
    # Perform face analysis
    r = DeepFace.analyze(image, enforce_detection=False)
    
    result = r[0]
    # Get face details
    emotion = result['dominant_emotion']
    age = result['age']
    gender = result['dominant_gender']
    race = result['dominant_race']
      
    # Generate output text
    message = f"Emotion: {emotion}\nAge: {age}\nGender: {gender}\nRace: {race}"
    
    return message

# Define the input and output interface
iface = gr.Interface(
    fn=analyze_face,
    inputs="image",
    outputs="text",
    title="Face Analysis",
    description="Analyzes a person's face and displays the results.",
    capture_session=True,
    allow_flagging=False,
    layout="vertical",
)

# Launch the interface
iface.launch()