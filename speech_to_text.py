# whisper --language en --model large -o {out_dir} -- {mp3_file}
import os
import json
import glob

import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio_path = '/content/drive/MyDrive/Stanford_CS224N_Winter_2021_Lecture_5-Recurrent_Neural_networks_(RNNs).mp3'
audio = whisper.load_audio(audio_path)
result = model.transcribe(audio)

stanford_nlp_audio_path = 'Stanford_NLP_Audios/*'
audios = glob.glob(stanford_nlp_audio_path)

for audio in audios:
  filename = os.path.basename(audio).split('.')[0]
  audio = whisper.load_audio(audio)
  result = model.transcribe(audio)
  with open(f"Stanford_Speech_to_Text_Dump/{filename}.json", "w") as outfile:
    json.dump(result, outfile)