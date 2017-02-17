import unittest
from train import build_new_list, erase_useless_elements, replace_cards, replace_numbers, train


class Testreplace_numbers(unittest.TestCase):
    def test_when_4_nord_return_4_1(self):
        src_list = [1, 1, 1, 1]
        self.assertEqual(['nord', 'nord', 'nord', 'nord'],
                         replace_numbers(src_list))

    def test_when_1_moins_1_2_moins_2_return_nord_sud_est_ouest(self):
        src_list = [1, -1, 2, -2]
        self.assertEqual(['nord', 'sud', 'est', 'ouest'],
                         replace_numbers(src_list))


class Testreplace_cards(unittest.TestCase):
    def test_when_4_1_return_4_nord(self):
        src_list = ['nord', 'nord', 'nord', 'nord']
        self.assertEqual([1, 1, 1, 1],
                         replace_cards(src_list))

    def test_when_nord_sud_est_ouest_return_1_moins_1_2_moins_2(self):
        src_list = ['nord', 'sud', 'est', 'ouest']
        self.assertEqual([1, -1, 2, -2],
                         replace_cards(src_list))


class Testbuild_new_list2(unittest.TestCase):
    def test_when_start_1_and_return_src_list_without_b_and_c(self):
        src_list = ['a', 'b', 'c', 'd', 'f', 'g']

        self.assertEqual(['a', 'd', 'f', 'g'],
                         build_new_list(src_list, 1))


class Testerase_useless_elements(unittest.TestCase):
    def test_when1_1(self):
        src_list = [1]
        self.assertEqual([1], erase_useless_elements(src_list))

    def test_when4_4(self):
        src_list = [1, 1, 1, 1]
        self.assertEqual([1, 1, 1, 1], erase_useless_elements(src_list))

    def test_when5_4(self):
        src_list = [1, 1, 1, 1, -1]
        self.assertEqual([1, 1, 1], erase_useless_elements(src_list))


class Testtrain(unittest.TestCase):
    def test_when_NSEO_return_NSEO(self):
        src_list = ['nord', 'sud', 'est', 'ouest']

        self.assertEqual(['nord', 'sud', 'est', 'ouest'],
                         train(src_list))

    def test_when_Nord2_return_Nord(self):
        src_list = ['nord', 'nord', 'nord', 'nord', 'nord']

        self.assertEqual(['nord', 'nord', 'nord', 'nord', 'nord'],
                         train(src_list))

    def test_when_Nord_return_Nord(self):
        src_list = ['nord', 'nord', 'sud', 'nord']

        self.assertEqual(['nord', 'nord'],
                         train(src_list))

    def test_kata_return_ouest(self):
        src_list = ["nord", "sud", "sud", "est", "ouest", "nord", "ouest"]
        self.assertEqual(['ouest'],
                         train(src_list))


if __name__ == '__main__':
    unittest.main()
