# 2026-09-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.146    |       1.04996  |   0.109951 |
| solution-pl        |     0.431953 |       0.1619   |   0.242317 |
| solution-aron-mark |     6.48928  |       0.173466 |   0.244508 |
| solution-1-flask   |     0.435318 |       1.00831  |   0.27259  |
| solution-1         |     7.7296   |       1e-06    |   0.65855  |
| solution-2         |     0.42094  |       0.711603 |   1.26916  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436697 |       0.158803 |   0.37934  |
| solution-pl        |     0.434345 |       0.157317 |   0.384431 |
| solution-flask     |     0.437865 |       1.00868  |   0.399054 |
| solution-1-flask   |     0.439944 |       1.00862  |   0.807312 |
| solution-2         |     0.428587 |       0.506334 |   6.50896  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.43108  |       0.161167 |    1.13889 |
| solution-pl        |     0.430015 |       0.162209 |    1.15372 |
| solution-flask     |     0.433329 |       1.00885  |    1.67479 |
| solution-1-flask   |     0.433587 |       1.0086   |    5.76312 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433715 |       0.186732 |    3.58841 |
| solution-pl        |     0.425983 |       0.184341 |    3.59946 |
| solution-flask     |     0.428736 |       1.00881  |    5.36416 |