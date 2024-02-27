import pickle
import datetime
from typing import List
import pandas as pd
from abc import ABC, abstractmethod

class RevenuePredictor(ABC):
    def __init__(self, model_name) -> None:
        """
        Load model dari file yang tersedia
        """
        with open(f"models/{model_name}.pkl", "rb") as fin:
            try:
                self.__module__=pickle.load(fin)
            except (OSError, FileNotFoundError, TypeError):
                print("wrong path / model not available")
                exit(-1)
'''
def calculate_next_date(self, prev_date):
    """
    Calculate next date
    date_format = yyyy-mm-dd
    """
    self.next_date = datetime.datetime(
        *list(map(lambda x: int(x), prev_date.split("-")))
    ) + datetime.timedelta(
        days=1
    ) 
'''
def calculate_next_date(self, prev_date):
        """
        Calculates next date
        date_format = yyyy-mm-dd
        """
        self.next_date = datetime.datetime(
            *list(map(lambda x: int(x), prev_date.split("-")))
        ) + datetime.timedelta(
            days=1
        )  # next date

def get_next_date(self, prev_date):
        try:
            return self.next_date.strftime("%y-%m-%d")
        except NameError:
            self.calculate_next_date(prev_date)

@abstractmethod
def predict(self, prev_date) -> List:
     pass

@abstractmethod
def preprocess_inputs(self, prev_date):
        pass
