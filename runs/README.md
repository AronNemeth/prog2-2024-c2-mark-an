# 2026-05-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.79811  |       1.03574  |   0.100604 |
| solution-pl        |     0.397715 |       0.144087 |   0.220291 |
| solution-aron-mark |     4.72593  |       0.13712  |   0.222082 |
| solution-1-flask   |     0.408208 |       1.00802  |   0.239522 |
| solution-1         |     7.71043  |       1e-06    |   0.636232 |
| solution-2         |     0.383373 |       0.59216  |   1.65694  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.402475 |       0.139777 |   0.3485   |
| solution-pl        |     0.39792  |       0.147789 |   0.35732  |
| solution-flask     |     0.407702 |       1.0074   |   0.363524 |
| solution-1-flask   |     0.39408  |       1.00783  |   0.750647 |
| solution-2         |     0.403599 |       0.489904 |   4.53328  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.40355  |       0.151367 |    1.09697 |
| solution-aron-mark |     0.413349 |       0.150838 |    1.10237 |
| solution-flask     |     0.393209 |       1.00796  |    1.59078 |
| solution-1-flask   |     0.409994 |       1.00855  |    5.529   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.407446 |       0.17295  |    3.69505 |
| solution-pl        |     0.408342 |       0.177057 |    3.7336  |
| solution-flask     |     0.404549 |       1.00808  |    5.26444 |