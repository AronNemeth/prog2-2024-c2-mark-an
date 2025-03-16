# 2025-03-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510036 |       1.00863  |   0.083362 |
| solution-aron-mark |     1.87761  |       0.119539 |   0.185417 |
| solution-pl        |     0.513664 |       0.120024 |   0.186251 |
| solution-1-flask   |     4.86979  |       1.10715  |   0.265021 |
| solution-1         |     7.05376  |       1e-06    |   0.594321 |
| solution-2         |     0.512529 |       0.534345 |   0.785957 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513065 |       0.123232 |   0.290875 |
| solution-pl        |     0.513316 |       0.121463 |   0.29125  |
| solution-flask     |     0.507445 |       1.00904  |   0.294126 |
| solution-1-flask   |     0.514213 |       1.00877  |   0.79601  |
| solution-2         |     0.511776 |       0.501173 |   4.68613  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.515751 |       0.137304 |   0.903789 |
| solution-pl        |     0.508775 |       0.128624 |   0.905185 |
| solution-flask     |     0.509285 |       1.00898  |   1.25851  |
| solution-1-flask   |     0.518395 |       1.00893  |   5.67264  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511796 |       0.159628 |    2.84834 |
| solution-pl        |     0.518311 |       0.156156 |    2.851   |
| solution-flask     |     0.514777 |       1.01036  |    4.29311 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521713 |       0.264925 |    16.8656 |
| solution-aron-mark |     0.527235 |       0.265339 |    16.8732 |