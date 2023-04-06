# import the AudioCaptcha module from captcha.audio

from captcha.audio import AudioCaptcha

#Create an instance of AudioCaptcha().
audio = AudioCaptcha()

#provide string of numbers to create its audio CAPTCHA
captcha_text = '56579788' #text for captcha

#create the AUDIO CAPTCHA
audio_captcha = audio.generate(captcha_text)  

audio.write(captcha_text,'E:\Ritik Coder\Python\intresting stuff in python\Audio_captcha.wav') #specify file path