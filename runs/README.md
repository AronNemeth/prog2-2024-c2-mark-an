# 2024-11-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.22216  |       1.14607  |   0.105449 |
| solution-aron-mark |     0.555088 |       0.107413 |   0.191744 |
| solution-pl        |     5.80291  |       0.108558 |   0.194716 |
| solution-1-flask   |     0.564172 |       1.00871  |   0.256609 |
| solution-1         |     7.62729  |       1e-06    |   0.586071 |
| solution-2         |     0.55292  |       0.494218 |   1.37462  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.566666 |       0.10963  |   0.291497 |
| solution-aron-mark |     0.559237 |       0.109495 |   0.295896 |
| solution-flask     |     0.555085 |       1.00913  |   0.468972 |
| solution-1-flask   |     0.565104 |       1.00911  |   0.764926 |
| solution-2         |     0.555444 |       0.471735 |  13.4358   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557015 |       0.11684  |    1.0081  |
| solution-pl        |     0.554769 |       0.116703 |    1.0348  |
| solution-flask     |     0.556921 |       1.00888  |    2.10043 |
| solution-1-flask   |     0.564641 |       1.00884  |    5.36919 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557629 |       0.147768 |    4.10549 |
| solution-pl        |     0.554441 |       0.148162 |    4.1113  |
| solution-flask     |     0.558987 |       1.00952  |    8.30547 |