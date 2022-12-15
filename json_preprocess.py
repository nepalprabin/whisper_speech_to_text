## Preprocessing json transcribed file

import json

path = 'Stanford_Speech_to_Text_Dump/Stanford CS224N - NLP w⧸ DL ｜ Winter 2021 ｜ Lecture 4 - Syntactic Structure and Dependency Parsing [PSGIodTN3KE].json'

f = open(path)
res = json.load(f)

audio_segments = res['segments']
# print(audio_segments)
for i in range(len(audio_segments)):
    start_audio = audio_segments[i]['start']
    end_audio = audio_segments[i]['end']
    transcribed_text = audio_segments[i]['text']
    print(start_audio, end_audio, transcribed_text)