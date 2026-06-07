import gtts
import pypdf
from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hi milka Naveena.How are you.', lang='en')
tts.write_to_fp(mp3_fp)
tts.save('hello.mp3')

