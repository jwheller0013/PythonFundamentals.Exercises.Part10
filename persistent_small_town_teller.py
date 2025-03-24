import small_town_teller
import json
import os
import pickle

class PersistenceUtils():
    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as handler:
            pickle.dump(data, handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, "rb") as handler:
            data = pickle.load(handler)
        return data

class Bank_persist(small_town_teller.Bank, PersistenceUtils):
    def save_data(self):
        self.write_pickle("/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part10/customers.pickle", self.customers)
        self.write_pickle("/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part10/accounts.pickle", self.accounts)

    def load_data(self):
        self.customers = self.load_pickle("/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part10/customers.pickle")
        self.accounts = self.load_pickle("/Users/jim/Projects/p1/PythonFundamentals.Exercises.Part10/accounts.pickle")