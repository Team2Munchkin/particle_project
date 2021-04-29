from src.best_pairs_finder_non_brute_force import BestPairsFinderNonBruteForce
from src.best_pairs_finder import BestPairsFinder
from particle_generator import create_even_number_of_particles
from timeit import default_timer as timer

class CompareMethods:
    def compare_given_particles( self, particle_positions , brute_force, \
            non_brute_force, steps_non_brute_force ):
        start = timer( )
        best_pairs_bf = brute_force.find_best_pairs( \
            particle_positions=particle_positions )
        end = timer( )
        time_bf = end-start
        best_pairs_nbf = non_brute_force.find_best_pairs( \
            particle_positions=particle_positions, \
                MAX_ITERATIONS=steps_non_brute_force )
        time_nbf = timer( ) - end
        # if( not(best_pairs_bf == best_pairs_nbf) ):
        #     print(best_pairs_bf)
        #     print(best_pairs_nbf)
        #     exit()
        return (best_pairs_bf == best_pairs_nbf), time_bf, time_nbf
    
    def compare_given_particles_and_dimension( self, num_particles, dimension, \
            brute_force, non_brute_force, steps_non_brute_force, seed=None ):
        particle_positions = create_even_number_of_particles( num_particles, \
            dimension, seed=seed )
        return self.compare_given_particles( particle_positions, \
            brute_force, non_brute_force, steps_non_brute_force )
    
    def compare_given_parameters_of_testset( self, ntests, num_particles, \
            dimension, brute_force, non_brute_force, steps_non_brute_force, \
                seed=None ):
        counter = 0
        time_bf = 0
        time_nbf = 0
        for i in range( ntests ):    
            is_equal, time_one_test_bf, time_one_test_nbf = \
                self.compare_given_particles_and_dimension( num_particles, \
                    dimension, brute_force, non_brute_force, \
                        steps_non_brute_force )
            time_bf += time_one_test_bf
            time_nbf += time_one_test_nbf
            if is_equal :
                counter += 1
        return counter, time_bf, time_nbf

if __name__ == '__main__':
    compare = CompareMethods()
    brute_force = BestPairsFinder()
    non_brute_force = BestPairsFinderNonBruteForce()
    steps_non_brute_force = 20
    number_of_tests = 1000
    number_of_particles = 4
    for number_of_particles in range(4,5,2):
        for steps_non_brute_force in range(1,10,1):
            for dimension in range(1,2,1):
                number_matches, time_bf, time_nbf = compare.compare_given_parameters_of_testset( number_of_tests, \
                    number_of_particles, dimension, brute_force, non_brute_force, steps_non_brute_force  )
                print( number_of_particles, steps_non_brute_force, dimension, number_matches/number_of_tests, time_bf, time_nbf )
