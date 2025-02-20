import os
import pandas as pd
import numpy as np

from src.logger import setup_logger
logger = setup_logger(__name__)
from src.exceptions import CustomException

class CustomDataset:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = []
        pass
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        pass
        batch = {
        }
        return batch
