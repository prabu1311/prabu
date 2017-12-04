import unittest
from trainproblemmod import schedule

class Test_train (unittest.TestCase):
    def test_user_input(self):
        value = p. user_input(True)
        self.assertTrue(value,True)
            
    def test_train_details(self):
         res = p.train_details(True)[0]
         self.assertEqual(res,True)
         
    def test_best_board(self):
        val = p.best_board([12, "chennai",  3, "trichy"],4,"chennai","madurai")
        expected = [18, 'chennai', 7, 'vilupuram']
        self.assertEqual(expected,val[2])
        
    def test_finalchoice(self):
        choice =p.finalchoice(3,['chennai',  'madurai'])
        self.assertTrue(choice,True)
        
if __name__ == '__main__':
    p = schedule()
    unittest.main()
