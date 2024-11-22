import json
from ..initNeuralNetworks.usingChecks.featureList import feature_list, feature_list2
from .classify_target_requests import  extract_dbFeatures
import numpy as np
from ..initNeuralNetworks.usingChecks.trainNN import preprocess_data
import os
import numpy as np
from keras.models import load_model
import pickle as pickle
import pandas as pd
from threading import Lock
from .embeddingclassifier import decode_indices


# Global variables for caching the API client
model = None
cache_lock = Lock()
label_encoder = None  # Start with None to track if the encoder is loaded
X_embeddings_list = None

def predAttacks(new_requests, model_path='saved_model.keras', encoder_path='label_encoder.pkl', embeddings_path='X_embeddings.pkl'):
    global model
    global cache_lock
    global label_encoder
    global X_embeddings_list

    with cache_lock:
        # Load the model and embeddings only if they haven't been loaded already
        if model is None:
            if os.path.exists(model_path):
                model = load_model(model_path)
                print("Model loaded from disk.")
                with open(encoder_path, 'rb') as f:
                    label_encoder = pickle.load(f)
                    print("Label encoder loaded from disk.")

        # Load X_embeddings_list if it's not already loaded
        if X_embeddings_list is None and os.path.exists(embeddings_path):
            with open(embeddings_path, 'rb') as f:
                X_embeddings_list = pickle.load(f)
                print("X_embeddings_list loaded from disk.")
                
    # Ensure new_requests is a DataFrame
    if isinstance(new_requests, list):
        new_requests = pd.DataFrame(new_requests)

    # Prepare features and make predictions
    new_feature_df = extract_dbFeatures(new_requests)
    Y = new_feature_df[feature_list2].values
    Y_padded = preprocess_data(Y)
    Y_padded = np.array(Y_padded)
    Y_padded = (Y_padded - np.mean(Y_padded)) / (np.std(Y_padded) + 1e-8)
    # Predict embeddings
    Y_embeddings_list = model.predict(Y_padded)
    
    # Initialize an empty list to store predicted labels
    predicted_labels = []
    # Loop through each set of probabilities in the embeddings list
    for idx, probs in enumerate(Y_embeddings_list):
        # Sort probabilities in descending order and get their corresponding indices
        sorted_probs = np.argsort(probs)[::-1]
        # Decode class indices into class labels
        sorted_class = decode_indices(label_encoder, [sorted_probs[1]])
        predicted_label = sorted_class

        # Append the predicted label to the list
        predicted_labels.append(predicted_label)
        
        # Split the predicted label into components
        class_category_description_split = predicted_label[0].split('-', 2)
        
        # Update new_feature_df at the current index
        new_feature_df.loc[idx, 'class'] = class_category_description_split[0]
        new_feature_df.loc[idx, 'category'] = class_category_description_split[1]
        new_feature_df.loc[idx, 'descriptionOfClass'] = class_category_description_split[2]

    # Ensure predicted_labels matches new_feature_df length
    if len(predicted_labels) != len(new_feature_df):
        raise ValueError(f"Length mismatch: predicted_labels ({len(predicted_labels)}) vs new_feature_df ({len(new_feature_df)})")

    # print(new_feature_df.head(1))
    result_json = new_feature_df.to_json(orient='records')
    # result_json = json.dumps(result_json, indent=2)
    return result_json
