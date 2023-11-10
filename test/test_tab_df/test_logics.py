import unittest
import pandas as pd
from app.tab_df.logics import Dataset

class TestDataset(unittest.TestCase):

    def setUp(self):
        self.tab_df = Dataset()

    def test_set_df(self):
        # Test that df is None before calling set_df
        self.assertIsNone(self.tab_df.df)

        # Test that df is set correctly when calling set_df
        file_path = 'test.csv'
        df = pd.read_csv(file_path)
        self.tab_df.file_path = file_path
        self.tab_df.set_df()
        pd.testing.assert_frame_equal(self.tab_df.df, df)

        # Test that df is not overwritten when calling set_df multiple times
        self.tab_df.set_df()
        pd.testing.assert_frame_equal(self.tab_df.df, df)