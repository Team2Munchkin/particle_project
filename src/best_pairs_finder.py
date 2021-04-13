import numpy


class BestPairsFinder:

    def find_best_pairs(self, particle_positions):
        """
        Example:
        if particles_positions = [[0, 0], [1, 1], [20, 20], [21, 21]]
        should return [[[0, 0], [1, 1]], [[20, 20],[21, 21]]]  (or equivalent shufflings)
        """
        if len(particle_positions) == 4:
            distlist = []
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[1]))
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[2]))
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[3]))
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[2]))
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[3]))
            distlist.append(self.calc_dist_of_two_particles(particle_positions[2], particle_positions[3]))

            pairlist = []
            pairlist.append(distlist[0] + distlist[5])
            pairlist.append(distlist[1] + distlist[4])
            pairlist.append(distlist[2] + distlist[3])

            if pairlist.index(min(pairlist)) == 0:
                result = [[particle_positions[0], particle_positions[1]],
                        [particle_positions[2], particle_positions[3]]]
            if pairlist.index(min(pairlist)) == 1:
                result = [[particle_positions[0], particle_positions[2]],
                        [particle_positions[1], particle_positions[3]]]
            if pairlist.index(min(pairlist)) == 2:
                result = [[particle_positions[0], particle_positions[3]],
                        [particle_positions[1], particle_positions[2]]]

            for i in [0, 1]:
                if result[i][0][0] > result[i][1][0]:
                    result[i].reverse()
            if result[0][0][0] > result[1][0][0]:
                result.reverse()

            return result

        if len(particle_positions) == 6:

            distlist = []
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[1])) #0
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[2])) #1
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[3])) #2
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[4])) #3
            distlist.append(self.calc_dist_of_two_particles(particle_positions[0], particle_positions[5])) #4
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[2])) #5
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[3])) #6
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[4])) #7
            distlist.append(self.calc_dist_of_two_particles(particle_positions[1], particle_positions[5])) #8
            distlist.append(self.calc_dist_of_two_particles(particle_positions[2], particle_positions[3])) #9
            distlist.append(self.calc_dist_of_two_particles(particle_positions[2], particle_positions[4])) #10
            distlist.append(self.calc_dist_of_two_particles(particle_positions[2], particle_positions[5])) #11
            distlist.append(self.calc_dist_of_two_particles(particle_positions[3], particle_positions[4])) #12
            distlist.append(self.calc_dist_of_two_particles(particle_positions[3], particle_positions[5])) #13
            distlist.append(self.calc_dist_of_two_particles(particle_positions[4], particle_positions[5])) #14

            pairlist = []
            pairlist.append(distlist[0] + distlist[9] + distlist[14])
            pairlist.append(distlist[0] + distlist[10] + distlist[13])
            pairlist.append(distlist[0] + distlist[11] + distlist[12])
            pairlist.append(distlist[1] + distlist[6] + distlist[14])
            pairlist.append(distlist[1] + distlist[7] + distlist[13])
            pairlist.append(distlist[1] + distlist[8] + distlist[12])
            pairlist.append(distlist[2] + distlist[5] + distlist[14])
            pairlist.append(distlist[2] + distlist[7] + distlist[13])
            pairlist.append(distlist[2] + distlist[8] + distlist[11])
            pairlist.append(distlist[3] + distlist[5] + distlist[13])
            pairlist.append(distlist[3] + distlist[6] + distlist[11])
            pairlist.append(distlist[3] + distlist[8] + distlist[9])
            pairlist.append(distlist[4] + distlist[5] + distlist[12])
            pairlist.append(distlist[4] + distlist[6] + distlist[10])
            pairlist.append(distlist[4] + distlist[7] + distlist[9])


            if pairlist.index(min(pairlist)) == 0:
                result = [[particle_positions[0], particle_positions[1]],
                            [particle_positions[2], particle_positions[3]],
                            [particle_positions[4], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 1:
                result = [[particle_positions[0], particle_positions[1]],
                            [particle_positions[2], particle_positions[4]],
                            [particle_positions[3], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 2:
                result = [[particle_positions[0], particle_positions[1]],
                            [particle_positions[2], particle_positions[5]],
                            [particle_positions[3], particle_positions[4]]]
            if pairlist.index(min(pairlist)) == 3:
                result = [[particle_positions[0], particle_positions[2]],
                            [particle_positions[1], particle_positions[3]],
                            [particle_positions[4], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 4:
                result = [[particle_positions[0], particle_positions[2]],
                            [particle_positions[1], particle_positions[4]],
                            [particle_positions[3], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 5:
                result = [[particle_positions[0], particle_positions[2]],
                            [particle_positions[1], particle_positions[5]],
                            [particle_positions[3], particle_positions[4]]]
            if pairlist.index(min(pairlist)) == 6:
                result = [[particle_positions[0], particle_positions[3]],
                            [particle_positions[1], particle_positions[2]],
                            [particle_positions[4], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 7:
                result = [[particle_positions[0], particle_positions[3]],
                            [particle_positions[1], particle_positions[4]],
                            [particle_positions[2], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 8:
                result = [[particle_positions[0], particle_positions[3]],
                            [particle_positions[1], particle_positions[5]],
                            [particle_positions[2], particle_positions[4]]]
            if pairlist.index(min(pairlist)) == 9:
                result = [[particle_positions[0], particle_positions[4]],
                            [particle_positions[1], particle_positions[2]],
                            [particle_positions[3], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 10:
                result = [[particle_positions[0], particle_positions[4]],
                            [particle_positions[1], particle_positions[3]],
                            [particle_positions[2], particle_positions[5]]]
            if pairlist.index(min(pairlist)) == 11:
                result = [[particle_positions[0], particle_positions[4]],
                            [particle_positions[1], particle_positions[5]],
                            [particle_positions[2], particle_positions[3]]]
            if pairlist.index(min(pairlist)) == 12:
                result = [[particle_positions[0], particle_positions[5]],
                            [particle_positions[1], particle_positions[2]],
                            [particle_positions[3], particle_positions[4]]]
            if pairlist.index(min(pairlist)) == 13:
                result = [[particle_positions[0], particle_positions[5]],
                            [particle_positions[1], particle_positions[3]],
                            [particle_positions[2], particle_positions[4]]]
            if pairlist.index(min(pairlist)) == 14:
                result = [[particle_positions[0], particle_positions[5]],
                            [particle_positions[1], particle_positions[4]],
                            [particle_positions[2], particle_positions[3]]]


            for i in [0, 1, 2]:
                if result[i][0][0] > result[i][1][0]:
                        result[i].reverse()
            if result[0][0][0] > result[1][0][0]:
                result[0], result[1] = result[1], result[0]
            if result[0][0][0] > result[2][0][0]:
                result[0], result[2] = result[2], result[0]
            if result[1][0][0] > result[2][0][0]:
                result[1], result[2] = result[2], result[1]

            return result

            #testlist = []
            #for i in particle_positions:
            #    dummy = i[0] + i[1]
            #    testlist.append(dummy)
            #result = []
            #for i in range(4):
            #    result.append(testlist.index(min(testlist)))
            #    testlist[testlist.index(min(testlist))] = float('+inf')
            #return [[particle_positions[result[0]], particle_positions[result[1]]],
            #        [particle_positions[result[2]], particle_positions[result[3]]]]
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
