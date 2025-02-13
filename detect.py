import tensorflow as tf
from utils.preprocessing import preprocess_image
import cv2

def detect_deepfake(image_path):
    # Load the trained model
    model = tf.keras.models.load_model('models/pretrained_model.h5')
    
    # Preprocess the image
    image = preprocess_image(image_path)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    
    # Predict
    prediction = model.predict(image)
    if prediction[0] > 0.5:
        return "Fake"
    else:
        return "Real"

if __name__ == '__main__':
    image_path = 'data/sample_images/test_image.jpg'  # Replace with your test image path
    result = detect_deepfake(image_path)
    print(f"The image is classified as: {result}")