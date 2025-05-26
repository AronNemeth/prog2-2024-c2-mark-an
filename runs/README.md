# 2025-05-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.81017  |       1.00813  |   0.096779 |
| solution-pl        |     0.492507 |       0.146468 |   0.22461  |
| solution-aron-mark |     0.49081  |       0.147908 |   0.227489 |
| solution-1-flask   |     4.8958   |       1.05368  |   0.263657 |
| solution-1         |     7.26417  |       1e-06    |   0.713845 |
| solution-2         |     0.504209 |       0.607615 |   1.15953  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504676 |       0.151792 |   0.353379 |
| solution-pl        |     0.511124 |       0.151219 |   0.355831 |
| solution-flask     |     0.515523 |       1.00831  |   0.367341 |
| solution-1-flask   |     0.51961  |       1.00822  |   0.777678 |
| solution-2         |     0.520054 |       0.539688 |   3.19251  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489923 |       0.153639 |    1.04057 |
| solution-pl        |     0.496523 |       0.152525 |    1.0615  |
| solution-flask     |     0.49033  |       1.00846  |    1.52629 |
| solution-1-flask   |     0.501147 |       1.00839  |    5.38638 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.493334 |       0.187246 |    3.13338 |
| solution-pl        |     0.493589 |       0.183447 |    3.18237 |
| solution-flask     |     0.494292 |       1.0081   |    4.90562 |