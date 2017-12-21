import time

import pandas as pd




MODEL_DIRECTORY = 'model'

MODEL_FILE_NAME = '%s/model_car_file.pkl' % MODEL_DIRECTORY


def predict(input_df, model):

    print("Input data frame is...\n")

    print("-----------")

    print(input_df)

    print("-----------")



    predictions = model.predict(input_df).tolist()

    predictions = [int(prediction) for prediction in predictions]



    return {'predictions': predictions}