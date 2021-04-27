import numpy
from numpy.random import seed, rand, randint

class BestPairsFinderNonBruteForce:

    def find_best_pairs(self, particle_positions, MAX_ITERATIONS = -1, \
            seed_for_np=None, activation_energy=-1 ):
        """
        Example:
        if particles_positions = [[0, 0], [1, 1], [20, 20], [21, 21]]
        should return [[[0, 0], [1, 1]], [[20, 20],[21, 21]]]  (or equivalent shufflings)
        """
        number_particles = len(particle_positions)
        if number_particles >= 4:
            # generate an initial list of pairs from the array of positions
            list1 = particle_positions[::2]
            list2 = particle_positions[1::2]
            PairsList = [ [part1,part2] for part1,part2 in zip(list1,list2) ]

            # obtain the current energy
            energy = self.obtain_energy( PairsList )

            # save the current list as the best list
            min_energy = energy
            BestPairsList = PairsList.copy()
            if ( activation_energy == -1 ):
                activation_energy = energy
            # verify if the activation energy is not too small
            eps = 1e-6
            if( activation_energy < eps ):
                activation_energy = eps

            # iterate over pairs to eventually exchange two particles from neighboring pairs
            if MAX_ITERATIONS == -1:
                MAX_ITERATIONS = int(self.number_different_pairs( number_particles ))
            for counter in range( MAX_ITERATIONS ):
                # randomly exchange two particles
                for i in range( len(PairsList) ):
                    NewPairsList = self.exchange_neighbors( i, PairsList, \
                        seed_for_np=seed_for_np )
                    # check the energy for the new configuration
                    new_energy = self.obtain_energy( NewPairsList )
                    if ( new_energy < energy ):
                        energy = new_energy
                        PairsList = NewPairsList.copy()
                        if( new_energy < min_energy ):
                            min_energy = new_energy
                            BestPairsList = NewPairsList.copy()
                    else:
                        seed( seed_for_np )
                        delta_e = new_energy-energy
                        prob = numpy.exp( -delta_e/activation_energy )
                        if( rand() < prob ):
                            PairsList = NewPairsList.copy()
                            energy = new_energy

            # decide if the new configation is accepted
            return self.sort_solution( BestPairsList )
        return self.sort_solution( [particle_positions] )

    def calc_dist_of_two_particles(self, particle1, particle2):
        return numpy.linalg.norm(
            numpy.asarray(particle1) - numpy.asarray(particle2)
            )

    def sort_solution( self, PairsList ):
        if len( PairsList ) > 0 :
            # sort each pair
            for pairs in PairsList:
                pairs.sort()
            # sort pairs
            PairsList.sort()
        return PairsList

    def obtain_energy( self, PairsList ):
        energy = 0
        for pairs in PairsList:
            energy += self.calc_dist_of_two_particles( pairs[0], pairs[1] )
        return energy

    def number_different_pairs( self, n ):
        # check if n is even
        if n%2:
            return -1
        prod = 1
        counter = 3
        while counter < n:
            prod = prod*counter
            counter += 2
        return prod

    def exchange_neighbors( self, n, PairsList, seed_for_np=None ):
        # first pair
        f0, f1 = PairsList[n]
        # second pair
        index_second_pair = (n+1)%len(PairsList)
        s0, s1 = PairsList[index_second_pair]
        # copy of PairsList
        NewPairsList = PairsList.copy()
        # randomly pick two integers
        seed( seed_for_np )
        i, j = randint( 0, 2, size=2 )
        if i==0:
            if j==0:
                NewPairsList[n] = [f1,s0]
                NewPairsList[index_second_pair] = [f0,s1]
            else:
                NewPairsList[n] = [f1,s1]
                NewPairsList[index_second_pair] = [f0,s0]
        else:
            if j==0:
                NewPairsList[n] = [f0,s0]
                NewPairsList[index_second_pair] = [f1,s1]
            else:
                NewPairsList[n] = [f0,s1]
                NewPairsList[index_second_pair] = [f1,s0]
        return NewPairsList
