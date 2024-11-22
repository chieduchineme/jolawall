from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import numpy as np
from .classify_target_requests import extract_labels, extract_features2

def preprocess_features_and_labels(train_requests):
    """
    Prepares the feature matrix X and encodes the labels from feature_df.
    
    Args:
        feature_df (pd.DataFrame): DataFrame containing features and labels.

    Returns:
        X (np.ndarray): Feature matrix.
        encoded_labels (np.ndarray): Encoded labels for training.
        label_encoder (LabelEncoder): The label encoder used to transform labels.
    """
    labels = extract_labels(train_requests)

    feature_df = extract_features2(train_requests)
    # Extract features
    X = feature_df[labels].values
    
    # Extract labels as a single string combining key details
    labels = labels.apply(lambda row: f"{row['class']}-{row['category']}-{row['descriptionOfClass']}", axis=1).values

    # Encode labels
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)
    num_classes = len(label_encoder.classes_)  # Get number of unique classes dynamically

    # Convert labels to one-hot encoding
    encoded_labels_one_hot = to_categorical(encoded_labels, num_classes=num_classes)  # Using the dynamic num_classes

    return X, encoded_labels_one_hot, label_encoder
