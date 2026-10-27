import json
import os
import random

def get_random_text_verse():
  # Load JSON
  file_path = os.path.join(os.path.dirname(__file__), "configuration/versete_text.json")
  with open(file_path, "r", encoding="utf-8") as f:
    versete = json.load(f)

  # Choose a random element
  return random.choice(versete)

def get_random_photo_verse():
  # Load JSON
    file_path = os.path.join(os.path.dirname(__file__), "configuration/versete_imagini.json")
    with open(file_path, "r", encoding="utf-8") as f:
      versete = json.load(f)
  
    # Choose a random element
    return random.choice(versete)