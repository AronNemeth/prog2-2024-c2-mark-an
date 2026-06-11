# 2026-06-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.24974  |       1.09413  |   0.111647 |
| solution-pl        |     6.92722  |       0.201586 |   0.237593 |
| solution-aron-mark |     0.434755 |       0.150069 |   0.265216 |
| solution-1-flask   |     0.437759 |       1.00821  |   0.270178 |
| solution-1         |     8.3139   |       1e-06    |   0.746271 |
| solution-2         |     0.691221 |       0.724312 |   1.12141  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447546 |       0.153216 |   0.364201 |
| solution-pl        |     0.425005 |       0.152371 |   0.377152 |
| solution-flask     |     0.42537  |       1.00835  |   0.389574 |
| solution-1-flask   |     0.432786 |       1.00801  |   0.814476 |
| solution-2         |     0.42145  |       0.510632 |   3.99568  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444694 |       0.157292 |    1.1084  |
| solution-aron-mark |     0.440847 |       0.156579 |    1.19699 |
| solution-flask     |     0.426006 |       1.00831  |    1.66965 |
| solution-1-flask   |     0.432904 |       1.00836  |    5.62496 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432835 |       0.182725 |    3.92688 |
| solution-pl        |     0.430122 |       0.186008 |    3.94908 |
| solution-flask     |     0.436295 |       1.00831  |    5.31407 |