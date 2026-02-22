# 2026-02-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.85915  |       1.15268  |   0.119479 |
| solution-aron-mark |     0.445649 |       0.146051 |   0.233033 |
| solution-pl        |     0.446592 |       0.151161 |   0.233506 |
| solution-1-flask   |     0.450592 |       1.00842  |   0.283714 |
| solution-1         |    10.65     |       1e-06    |   0.673189 |
| solution-2         |     5.33962  |       0.626449 |   0.916747 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.441131 |       0.146335 |   0.361233 |
| solution-pl        |     0.448569 |       0.1488   |   0.362765 |
| solution-flask     |     0.440682 |       1.00854  |   0.382493 |
| solution-1-flask   |     0.449065 |       1.00853  |   0.811246 |
| solution-2         |     0.439986 |       0.503089 |   2.34354  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462828 |       0.156223 |    1.09474 |
| solution-aron-mark |     0.449364 |       0.155488 |    1.10159 |
| solution-flask     |     0.465694 |       1.00878  |    1.58783 |
| solution-1-flask   |     0.464445 |       1.00866  |    5.57025 |
| solution-2         |     0.439784 |       0.565644 |   35.54    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.450052 |       0.17964  |    3.88576 |
| solution-pl        |     0.461987 |       0.181743 |    3.89467 |
| solution-flask     |     0.448214 |       1.00857  |    5.15642 |