from io import BytesIO
from PIL import Image
import numpy as np
from keras.utils import load_img, img_to_array
from keras.models import load_model
import tensorflow as tf
from keras.applications.vgg16 import preprocess_input
from mtcnn import MTCNN


detector = MTCNN()
# Define paths
# image_path = 'C:/Users/dell/Desktop/MS_DS/M2/AppAutomaique/Projet/me.jpg'
image_hash  = {}
image_hash['Akram'] = {
    'hash' : np.array([0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0]),
    'fname' : 'Akram EL MOUDEN',
    'Age' : '22',
    'Adresse' : 'Tilila, AGADIR',
    'Job' : 'Student'
}
image_hash['Josef'] = {
    'hash' : np.array([1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0]),
    'fname' : 'Josef ABOKAYO',
    'Age' : '29',
    'Adresse' : 'Texas, USA',
    'Job' : 'ML Engeneer'
}
image_hash['David'] = {
    'hash' : np.array([1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0]),
    'name' : 'David CHARELETON',
    'Age' : '36',
    'Adresse' : 'NYC, USA',
    'Job' : 'Teacher'
}


def hamming_distance(a, b):
    return np.sum(a != b)




def load_keras_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return tf.keras.Model(inputs=model.input, outputs=model.get_layer('latent').output)

model_path = 'C:/Users/dell/Desktop/MS_DS/M2/AppAutomaique/Projet/final_weights.h5'
# Load the model
model = load_keras_model(model_path)
# Function to draw bounding box
def draw_box(image, result_list):
    y, x, width, height = result_list[0]['box']
    image_with_box = image.copy()
    image_with_box[x:x+height, y] = [255, 0, 0]        # left border
    image_with_box[x:x+height, y+width] = [255, 0, 0]  # right border
    image_with_box[x, y:y+width] = [255, 0, 0]         # top border
    image_with_box[x+height, y:y+width] = [255, 0, 0]  # bottom border
    return image_with_box, image[x:x+height, y:y+width]

# Function to draw bounding box
def draw_box(image, result_list):
    y, x, width, height = result_list[0]['box']
    image_with_box = image.copy()
    image_with_box[x:x+height, y] = [255, 0, 0]        # left border
    image_with_box[x:x+height, y+width] = [255, 0, 0]  # right border
    image_with_box[x, y:y+width] = [255, 0, 0]         # top border
    image_with_box[x+height, y:y+width] = [255, 0, 0]  # bottom border
    return image_with_box, image[x:x+height, y:y+width]
# Function to preprocess the image
'''def preprocess_image(image_path):
    detector = MTCNN()
    img = load_img(image_path, color_mode='rgb')
    img = img_to_array(img).astype('uint8')
    results = detector.detect_faces(img)
    if not results:
        raise ValueError("No face detected in the image")
    img, img_t = draw_box(img, results)
    img_t = tf.keras.preprocessing.image.array_to_img(img_t)
    img_t = img_t.resize((224, 224))
    img_t = img_to_array(img_t)
    img_t = np.expand_dims(img_t, axis=0)
    img_t = preprocess_input(img_t) # Remove 'version' argument
    return img_t
'''
def preprocess_image(img_bytes):
    global detector # = MTCNN()
    img = Image.open(BytesIO(img_bytes))
    if img.mode == 'RGBA':
        img = img.convert('RGB')  # Convert RGBA to RGB.convert('RGBA')
    #img = img.convert('RGB')  # Convert RGBA to RGB
    img = img_to_array(img).astype('uint8')
    results = detector.detect_faces(img)
    if not results:
        raise ValueError("No face detected in the image")
    img, img_t = draw_box(img, results)
    img_t = tf.keras.preprocessing.image.array_to_img(img_t)
    img_t = img_t.resize((224, 224))
    img_t = img_to_array(img_t)
    img_t = np.expand_dims(img_t, axis=0)
    img_t = preprocess_input(img_t)
    return img_t

#prediction
def predict(img_path):
    #model_path = 'C:/Users/dell/Desktop/MS_DS/M2/AppAutomaique/Projet/final_weights.h5'

    # Load the model
    #model = load_keras_model(model_path)
    global model 
    # Preprocess the image
    preprocessed_img = preprocess_image(img_path)

    # Make predictions
    predictions = model.predict(preprocessed_img)
    # Convert predictions to numpy array
    predictions_np = np.array(predictions[0])
    # Print the predictions
    #print(predictions_np)
    # Convert to binary means
    binary_means = np.where(predictions_np > 0.5, 1, 0)
    print(binary_means)
    return binary_means
def search_for_nearest_vect(img):
    generated_vector = predict(img)
    min_distance = float('inf')
    closest_key = None

    for key, value in image_hash.items():
        distance = hamming_distance(generated_vector, value['hash'])
        if distance < min_distance:
            min_distance = distance
            closest_key = key

    return closest_key


'''if __name__ == '__main__':
    l = [1,1,1,1,1]
    print(l)'''