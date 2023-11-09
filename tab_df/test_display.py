import unittest
import pandas as pd
from app.tab_df.display import display_tab_df_content

class TestDisplayTabDFContent(unittest.TestCase):

    def test_display_tab_df_content(self):
        file_path = 'test.csv'
        df = pd.read_csv(file_path)
        display_tab_df_content(file_path)
        self.assertEqual(len(st._get_report_ctx().buffer), 2)
        self.assertEqual(st._get_report_ctx().buffer[0].table.columns.tolist(), df.columns.tolist())
        self.assertEqual(st._get_report_ctx().buffer[1].slider.label, "Number of rows")