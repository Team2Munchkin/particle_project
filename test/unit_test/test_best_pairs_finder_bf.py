#from unittest import TestCase, skip
from src.best_pairs_finder import BestPairsFinder
import pytest

@pytest.mark.parametrize('particle_list, expected_best_pairs',
     [
         (list(), [[]]),
         ([[0., -1.], [1., 2.]], [[[0., -1.], [1., 2.]]]),
         ([[0., 0.], [1., 1.], [9., 9.], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]]),
         ([[0., 0.], [9., 9.], [1., 1.], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]]),
         ([[0., 9.], [9., 0.], [1., 10.], [10., 1.]],
          [[[0., 9.], [1., 10.]], [[9., 0.], [10., 1.]]]),
         ([[0., 321.], [3., 53.], [22., 63.], [1., 350.]],
          [[[0., 321.], [1., 350.]], [[3., 53.], [22., 63.]]]),
         ([[0., 2.], [4., 6.], [8., 10.], [12., 14.], [16., 18.], [20., 22.]],
          [[[0., 2.], [4., 6.]], [[8., 10.], [12., 14.]], [[16., 18.], [20., 22.]]]),
         ([[20., 22.], [4., 6.], [16., 18.], [12., 14.], [8., 10.], [0., 2.]],
          [[[0., 2.], [4., 6.]], [[8., 10.], [12., 14.]], [[16., 18.], [20., 22.]]])

     ])
def test_best_positions(particle_list, expected_best_pairs):
    pairs_finder = BestPairsFinder()
    assert pairs_finder.find_best_pairs(particle_positions=particle_list) == expected_best_pairs

@pytest.mark.parametrize('two_particles_positions, expected_distance',
     [
         ([ [0.], [0.] ], 0 ),
         ([ [0.], [1.] ], 1 ),
         ([ [0.,0.], [0.,1.] ], 1 ),
         ([ [4.,0.], [0.,3.] ], 5 ),
         ([ [2.,0.,2.], [0.,3.,0.] ], 17**0.5 )
     ])
def test_distance(two_particles_positions, expected_distance):
    pairs_finder = BestPairsFinder()
    assert pairs_finder.calc_dist_of_two_particles(
        particle1=two_particles_positions[0], particle2=two_particles_positions[1]
        ) == expected_distance

#class TestBestPairsFinder(TestCase):

#    def test_nothing(self):
#        self.assertTrue(True)
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
