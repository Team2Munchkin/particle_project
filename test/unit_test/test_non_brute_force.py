from unittest import TestCase, skip
from src.best_pairs_finder_non_brute_force import BestPairsFinderNonBruteForce
import pytest

@pytest.mark.parametrize('particle_list, expected_best_pairs',
     [
         ([], [[]]),
         ([[0., -1.], [1., 2.]], [[[0., -1.], [1., 2.]]]),
         ([[1., 2.], [0., -1.]], [[[0., -1.], [1., 2.]]]),
         ([[-1, 0.], [0., -1.]], [[[-1., 0.], [0., -1.]]]),
         ([[0., 1.], [0., -1.]] ,[[[0,-1],[0,1]]] ),
         ([[0., 0.], [1., 1.], [9., 9], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10]]])
     ])
def test_best_positions(particle_list, expected_best_pairs):
    pairs_finder = BestPairsFinderNonBruteForce()
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
    pairs_finder = BestPairsFinderNonBruteForce()
    assert pairs_finder.calc_dist_of_two_particles(
        particle1=two_particles_positions[0], particle2=two_particles_positions[1]
        ) == expected_distance

class TestBestPairsFinder(TestCase):
    def test_nothing(self):
        self.assertTrue(True)
