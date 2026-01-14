# 2026-01-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.70213  |       1.53441  |   0.094527 |
| solution-pl        |     0.44403  |       0.152886 |   0.223478 |
| solution-aron-mark |     0.435539 |       0.151387 |   0.224798 |
| solution-1-flask   |     0.451045 |       1.00699  |   0.236004 |
| solution-1         |     7.32074  |       1e-06    |   0.774297 |
| solution-2         |     4.66388  |       0.654175 |   0.807578 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443721 |       0.154368 |   0.333208 |
| solution-pl        |     0.438708 |       0.157958 |   0.334894 |
| solution-flask     |     0.440998 |       1.00684  |   0.415194 |
| solution-1-flask   |     0.444523 |       1.00681  |   0.72198  |
| solution-2         |     0.43426  |       0.493956 |  12.7845   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.446499 |       0.159127 |    1.00042 |
| solution-pl        |     0.433352 |       0.159447 |    1.00857 |
| solution-flask     |     0.437079 |       1.0069   |    1.75946 |
| solution-1-flask   |     0.445618 |       1.00675  |    5.60031 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.442488 |       0.184685 |    4.36275 |
| solution-aron-mark |     0.435019 |       0.190368 |    4.4878  |
| solution-flask     |     0.445345 |       1.00697  |    5.76365 |