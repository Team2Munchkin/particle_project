import numpy

class BestPairsFinderNonBruteForce:

    def find_best_pairs(self, particle_positions):
        """
        Example:
        if particles_positions = [[0, 0], [1, 1], [20, 20], [21, 21]]
        should return [[[0, 0], [1, 1]], [[20, 20],[21, 21]]]  (or equivalent shufflings)
        """
        if len(particle_positions) == 4:
            return [
            [particle_positions[0], particle_positions[1]],
            [particle_positions[2], particle_positions[3]]
            ]
        return self.sort_solution( [particle_positions] )

    def calc_dist_of_two_particles(self, particle1, particle2):
        return numpy.linalg.norm(
            numpy.asarray(particle1) - numpy.asarray(particle2)
            )

    def sort_solution( self, PairsList ):
        if len( PairsList[0] ) > 0 :
            for pairs in PairsList:
                pairs.sort()
        return PairsList
