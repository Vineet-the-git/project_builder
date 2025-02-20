def bp_requirement_txt():
    return """pandas
scikit-learn
numpy
matplotlib
seaborn

# Add more dependencies
"""

def bp_config_yaml():
    return """data:
raw_path: data/raw
processed_path: data/processed

model:
    model_dir: models
    model_name: model.pkl

logger:
    log_dir: logs

train:
    train_dir: data/raw

test:
    test_dir: data/raw

# Add more configurations
"""

def bp_logger_py():
    return """import logging
import os

def setup_logger(name, log_level=logging.INFO, log_file="logs/project.log"):
    
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(log_format))

    # File handler
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
"""

def bp_load_config_py():
    return """import yaml

def get_configs(config_path = 'config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
"""

def bp_exception_py():
    return """import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
"""

def bp_make_dataset_py(boiler_plate=False, model_type='classical'):
    if not boiler_plate:
        return """# Create the custom dataset here"""
    else:
        if model_type == 'neural':
            return """import os
import pandas as pd
from PIL import Image
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms

from src.logger import setup_logger
logger = setup_logger(__name__)
from src.exceptions import CustomException

class CustomDataset(Dataset):
    def __init__(self, data_dir, transform=None):
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
"""
        else:
            return """import os
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
"""

def bp_model_py(boiler_plate=False, model_type='classical'):
    if not boiler_plate:
        return """# Create the model here"""
    else:
        if model_type == 'neural':
            return """import torch
import torch.nn as nn
import torch.nn.functional as F

from src.logger import setup_logger
logger = setup_logger(__name__)
from src.exceptions import CustomException

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        pass

    def forward(self, x):
        pass
        return x
"""
        else:
            return """import numpy as np
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
"""
        
def bp_train_model_py(boiler_plate=False, model_type='classical'):
    if not boiler_plate:
        return """# Train the model here"""
    else:
        if model_type == 'neural':
            return """import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from src.models.model import NeuralNetwork
from src.data.make_dataset import CustomDataset
from src.logger import setup_logger
logger = setup_logger(__name__)
from src.exceptions import CustomException

def train_model(model, train_loader, val_loader, config):

    # Define loss function and optimizer
    criterion = None
    optimizer = optim.Adam(model.parameters(), lr=config['train']['learning_rate'])

    # Train the model
    for epoch in range(config['train']['num_epochs']):
        loss_per_epoch = []
        
        for batch in tqdm(train_loader):
            input = batch['input']
            target = batch['target']

            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass
            output = model(input)

            # Calculate loss
            loss = criterion(output, target)

            # Backward pass
            loss.backward()

            # Optimize
            optimizer.step()

            loss_per_epoch.append(loss.item())

        # Log the loss
        logger.info(f"Epoch: {epoch}, Loss: {np.mean(loss_per_epoch)}")

        # validate the model
        if epoch%config['train']['val_freq'] == 0:
            val_loss = []
            model.eval()
            for batch in tqdm(val_loader):
                input = batch['input']
                target = batch['target']

                # Forward pass
                output = model(input)

                # Calculate loss
                loss = criterion(output, target)

                val_loss.append(loss.item())

            # Log the validation loss
            logger.info(f"Validation Loss: {np.mean(val_loss)}")

        # save the model

    return model


if __name__ == "__main__":
    config = get_configs()
    train_dataset = CustomDataset(data_dir=config['train']['train_dir'])
    train_loader = DataLoader(train_dataset, batch_size=config['train']['batch_size'], shuffle=True)
    val_dataset = CustomDataset(data_dir=config['train']['val_dir'])
    val_loader = DataLoader(val_dataset, batch_size=config['train']['batch_size'], shuffle=False)

    model = NeuralNetwork()
    model = train_model(model, train_loader, val_loader, config)
"""
        else:
            return """# Train your model here"""