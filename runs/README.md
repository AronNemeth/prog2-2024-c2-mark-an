# 2026-02-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.95819  |       1.04285  |   0.102202 |
| solution-aron-mark |     0.465269 |       0.160901 |   0.24555  |
| solution-pl        |     0.471962 |       0.163486 |   0.246992 |
| solution-1-flask   |     0.469762 |       1.00821  |   0.303651 |
| solution-1         |     8.28987  |       1e-06    |   0.68697  |
| solution-2         |     5.19674  |       0.63176  |   1.08446  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463827 |       0.16221  |   0.372226 |
| solution-pl        |     0.469402 |       0.162936 |   0.375313 |
| solution-flask     |     0.464612 |       1.00831  |   0.379556 |
| solution-1-flask   |     0.475041 |       1.0086   |   0.808042 |
| solution-2         |     0.46327  |       0.520385 |   2.68145  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485206 |       0.170412 |    1.08603 |
| solution-pl        |     0.465843 |       0.168449 |    1.09244 |
| solution-flask     |     0.470775 |       1.00874  |    1.5928  |
| solution-1-flask   |     0.476692 |       1.00854  |    5.59161 |
| solution-2         |     0.461978 |       0.558195 |  169.78    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463991 |       0.191986 |    3.54176 |
| solution-pl        |     0.459966 |       0.193539 |    3.55299 |
| solution-flask     |     0.464017 |       1.00825  |    5.14489 |