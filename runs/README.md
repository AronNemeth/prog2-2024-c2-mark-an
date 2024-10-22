# 2024-10-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.33024  |       1.09244  |   0.113797 |
| solution-pl        |     5.9643   |       0.112282 |   0.181278 |
| solution-aron-mark |     0.574936 |       0.108867 |   0.188643 |
| solution-1-flask   |     0.587666 |       1.00952  |   0.265804 |
| solution-1         |     7.92446  |       1e-06    |   0.599296 |
| solution-2         |     0.567639 |       0.513437 |   0.790298 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.579391 |       0.112113 |   0.303806 |
| solution-aron-mark |     0.57096  |       0.110198 |   0.305137 |
| solution-flask     |     0.569115 |       1.00899  |   0.478411 |
| solution-1-flask   |     0.573263 |       1.00887  |   0.769373 |
| solution-2         |     0.572507 |       0.496116 |   1.99254  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.560473 |       0.119106 |    1.0047  |
| solution-pl        |     0.586286 |       0.11668  |    1.02195 |
| solution-flask     |     0.55601  |       1.00922  |    2.11166 |
| solution-1-flask   |     0.566228 |       1.00922  |    5.42533 |
| solution-2         |     0.56751  |       0.531751 |  164.643   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.554937 |       0.148829 |    4.29925 |
| solution-aron-mark |     0.562698 |       0.148821 |    4.38962 |
| solution-flask     |     0.559685 |       1.00939  |    8.52471 |