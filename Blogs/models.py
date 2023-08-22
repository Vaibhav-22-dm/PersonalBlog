from django.db import models
from django.contrib.auth.models import User
from gtts.tts import gTTS
from tinymce import models as tinymce_models
import re
import uuid 
import requests

# Create your models here.
class Blog(models.Model):
    title = models.TextField(null=True, blank=True)
    content = tinymce_models.HTMLField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    audio = models.FileField(upload_to='media/audio/', null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        clean = re.compile('<.*?>')
        if(self.audio is None or self.audio == ""):
            audio = gTTS(text=re.sub(clean, '', self.content), lang='en') 
            file_name = str(uuid.uuid1()) + ".mp3"
            audio.save("media/audio/" + file_name)
            self.audio = "audio/" + file_name
        if(self.summary is None or self.summary == ""):
            text=re.sub(clean, '', self.content)     
            url = "https://api.meaningcloud.com/summarization-1.0"
            payload={'key':'f225530c7bae7394a6b88f37c086b471','txt':text,'sentences':'5'}
            try:
                response = requests.post(url, data=payload)
                self.summary = response.json()['summary']
            except Exception as e:
                print(e)
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
    reply = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.author.username + "'s comment on Blog - " + str(self.blog.id)
