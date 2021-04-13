from src.particle_generator import *
import pytest

def test_do_nothing():
    pass

@pytest.mark.parametrize('particles, expected_particles',
                         [
                             ([2, 2], [[0.769749131946113, 0.9228646209386234], [0.451167888968656, 0.19329838709658942]]),
                             ([0, 0], [])
                         ])
def test_particle_generator(particles, expected_particles):
    assert create_even_number_of_particles(num_particles=particles[0], dimension=particles[1]) == expected_particles
