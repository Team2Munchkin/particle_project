import numpy
from numpy.random import seed, rand, randint

class BestPairsFinderNonBruteForce:

    def find_best_pairs(self, particle_positions):
        """
        Example:
        if particles_positions = [[0, 0], [1, 1], [20, 20], [21, 21]]
        should return [[[0, 0], [1, 1]], [[20, 20],[21, 21]]]  (or equivalent shufflings)
        """
        if len(particle_positions) >= 4:
            # generate an initial list of pairs from the array of positions
            list1 = particle_positions[::2]
            list2 = particle_positions[1::2]
            PairsList = [ [part1,part2] for part1,part2 in zip(list1,list2) ]

            # obtain the current energy
            energy = self.obtain_energy( PairsList )

            # save the current list as the best list
            min_energy = energy
            BestPairsList = PairsList.copy()
            activation_energy = 0.3*energy
            eps = 1e-6
            if( activation_energy < eps ):
                activation_energy = eps

            # iterate over pairs to eventually exchange two particles from neighboring pairs
            MAX_ITERATIONS = 10
            for counter in range( MAX_ITERATIONS ):
                # randomly exchange two particles
                for i in range( len(PairsList)-1 ):
                    NewPairsList = self.exchange_neighbors( i, PairsList )
                    #print( counter, i, NewPairsList )
                    # check the energy for the new configuration
                    new_energy = self.obtain_energy( NewPairsList )
                    if ( new_energy < energy ):
                        energy = new_energy
                        PairsList = NewPairsList.copy()
                        if( new_energy < min_energy ):
                            min_energy = new_energy
                            BestPairsList = NewPairsList.copy()
                    else:
                        seed()
                        delta_e = new_energy-energy
                        prob = numpy.exp( -delta_e/activation_energy )
                        if( rand() < prob ):
                            PairsList = NewPairsList.copy()

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

    def exchange_neighbors( self, n, PairsList ):
        # first pair
        f0, f1 = PairsList[n]
        # second pair
        s0, s1 = PairsList[n+1]
        # copy of PairsList
        NewPairsList = PairsList.copy()
        # randomly pick two integers
        seed( )
        i, j = randint( 0, 2, size=2 )
        if i==0:
            if j==0:
                NewPairsList[n] = [f1,s0]
                NewPairsList[n+1] = [f0,s1]
            else:
                NewPairsList[n] = [f1,s1]
                NewPairsList[n+1] = [f0,s0]
        else:
            if j==0:
                NewPairsList[n] = [f0,s0]
                NewPairsList[n+1] = [f1,s1]
            else:
                NewPairsList[n] = [f0,s1]
                NewPairsList[n+1] = [f1,s0]
        return NewPairsList
