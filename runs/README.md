# 2026-11-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.430104 |       1.01037  |   0.096705 |
| solution-pl        |     7.12216  |       0.168313 |   0.249381 |
| solution-aron-mark |     0.425628 |       0.162644 |   0.249675 |
| solution-1-flask   |     2.65008  |       1.04813  |   0.279038 |
| solution-1         |     8.89485  |       1e-06    |   0.590082 |
| solution-2         |     0.426972 |       0.54841  |   0.813871 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.418148 |       1.01076  |   0.224818 |
| solution-pl        |     0.43056  |       0.184365 |   0.38416  |
| solution-aron-mark |     0.431299 |       0.170893 |   0.390177 |
| solution-1-flask   |     0.429817 |       1.0106   |   0.78853  |
| solution-2         |     0.423097 |       0.505782 |   2.58037  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.419484 |       1.01067  |   0.997468 |
| solution-pl        |     0.417618 |       0.173714 |   1.12126  |
| solution-aron-mark |     0.419997 |       0.173734 |   1.12336  |
| solution-1-flask   |     0.42216  |       1.01043  |   5.43412  |
| solution-2         |     0.417341 |       0.556214 |  25.5555   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42019  |       0.211638 |    3.47482 |
| solution-pl        |     0.4219   |       0.216759 |    3.49169 |
| solution-flask     |     0.415686 |       1.01037  |    4.2034  |