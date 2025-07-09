# 2025-07-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.24488  |       1.06148  |   0.096378 |
| solution-pl        |     0.481386 |       0.147393 |   0.232455 |
| solution-aron-mark |     5.9283   |       0.209128 |   0.232635 |
| solution-1-flask   |     0.502943 |       1.00905  |   0.253575 |
| solution-1         |     7.89927  |       1e-06    |   0.701362 |
| solution-2         |     0.494621 |       0.634121 |   1.60126  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489322 |       0.147932 |   0.358429 |
| solution-pl        |     0.492896 |       0.148553 |   0.358598 |
| solution-flask     |     0.492955 |       1.00817  |   0.379463 |
| solution-1-flask   |     0.498136 |       1.00822  |   0.793104 |
| solution-2         |     0.492528 |       0.503655 |   6.24     |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492394 |       0.156352 |    1.0679  |
| solution-aron-mark |     0.494716 |       0.155763 |    1.07369 |
| solution-flask     |     0.492462 |       1.00831  |    1.58808 |
| solution-1-flask   |     0.503577 |       1.00839  |    5.65025 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49292  |       0.185685 |    3.21671 |
| solution-pl        |     0.491758 |       0.183903 |    3.24551 |
| solution-flask     |     0.493337 |       1.00821  |    5.06116 |