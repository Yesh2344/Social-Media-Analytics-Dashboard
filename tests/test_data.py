import unittest
from utils.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        data = load_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()