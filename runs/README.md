# 2025-04-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23171  |       1.12924  |   0.084066 |
| solution-aron-mark |     0.504982 |       0.121482 |   0.192351 |
| solution-pl        |     5.56665  |       0.120161 |   0.193373 |
| solution-1-flask   |     0.52873  |       1.00844  |   0.266787 |
| solution-1         |     7.86924  |       1e-06    |   0.743677 |
| solution-2         |     0.504646 |       0.686185 |   0.761004 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.522689 |       1.01025  |   0.291024 |
| solution-aron-mark |     0.523057 |       0.122237 |   0.296935 |
| solution-pl        |     0.503655 |       0.120976 |   0.296985 |
| solution-1-flask   |     0.528139 |       1.00877  |   0.807139 |
| solution-2         |     0.518337 |       0.514067 |   2.65812  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.536075 |       0.128295 |   0.881237 |
| solution-pl        |     0.521251 |       0.130339 |   0.887866 |
| solution-flask     |     0.513672 |       1.009    |   1.23346  |
| solution-1-flask   |     0.511588 |       1.00879  |   5.36138  |
| solution-2         |     0.507714 |       0.549234 |  42.0679   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506517 |       0.159621 |    2.77549 |
| solution-aron-mark |     0.506949 |       0.160089 |    2.78599 |
| solution-flask     |     0.505477 |       1.00982  |    4.14662 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507754 |       0.265233 |    15.5022 |
| solution-pl        |     0.510366 |       0.268724 |    15.7917 |