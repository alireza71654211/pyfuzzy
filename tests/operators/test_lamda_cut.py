
import unittest
from pyfuzzy.operators import lamda_cut

class LamdaCutTestCase(unittest.TestCase):

    def test_lamda_cut_1(self):  #error about great values in dic
        u = {0: 0.2, 1: 0.5, 2: 1.3}
        a = 0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_2(self):   #error about great values in dic
        u = {0: 0.2, 1: 0.5, 2: 3.1}
        a = 0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_3(self):    #error about int value of lamda-cut
        u = {0: 0.2, 1: 0.5, 2: 0.9}
        a = 1
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_4(self):     #error about great value of lamda-cut
        u = {0: 0.2, 1: 0.5, 2: 0.9}
        a = 2.1
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_5(self):                #error about wrong request
        u = {0: 0.2, 1: 2.5, 2: 1.3}
        a = 0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_6(self):                #error about wrong request
        u = {0: -0.2, 1: 0.5, 2: 3.5}
        a = 0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_7(self):                #error about wrong request
        u = {0: 0.2, 1: -0.5, 2: 0.7}
        a = 0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_8(self):                #error about wrong request
        u = {0: 0.2, 1: 0.5, 2: 0.7}
        a = -0.3
        self.assertRaises(TypeError, lambda: lamda_cut.lamda_cut(u, a))

    def test_lamda_cut_9(self):                #test about right values
        u = {0: 0.2, 1: 0.5, 2: 0.7, 3: 0.3123, 4: 0.1117, 5: 0.67843, 6: 0.00007}
        a = 0.3
        self.assertEqual(lamda_cut.lamda_cut(u, a),[0, 1, 1, 1, 0, 1, 0])

    def test_lamda_cut_10(self):                #test about right values
        u = {0: 0.00000000002, 1: 0.99999999999999999}
        a = 0.45678
        self.assertEqual(lamda_cut.lamda_cut(u, a),[0, 1])

    def test_lamda_cut_11(self):                #test about right values
        u = {0: 0.1, 1: 0.6, 2: 0.7, 3: 0.29}
        a = 0.30000000111
        self.assertEqual(lamda_cut.lamda_cut(u, a),[0, 1, 1, 0])

    def test_lamda_cut_12(self):                #test about right values
        u = {0: 0.2, 1: 0.1, 2: 0.7}
        a = 0.222222222222222223
        self.assertEqual(lamda_cut.lamda_cut(u, a),[0, 0, 1])

    def test_lamda_cut_13(self):                #test about right values
        u = {0: 0.2, 1: 0.5, 2: 0.7}
        a = 0.395832000011
        self.assertEqual(lamda_cut.lamda_cut(u, a),[0,1,1])

    def test_lamda_cut_14(self):               # test about right values
        u = {0: 0.5, 1: 0.1, 2: 0.2}
        a = 0.3
        self.assertEqual(lamda_cut.lamda_cut(u, a),[1,0,0])




if __name__ == '__main__':
    unittest.main()