# Best pairs finder

This functions finds the best pairs of particles.

# Script `find_optimal_pairs.py`
This script can be called from a terminal. It reads an input file with the coordinates of all particles and outputs an optimal solution.

## Example of use

```python src/find_optimal_pairs.py -i input -o output -m MC -s 20```

* `-i`: provides the name of the input file. In our example, it is `input`. Conditions:
  * the input is a **text file** with the position of all the particles
  * each line contains the coordinates of **one particle** separated by **spaces**
  * the **number of lines** must be equal the **number of particles**
* `-o`: name of the output file.
* `-m`: method to find the solution. Possible choices are `MC`, `bf`, `Monte_Carlo` or `brute_force`
* `-s`: number of Monte-Carlo steps. It must be a **positive integer**.

### Examples of input files
#### Six particles in one dimension
```
0
1
2
3
4
5
```

Considering that:
* that this input has the name `input.txt`
* the input has been saved inside the `src` directory (where `find_optimal_pairs.py` is located)
* the current directory is `src`

then the command
```python src/find_optimal_pairs.py -i input.txt -o output.txt -m MC -s 20```
has as output the file `output.txt` with the following intent

```
0.0, 1.0
2.0, 3.0
4.0, 5.0
```

#### Four particles in three dimensions
Similarly to the previous example, the input file has the following intent:
```
0 0 0
1 1 1
2 2 2
3 3 3
```

Then the command

```python src/find_optimal_pairs.py -i input.txt -o output.txt -m MC -s 20```

generates the following output

```
[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]
[2.0, 2.0, 2.0], [3.0, 3.0, 3.0]
```
