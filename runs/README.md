# 2025-12-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.4055   |       1.13014  |   0.096686 |
| solution-aron-mark |     0.901819 |       0.161191 |   0.243598 |
| solution-pl        |     0.476083 |       0.161682 |   0.244294 |
| solution-1-flask   |     0.478588 |       1.00834  |   0.261645 |
| solution-1         |     7.9493   |       1e-06    |   0.752549 |
| solution-2         |     4.96823  |       0.743957 |   1.3487   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479524 |       0.164658 |   0.36794  |
| solution-aron-mark |     0.474787 |       0.163102 |   0.371406 |
| solution-flask     |     0.471817 |       1.00865  |   0.373456 |
| solution-1-flask   |     0.486511 |       1.00858  |   0.812635 |
| solution-2         |     0.470947 |       0.521156 |   4.37355  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481503 |       0.170889 |    1.07368 |
| solution-aron-mark |     0.501673 |       0.175516 |    1.08724 |
| solution-flask     |     0.474215 |       1.00868  |    1.58602 |
| solution-1-flask   |     0.50624  |       1.00865  |    5.5788  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477866 |       0.196095 |    3.59936 |
| solution-pl        |     0.478517 |       0.194141 |    3.60386 |
| solution-flask     |     0.494893 |       1.00842  |    5.14583 |