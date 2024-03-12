import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
import numpy as np


def load_base_model(input_shape):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    
    # Freeze all layers in the base model
    for layer in base_model.layers:
        layer.trainable = False
        
    return base_model


def create_final_model(base_model, layer_name='block5_conv3'):
    last_but_one_layer = base_model.get_layer(layer_name).output
    gap_layer = tf.keras.layers.GlobalAveragePooling2D()(last_but_one_layer)
    
    model = Model(inputs=base_model.input, outputs=gap_layer)
    return model


def extract_features(model, directory, target_size=(150, 150), batch_size=32):
    datagen = ImageDataGenerator(rescale=1./255)
    generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode=None,
        shuffle=False
    )
    
    features = model.predict(generator, steps=np.ceil(generator.samples / generator.batch_size))
    labels = generator.classes
    
    return features, labels


def save_features_labels(features, labels, features_file='extracted_features.npy', labels_file='labels.npy'):
    np.save(features_file, features)
    np.save(labels_file, labels)


def load_saved_features(features_file='extracted_features.npy', labels_file='labels.npy'):
    loaded_features = np.load(features_file)
    loaded_labels = np.load(labels_file)
    
    return loaded_features, loaded_labels

if __name__ == "__main__":
    # Define input parameters
    input_shape = (150, 150, 3)
    data_directory = "D:\SEM-4\PROJECTS\ML\Archive"
    
    # Load base model
    base_model = load_base_model(input_shape)
    
    # Create final model
    final_model = create_final_model(base_model)
    
    # Extract features and labels
    extracted_features, extracted_labels = extract_features(final_model, data_directory)
    
    # Save extracted features and labels
    save_features_labels(extracted_features, extracted_labels)
    
    # Load saved features and labels
    loaded_features, loaded_labels = load_saved_features()
    
    # Print success message or any other desired output
    print("Features and labels extracted, saved, and loaded successfully!")

