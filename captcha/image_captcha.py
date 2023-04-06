from captcha.image import ImageCaptcha

#create an instance pass dimension of captcha image
image = ImageCaptcha(300,300)

#captcha
captcha_text = '45hsgd'

# create the CAPTCHA.
data = image.generate(captcha_text)

# save the generated image CAPTCHA.
image.write(captcha_text, f'./captcha/{captcha_text}.png')