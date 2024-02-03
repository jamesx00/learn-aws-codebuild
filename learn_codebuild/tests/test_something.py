from learn_codebuild import some_class
import unittest


class TestSomething(unittest.TestCase):

    def test_class_return_true(self):
        test_object = some_class.SomeClass()
        self.assertTrue(test_object.return_true())

    def test_class_return_false(self):
        test_object = some_class.SomeClass()
        self.assertFalse(test_object.return_false())


if __name__ == "__main__":
    unittest.main()
