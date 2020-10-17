import io
import pygame
from gtts import gTTS

def speech(text):
    with io.BytesIO() as file:
        gTTS(text=text,lang='en').write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        i = 0
        while pygame.mixer.music.get_busy():
                continue
            
if __name__ == '__main__':
    for i in range(3):
        speech('Please check the code')        
