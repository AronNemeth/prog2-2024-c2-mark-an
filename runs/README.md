# 2024-07-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492697 |       1.00954  |   0.090126 |
| solution-pl        |     5.75941  |       0.101634 |   0.164671 |
| solution-aron-mark |     0.495456 |       0.099483 |   0.169767 |
| solution-1-flask   |     1.27918  |       1.09197  |   0.262539 |
| solution-1         |     7.79921  |       1e-06    |   0.663508 |
| solution-2         |     0.492046 |       0.53029  |   0.844632 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.491067 |       1.00888  |   0.191967 |
| solution-pl        |     0.494468 |       0.102532 |   0.285096 |
| solution-aron-mark |     0.494279 |       0.101637 |   0.294015 |
| solution-1-flask   |     0.49964  |       1.00887  |   0.772516 |
| solution-2         |     0.492031 |       0.464138 |   4.95427  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492078 |       1.00887  |   0.875341 |
| solution-aron-mark |     0.493601 |       0.110386 |   0.972474 |
| solution-pl        |     0.493645 |       0.109835 |   0.974927 |
| solution-1-flask   |     0.498252 |       1.00897  |   5.48944  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492152 |       1.00915  |    4.07062 |
| solution-aron-mark |     0.491659 |       0.148129 |    4.17825 |
| solution-pl        |     0.491424 |       0.150755 |    4.23715 |