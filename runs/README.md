# 2024-08-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558048 |       1.00883  |   0.089216 |
| solution-pl        |     0.55601  |       0.103828 |   0.174887 |
| solution-aron-mark |     1.8784   |       0.106303 |   0.188555 |
| solution-1-flask   |     1.19091  |       1.04844  |   0.256696 |
| solution-1         |     7.5657   |       1e-06    |   0.646744 |
| solution-2         |     4.39837  |       0.574035 |   1.26712  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55302  |       1.00883  |   0.230045 |
| solution-aron-mark |     0.555171 |       0.105013 |   0.294367 |
| solution-pl        |     0.555506 |       0.110456 |   0.331356 |
| solution-1-flask   |     0.558283 |       1.00931  |   0.806566 |
| solution-2         |     0.561397 |       0.504138 |   3.01219  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558454 |       1.00926  |   0.913957 |
| solution-aron-mark |     0.558778 |       0.118902 |   1.03418  |
| solution-pl        |     0.56193  |       0.114091 |   1.03762  |
| solution-1-flask   |     0.565643 |       1.00897  |   5.58273  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.556206 |       1.00895  |    4.07296 |
| solution-pl        |     0.555635 |       0.145993 |    4.35105 |
| solution-aron-mark |     0.559129 |       0.143528 |    4.38058 |