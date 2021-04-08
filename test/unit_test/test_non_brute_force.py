from unittest import TestCase, skip
from src.best_pairs_finder_non_brute_force import BestPairsFinderNonBruteForce as BestPairs
import pytest

@pytest.mark.parametrize('particle_list, expected_best_pairs',
     [
         ([], [[]]),
         ([[0., -1.], [1., 2.]], [[[0., -1.], [1., 2.]]]),
         ([[1., 2.], [0., -1.]], [[[0., -1.], [1., 2.]]]),
         ([[-1, 0.], [0., -1.]], [[[-1., 0.], [0., -1.]]]),
         ([[0., 1.], [0., -1.]] ,[[[0,-1],[0,1]]] ),
         ([[0],[1],[2],[3]],[[[0],[1]],[[2],[3]]] ),
         ([[0],[2],[1],[3]],[[[0],[1]],[[2],[3]]] ),
         ([[0., 0.], [1., 1.], [9., 9], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10]]]),
         ([[0., 0.], [9., 9.], [1., 1.], [10., 10.]],
          [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10]]]),
         ([[0,0,0],[10,20,30],[1,3,5],[10,20,31]],
          [[[0,0,0],[1,3,5]],[[10,20,30],[10,20,31]]])
     ])
def test_best_positions(particle_list, expected_best_pairs):
    pairs_finder = BestPairs()
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
    pairs_finder = BestPairs()
    assert pairs_finder.calc_dist_of_two_particles(
        particle1=two_particles_positions[0], particle2=two_particles_positions[1]
        ) == expected_distance

@pytest.mark.parametrize('pairs_list, expected_pairs_list',
     [
         ([[]], [[]]),
         ([[[0., -1.], [1., 2.]]], [[[0., -1.], [1., 2.]]]),
         ([[[1., 2.], [0., -1.]]], [[[0., -1.], [1., 2.]]]),
         ([[[-1, 0.], [0., -1.]]], [[[-1., 0.], [0., -1.]]]),
         ([[[0., 1.], [0., -1.]]], [[[0,-1], [0,1]]] ),
         ( [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]],
           [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]] ),
         ( [[[1., 1.], [0., 0.]], [[10., 10.], [9., 9.]]],
           [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]] ),
         ( [[[10., 10.], [9., 9.]], [[1., 1.], [0., 0.]]],
           [[[0., 0.], [1., 1.]], [[9., 9.], [10., 10.]]] )
     ])
def test_sort_solution(pairs_list, expected_pairs_list):
    pairs_finder = BestPairs()
    assert pairs_finder.sort_solution(
        pairs_list
        ) == expected_pairs_list

@pytest.mark.parametrize( 'pairs_list, expected_energy',
    [
        ([[ [0.], [0.] ]], 0.),
        ([[ [0.], [1.] ]], 1.),
        ([[ [1.], [1.] ]], 0.),
        ([[ [0.], [2.] ]], 2.),
        ([ [[0,0],[3,4]], [[0,1],[5,13]] ] , 18. ),
    ])
def test_obtain_energy( pairs_list, expected_energy ):
    pairs_finder = BestPairs()
    assert pairs_finder.obtain_energy( pairs_list ) == expected_energy

class TestBestPairsFinder(TestCase):
    def test_nothing(self):
        self.assertTrue(True)