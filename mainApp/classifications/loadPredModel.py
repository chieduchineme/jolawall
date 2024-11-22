from .labelPreprocessing import preprocess_features_and_labels
from ..initNeuralNetworks.usingChecks.baseCNN_LSTM import create_model
from ..initNeuralNetworks.usingChecks.trainNN import train_model
from sklearn.preprocessing import LabelEncoder
from threading import Lock

class NoThreatsDetectedError(Exception):
    pass

# Global variable for caching the API client
model = None
cache_lock = Lock()  #
label_encoder = LabelEncoder()

def loadPredModel(train_requests):
    global model
    global cache_lock
    global label_encoder

    # Prepare the feature matrix X and label vector y
    X, encoded_labels_one_hot, label_encoder = preprocess_features_and_labels(train_requests)
    num_classes = len(label_encoder.classes_)
    # Create and train the model
    model = create_model(num_classes)

    model, X_padded = train_model(model, X, encoded_labels_one_hot)
    return model, label_encoder, X_padded
