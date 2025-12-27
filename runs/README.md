# 2025-12-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.96073  |       1.06835  |   0.102499 |
| solution-pl        |     0.466199 |       0.159379 |   0.248052 |
| solution-aron-mark |     0.466684 |       0.161505 |   0.248584 |
| solution-1-flask   |     0.468775 |       1.00824  |   0.274021 |
| solution-1         |     8.71005  |       1e-06    |   0.701971 |
| solution-2         |     5.19335  |       0.627603 |   0.730139 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.491946 |       1.00835  |   0.370458 |
| solution-pl        |     0.479707 |       0.163892 |   0.373814 |
| solution-aron-mark |     0.46925  |       0.162964 |   0.374011 |
| solution-1-flask   |     0.4695   |       1.00849  |   0.834594 |
| solution-2         |     0.463685 |       0.503277 |   8.33637  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469362 |       0.16847  |    1.09866 |
| solution-pl        |     0.476646 |       0.169095 |    1.11512 |
| solution-flask     |     0.472805 |       1.00859  |    1.61236 |
| solution-1-flask   |     0.478514 |       1.00859  |    5.60898 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481761 |       0.195798 |    3.64466 |
| solution-pl        |     0.484688 |       0.200642 |    3.78558 |
| solution-flask     |     0.474291 |       1.00849  |    5.16187 |