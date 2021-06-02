# from keras.models import load_model
# import h5py
# expression = load_model('./model/expression_model.hdf5')


def detect_emotions(self, img: np.ndarray, face_rectangles: NumpyRects = None) -> list:
    """
    Detects bounding boxes from the specified image with ranking of emotions.
    :param img: image to process (BGR or gray)
    :return: list containing all the bounding boxes detected with their emotions.
    """
    if img is None or not hasattr(img, "shape"):
        raise InvalidImage("Image not valid.")

    emotion_labels = self._get_labels()

    if not face_rectangles:
        face_rectangles = self.find_faces(img, bgr=True)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    emotions = []
    for face_coordinates in face_rectangles:
        face_coordinates = self.tosquare(face_coordinates)
        x1, x2, y1, y2 = self.__apply_offsets(face_coordinates)

        if y1 < 0 or x1 < 0:
            gray_img = self.pad(gray_img)
            x1 += 40
            x2 += 40
            y1 += 40
            y2 += 40
            x1 = np.clip(x1, a_min=0, a_max=None)
            y1 = np.clip(y1, a_min=0, a_max=None)

        gray_face = gray_img[y1:y2, x1:x2]

        try:
            gray_face = cv2.resize(gray_face, self.__emotion_target_size)
        except Exception as e:
            print("{} resize failed: {}".format(gray_face.shape, e))
            continue
        
        # Local Keras model
        gray_face = self.__preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)

        emotion_prediction = self.__emotion_classifier.predict(gray_face)[0]
        labelled_emotions = {
            emotion_labels[idx]: round(float(score), 2)
            for idx, score in enumerate(emotion_prediction)
        }

        emotions.append(
            dict(box=face_coordinates, emotions=labelled_emotions)
        )

    self.emotions = emotions

    return emotions
    
def top_emotion(self, img: np.ndarray):
    """Convenience wrapper for `detect_emotions` returning only top emotion for first face in frame.
    :param img: image to process
    :return: top emotion and score (for first face in frame)
    """
    emotions = self.detect_emotions(img=img)
    top_emotions = [
        max(e["emotions"], key=lambda key: e["emotions"][key]) for e in emotions
    ]

    # Take first face
    top_emotion = top_emotions[0]
    score = emotions[0]["emotions"][top_emotion]

    return top_emotion, score

from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"if __name__ == "__main__":        # on running python app.py

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    params = flask.request.json
    
    if (params != None):
        return params

app.run()                    # run the flask app
  