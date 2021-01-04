from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL.Image
import os

class Model:

    def __init__(self):
        self.model = LinearSVC()

    
    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:,:,0]
            img = img.reshape(16950)
            img_list = np.append(img_list,[img])
            class_list = np.append(class_list, 1)
        
        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')[:,:,0]
            img = img.reshape(16950)
            img_list = np.append(img_list,[img])
            class_list = np.append(class_list, 2)

        img_list = img_list.reshape(counters[0] -1 + counters[1] - 1, 16950)
        self.model.fit(img_list, class_list)
        print('Model successfuly trained')

    def predict(self,frame):

        HERE = os.path.dirname(os.path.abspath(__file__))
        
        frame = frame[1]
        cv.imwrite('predict.jpg', cv.cvtColor(frame,cv.COLOR_RGB2GRAY))
        img = PIL.Image.open('predict.jpg')
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)
        img.save('predict.jpg')

        image_path = os.path.join(HERE, 'predict.jpg')
        img = cv.imread(image_path)[:,:,0]
        img = img.reshape(16950)
        prediction = self.model.predict([img])
        return prediction[0]
