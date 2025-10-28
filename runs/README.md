# 2025-10-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.61101  |       1.03817  |   0.09804  |
| solution-aron-mark |     0.49742  |       0.159135 |   0.239867 |
| solution-pl        |     0.495273 |       0.15624  |   0.240646 |
| solution-1-flask   |     0.495005 |       1.00825  |   0.254518 |
| solution-1         |     8.42808  |       1e-06    |   0.749277 |
| solution-2         |     4.80638  |       0.771872 |   1.77104  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491999 |       0.158442 |   0.365694 |
| solution-aron-mark |     0.493672 |       0.160241 |   0.371436 |
| solution-flask     |     0.515638 |       1.00855  |   0.380771 |
| solution-1-flask   |     0.507584 |       1.00859  |   0.803255 |
| solution-2         |     0.49657  |       0.54048  |   4.1574   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521514 |       0.167681 |    1.08678 |
| solution-pl        |     0.510186 |       0.173485 |    1.08787 |
| solution-flask     |     0.497957 |       1.00849  |    1.6052  |
| solution-1-flask   |     0.502108 |       1.00877  |    5.66734 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.493458 |       0.199654 |    3.30461 |
| solution-pl        |     0.506898 |       0.201065 |    3.31963 |
| solution-flask     |     0.507074 |       1.00851  |    5.13848 |