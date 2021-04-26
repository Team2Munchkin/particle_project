from argparse import ArgumentParser
import numpy as np
from src.best_pairs_finder_non_brute_force import BestPairsFinderNonBruteForce as BestPairs

class ParseArgs:
    def convert_to_dictionary( self, arg ):
        """
        Function that converts to a dictionary the arguments read from the terminal
        """
        dict = {
            'input': arg.i[0],
            'output': arg.o[0],
            'method': arg.m,
            'steps': arg.s
        }
        return dict

    def parse_arguments(self):
        """
        Function to parse the arguments from the terminal
        """
        parser = ArgumentParser()

        parser.add_argument('-i', metavar='--input', type=str, nargs=1,
            required=True, action='store',
            help='input file' )
        parser.add_argument('-o', metavar='--output', type=str, nargs=1,
            required=True, action='store',
            help='output file' )
        parser.add_argument('-m', metavar='--method', type=str,
            required=False, action='store',
            choices=['MC','bf','Monte_Carlo','brute_force'],
            default='MC',
            help='method. Possible choices: MC, bf, Monte_Carlo or brute_force' )
        parser.add_argument('-s', metavar='--steps', type=int,
            default=20, help='number of Monte-Carlo steps')

        args = parser.parse_args()

        # store a dictionary containing the arguments
        self.arguments_as_dictionary = self.convert_to_dictionary( args )
        # sanity check
        self.arguments_sanity_check()

    def arguments_sanity_check(self):
        # check if the number of steps is positive
        if self.arguments_as_dictionary['steps'] < 0:
            raise RuntimeError('Number of Monte-Carlo steps must be positive.')

    def name_of_input(self):
        return self.arguments_as_dictionary['input']

    def name_of_output(self):
        return self.arguments_as_dictionary['output']

    def name_of_method(self):
        return self.arguments_as_dictionary['method']

def check_if_data_contain_only_pairs(list_of_pairs):
    for pair in list_of_pairs:
        print(pair,len(pair))
        if len(pair) != 2:
            raise RuntimeError('data must contains a list with pairs')
    return True

def read_input(fname,dtype=float):
    data = np.loadtxt(fname=fname,dtype=dtype)
    # Convert from numpy array to list
    return data.tolist()

def write_output(fname,data):
    check_if_data_contain_only_pairs(data)
    with open(fname,'w') as out:
        for pairs in data:
            out.write(str(pairs[0]) + ', '+ str(pairs[1]) + '\n' )

if __name__ == '__main__':
    # Parse arguments
    arguments = ParseArgs()
    arguments.parse_arguments()
    # Name of files and method
    input = arguments.name_of_input()
    output = arguments.name_of_output()
    method = arguments.name_of_method()
    # Read input
    positions = read_input(fname=input,dtype=float)
    # Find best pairs
    pairs_finder = BestPairs()
    pairs = pairs_finder.find_best_pairs( \
        particle_positions=positions, MAX_ITERATIONS=20 )
    # Write to output
    write_output(fname=output,data=pairs)
    #print(pairs)
