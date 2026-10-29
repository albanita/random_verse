import json
import os
import random

def get_random_verse(source_configuration: str):
  # Load JSON
  file_path = os.path.join(os.path.dirname(__file__), source_configuration)
  with open(file_path, "r", encoding="utf-8") as f:
    versete = json.load(f)

  # Choose a random element
  return random.choice(versete)
