"""Unit testing"""
import unittest
import tempfile
from data.dna_data import search as SearchClass

class TestSearch(unittest.TestCase):
    """Test cases"""
    search = SearchClass.Dnafreq()

    def test_0_import_dna_not_empty(self):
        """test 1"""
        fake_csv = [
            "start, length\n",
            "1, 1\n",
            ]
        temp = tempfile.NamedTemporaryFile(suffix=".csv")
        with open(temp.name, 'w') as _f:
            _f.writelines(fake_csv)
        data = self.search.read_data(temp.name)
        self. assertIsNotNone(data)

    def test_0_import_dna_correct(self):
        """test 2"""
        fake_csv = [
            "start, length\n",
            "10, 5\n",
            "5, 2\n",
            "20, 10\n",
            "10, 5\n",
            "10, 4\n"
        ]
        expect = [[5, 6, 1], [10, 13, 1], [10, 14, 2], [20, 29, 1]]
        temp = tempfile.NamedTemporaryFile(suffix=".csv")
        with open(temp.name, 'w') as _f:
            _f.writelines(fake_csv)
        data = self.search.read_data(temp.name)
        self.assertEqual(data, expect)

    def test_1_import_loc_not_empty(self):
        """test 3"""
        fake_csv = [
            "position, coverage\n",
            "1, \n",
        ]
        temp = tempfile.NamedTemporaryFile(suffix=".csv")
        with open(temp.name, 'w') as _f:
            _f.writelines(fake_csv)
        head, data = self.search.read_request(temp.name)
        self.assertIsNotNone(head)
        self.assertIsNotNone(data)

    def test_1_import_loc_correct(self):
        """test 4"""
        fake_csv = [
            "position, coverage\n",
            "3, \n",
            "5, \n"
        ]
        expect_h = ["position", " coverage"]
        expect_b = [[3, 0], [5, 0]]
        temp = tempfile.NamedTemporaryFile(suffix=".csv")
        with open(temp.name, 'w') as _f:
            _f.writelines(fake_csv)
        head, data = self.search.read_request(temp.name)
        self.assertEqual(head, expect_h)
        self.assertEqual(data, expect_b)

    def test_2_cal_not_empty(self):
        """test 5"""
        data = self.search.calculation([[2, 3, 1], [3, 5, 2], [7, 9, 1]], [[1, 0]])
        self.assertIsNotNone(data)

    def test_2_cal_correct(self):
        """test 6"""
        seq = [[3, 7, 1], [12, 16, 3], [15, 25, 1]]
        position = [[2, 0], [4, 0], [15, 0]]
        expect = [[2, 0], [4, 1], [15, 4]]
        data = self.search.calculation(position, seq)
        self.assertEqual(data, expect)

if __name__ == '__main__':
    unittest.main()
