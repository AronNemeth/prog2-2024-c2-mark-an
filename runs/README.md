# 2026-07-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4745   |       1.0091   |   0.099527 |
| solution-1-flask   |     1.27924  |       1.14978  |   0.228082 |
| solution-pl        |     0.455903 |       0.1612   |   0.238879 |
| solution-aron-mark |     0.46662  |       0.157309 |   0.244799 |
| solution-1         |     7.96724  |       1e-06    |   0.741201 |
| solution-2         |     4.83526  |       0.667638 |   1.11578  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434164 |       0.156555 |   0.361605 |
| solution-aron-mark |     0.467205 |       0.161381 |   0.364594 |
| solution-flask     |     0.443342 |       1.00974  |   0.396643 |
| solution-1-flask   |     0.446929 |       1.00917  |   0.726135 |
| solution-2         |     0.463022 |       0.526102 |   2.8449   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449809 |       0.161691 |    1.0528  |
| solution-aron-mark |     0.43067  |       0.161103 |    1.10975 |
| solution-flask     |     0.43619  |       1.00938  |    1.64777 |
| solution-1-flask   |     0.446077 |       1.00937  |    5.94293 |
| solution-2         |     0.451365 |       0.58891  |   31.1199  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.433522 |       0.183297 |    3.56578 |
| solution-aron-mark |     0.43163  |       0.186077 |    3.58507 |
| solution-flask     |     0.429291 |       1.00943  |    5.19461 |