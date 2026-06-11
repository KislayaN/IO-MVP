from google import genai
import os

# API key

API_KEY = ""

client = genai.Client(api_key=API_KEY)

try: 
    # list all available models
    models = client.models.list()
    
    print("Available models: \n")
    for model in models:
        if "generateContent" in model.supported_actions:
            print(model.name)
            
except Exception as e:
    print("Error: ", e)