import unittest
from trainproblemnew import Schedule

class Test_train (unittest.TestCase):
    def test_user_input(self):
        value = p. user_input(True)
        self.assertTrue(value,True)
            
    def test_train_details(self):
         res = p.train_details(True)[0]
         self.assertEqual(res,True)
         
    def test_best_board(self):
        wholelist = [[5, 'madurai', 8, 'chennai'], [1, 'chennai ', 3, 'trichy'],
                     [5, 'vilupuram', 6, 'chennai'], [1, 'chennai', 4, 'vilipuram'],
                     [22, 'chennai', 3, 'trichy'], [14, 'chennai', 5, 'trichy'],
                     [18, 'chennai', 7, 'vilipuram'], [20, 'vilupuram', 9, 'chennai'],
                     [5, 'chennai', 14, 'madurai']]

        val = p.best_board(wholelist,15,"chennai","madurai")
        expected = [18, 'chennai', 7, 'vilupuram']
        self.assertNotEqual(expected,val[2])
        
    def test_finalchoice(self):
        choice =p.finalchoice(3,['chennai',  'madurai'])
        self.assertTrue(choice,True)
        
if __name__ == '__main__':
    p = Schedule()
    unittest.main()



##result =open("htmlprogram.txt","r").read()
##        needed =html.operation("htmlprogram.txt")
##        self.assertNotEqual(needed[0],result)
##        self.assertEqual(needed[1],True)
