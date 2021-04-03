import numpy

class BestPairsFinder:

    def find_best_pairs(self, particle_positions):
        """
        Example:
        if particles_positions = [[0, 0], [1, 1], [20, 20], [21, 21]]
        should return [[[0, 0], [1, 1]], [[20, 20],[21, 21]]]  (or equivalent shufflings)
        """
        if len(particle_positions) == 4:
            return [[particle_positions[0], particle_positions[1]],[particle_positions[2], particle_positions[3]]]
        return [particle_positions]

    # def check_combinations(self, particle_positions):
    #     distance_sums = list()
    #     distance_sums.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[1]) +
    #                          self.calc_dist_of_two_particles(particle_positions[2], particle_positions[3]))
    #     distance_sums.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[2]) +
    #                          self.calc_dist_of_two_particles(particle_positions[0], particle_positions[3]))
    #     distance_sums.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[2]) +
    #                          self.calc_dist_of_two_particles(particle_positions[1], particle_positions[3]))
    #
    #     ind = numpy.argmin(distance_sums)
    #     return best_solution

    def calc_dist_of_two_particles(self, particle1, particle2):
        return numpy.linalg.norm(numpy.asarray(particle1) - numpy.asarray(particle2))
