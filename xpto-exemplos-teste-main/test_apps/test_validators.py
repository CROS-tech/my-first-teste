import unittest
from apps.validators import Validators

class TestValidators(unittest.TestCase):
    def setUp(self):
        self.validator = Validators()

    def test_valid_identifier(self):
        self.assertTrue(self.validator.check_valid_identifier("abc"))
        self.assertTrue(self.validator.check_valid_identifier("abc123"))
        self.assertTrue(self.validator.check_valid_identifier("_abc"))
        self.assertTrue(self.validator.check_valid_identifier("a_b123"))
        self.assertTrue(self.validator.check_valid_identifier("abcdefghij"))

        # inválidos
        self.assertFalse(self.validator.check_valid_identifier("12abc"))
        self.assertFalse(self.validator.check_valid_identifier("$abc"))
        self.assertFalse(self.validator.check_valid_identifier("ab"))
        self.assertFalse(self.validator.check_valid_identifier("abcdefghijkl"))
        self.assertFalse(self.validator.check_valid_identifier("a bc"))
        self.assertFalse(self.validator.check_valid_identifier(""))

if __name__ == "__main__":
    unittest.main()
