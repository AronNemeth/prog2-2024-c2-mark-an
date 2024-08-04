# 2024-08-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.09776  |       1.08853  |   0.078329 |
| solution-aron-mark |     0.570106 |       0.100971 |   0.168216 |
| solution-pl        |     1.87522  |       0.1033   |   0.17039  |
| solution-1-flask   |     0.559638 |       1.00864  |   0.262853 |
| solution-1         |     7.68718  |       1e-06    |   0.727524 |
| solution-2         |     4.46663  |       0.695118 |   1.24031  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553708 |       1.00894  |   0.223056 |
| solution-pl        |     0.555555 |       0.103559 |   0.288818 |
| solution-aron-mark |     0.553292 |       0.103849 |   0.290407 |
| solution-1-flask   |     0.557914 |       1.00892  |   0.791869 |
| solution-2         |     0.560867 |       0.475618 |   3.66484  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552305 |       1.00923  |   0.884713 |
| solution-pl        |     0.553234 |       0.112959 |   0.98051  |
| solution-aron-mark |     0.550407 |       0.111458 |   0.988796 |
| solution-1-flask   |     0.557115 |       1.00901  |   5.52422  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549287 |       1.00908  |    4.2237  |
| solution-aron-mark |     0.553895 |       0.142019 |    4.32492 |
| solution-pl        |     0.562732 |       0.143473 |    4.38315 |