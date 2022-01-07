import unittest
from Survey import *

class TestSurveyCase(unittest.TestCase):
    def setUp(self):
        question = "Language?"
        self.my_survey=Survey(question)
        self.responses=["chinese", "english", "japanese"]

    def test_single(self):
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1],self.my_survey.responses)
    
    def test_All(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        self.assertEqual(self.responses,self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()
