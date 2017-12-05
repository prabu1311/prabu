import unittest
from HtmlProblem import Htmlproblem
class Testhtmlprob (unittest.TestCase):
    
    def test_check(self):
        
        value = html.check_input("htmlprogram.txt")[1]
        self.assertEqual(value,True)
        self.assertNotEqual(value,"ram.txt")
        
  
    def test_operation(self):
        result =open("htmlprogram.txt","r").read()
        needed =html.operation("htmlprogram.txt")
        self.assertNotEqual(needed[0],result)
        self.assertEqual(needed[1],True)

if __name__ == '__main__':
    html=Htmlproblem()
    unittest.main()
    
