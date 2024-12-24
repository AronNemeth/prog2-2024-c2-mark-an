# 2024-12-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.8047   |       1.00874  |   0.114548 |
| solution-pl        |     0.53382  |       0.111066 |   0.188946 |
| solution-aron-mark |     0.536828 |       0.111993 |   0.191222 |
| solution-1-flask   |     4.86801  |       1.05567  |   0.270424 |
| solution-1         |     7.46791  |       1e-06    |   0.597592 |
| solution-2         |     0.554358 |       0.497511 |   1.12416  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535541 |       0.11152  |   0.325426 |
| solution-pl        |     0.552772 |       0.113342 |   0.326475 |
| solution-flask     |     0.549579 |       1.0091   |   0.49092  |
| solution-1-flask   |     0.554258 |       1.00922  |   0.822349 |
| solution-2         |     0.567388 |       0.529965 |   2.45069  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534775 |       0.118693 |    1.08758 |
| solution-pl        |     0.538208 |       0.120055 |    1.09102 |
| solution-flask     |     0.530999 |       1.0091   |    2.1834  |
| solution-1-flask   |     0.603012 |       1.00954  |    5.85737 |
| solution-2         |     0.527499 |       0.529113 |   40.3409  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543205 |       0.149843 |    4.61865 |
| solution-aron-mark |     0.5351   |       0.14611  |    4.69843 |
| solution-flask     |     0.528872 |       1.00901  |    8.73353 |