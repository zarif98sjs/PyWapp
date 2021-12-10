# **`PyWapp`**
 _**Automate sending messages and images for whatsapp**_

 ## **Clone Repository**

 ```bash
 git clone https://github.com/zarif98sjs/PyWapp
 ```

 ## **Feature**

- send text to users / groups
- send images to users / groups

 ## **Demo Code**

 ```py
import pywapp as pw

NAME = "YOUR NAME HERE" ## user name or group name 

MESSAGE = "Your message here ... " ## message 
pw.send_message(NAME,MESSAGE)

IMAGE_URL = "J:\\My Drive\\Zarif\\Work\\mail\\image042.png" ## path to image
pw.send_image(NAME,IMAGE_URL)
 ```