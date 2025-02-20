import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.logger import setup_logger
logger = setup_logger(__name__)
from src.exceptions import CustomException

class ClassicalModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        pass

    def train(self, X_train, y_train):
        pass

    def predict(self, X_test):
        pass
        return y_pred
