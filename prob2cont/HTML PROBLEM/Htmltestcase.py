import unittest
from HtmlProblem import prob
class Testprob (unittest.TestCase):
    
    def test_check(self):
        
        value = p.check("html.txt")[1]
        self.assertTrue(value,True)
  
    def test_operation(self):
        result = p.operation("html.txt")[1]
        self.assertTrue(result,True)
  
  
        #self.assertEqual(result, )
        
    #def test_display(self):

        #dis = p.display()
        #check = True
        #self.assertEqual(p.display(),check)
    

if __name__ == '__main__':
    p =prob()
    unittest.main()
    
