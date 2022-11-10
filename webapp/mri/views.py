from django.shortcuts import render

from django.shortcuts import render
import keras
from PIL import Image
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.
media='media'
model = keras.models.load_model('../saved_models/trained.h5')

def makepredictions(path):
    #we open the image

    img=Image.open(path)

    #we resize the image for model

    img_d = img.resize((244,244))

    # we check if image is RGB or not

    if len(np.array(img_d).shape)<4:
        rgb_img =Image.new("RGB",img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img=img_d


    # here we convert the image into numpy array and reshape
    rgb_img=np.array(rgb_img,dtype=np.float64)
    rgb_img=rgb_img.reshape(1,244,244,3)

    #we make predictions here

    predictions =model.predict(rgb_img)
    a=int(np.argmax(predictions))
    if a==1:
        a="Result : Glioma Tumor"
    elif a==2:
        a="Result : Meningioma Tumor"
        
    elif a==3:
        a="Result : No Tumor"
    else:
        a="Result: Pictiuary Tumor"
    return a