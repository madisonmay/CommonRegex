from datetime import datetime

class NormalizedDate():
  pass

class NormalizedTime():

  def __init__(self, text):
    formats = ["%H:%M"]
    for format in formats:
      if datetime.strptime(text, format):
        print text


if __name__ == "__main__":


