from unittest import TestCase, skip
from src.best_pairs_finder import BestPairsFinder
import pytest

@pytest.mark.parametrize('particle_list, expected_best_pairs',
     [
         (list(), [[]]),
         ([[0., -1.], [1., 2.]], [[[0., -1.], [1., 2.]]]),
         ([[0., 0.], [1., 1.], [9., 9], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10]]])
     ])
def test_best_positions(particle_list, expected_best_pairs):
    pairs_finder = BestPairsFinder()
    assert pairs_finder.find_best_pairs(particle_positions=particle_list) == expected_best_pairs


class TestBestPairsFinder(TestCase):

    def test_nothing(self):
        self.assertTrue(True)
    #
    # def test_zero_particles(self):
    #     pairs_finder = BestPairsFinder()
    #     particle_positions = list()
    #     best_pairs = pairs_finder.find_best_pairs(particle_positions=particle_positions)
    #     self.assertTrue([[]] == best_pairs)
    #
    # def test_two_particles_in_two_dimensions(self):
    #     pairs_finder = BestPairsFinder()
    #     particle_positions = [[0., -1.], [1., 2.]]
    #     best_pairs = pairs_finder.find_best_pairs(particle_positions=particle_positions)
    #     self.assertCountEqual([[[0., -1.], [1., 2.]]], best_pairs)
    #
    # def test_four_particles_in_two_dimensions(self):
    #     pairs_finder = BestPairsFinder()
    #     particle_positions = [[0., 0.], [1., 1.], [9., 9], [10., 10.]]
    #     best_pairs = pairs_finder.find_best_pairs(particle_positions=particle_positions)
    #     self.assertCountEqual([
    #                 [[0., 0.], [1., 1.]],
    #                 [[9., 9.], [10., 10]]
    #                     ], best_pairs)
