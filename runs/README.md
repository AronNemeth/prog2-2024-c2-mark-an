# 2026-06-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.27185  |       1.099    |   0.103924 |
| solution-1-flask   |     0.443704 |       1.00873  |   0.229825 |
| solution-pl        |     0.496607 |       0.159333 |   0.230776 |
| solution-aron-mark |     0.430295 |       0.150342 |   0.240296 |
| solution-1         |     8.19005  |       2e-06    |   0.627434 |
| solution-2         |     5.00159  |       0.640132 |   0.794959 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.434235 |       0.150474 |   0.351899 |
| solution-pl        |     0.441364 |       0.157931 |   0.355284 |
| solution-flask     |     0.477143 |       1.00878  |   0.402356 |
| solution-1-flask   |     0.434289 |       1.00887  |   0.716105 |
| solution-2         |     0.436147 |       0.514286 |   2.87342  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.437688 |       0.162353 |    1.03614 |
| solution-aron-mark |     0.442693 |       0.165307 |    1.04345 |
| solution-flask     |     0.439027 |       1.00895  |    1.65413 |
| solution-1-flask   |     0.439889 |       1.0088   |    5.56887 |
| solution-2         |     0.430507 |       0.572289 |   28.9076  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427041 |       0.185446 |    3.87811 |
| solution-pl        |     0.443403 |       0.188211 |    4.01582 |
| solution-flask     |     0.436755 |       1.00897  |    5.44488 |