# 2025-06-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.92952  |       1.00825  |   0.098245 |
| solution-pl        |     0.497296 |       0.14886  |   0.229229 |
| solution-aron-mark |     0.498049 |       0.147966 |   0.2342   |
| solution-1-flask   |     5.23108  |       1.04119  |   0.26657  |
| solution-1         |     7.64121  |       1e-06    |   0.620646 |
| solution-2         |     0.495113 |       0.587567 |   1.32005  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499311 |       0.149689 |   0.353765 |
| solution-aron-mark |     0.496475 |       0.152532 |   0.356371 |
| solution-flask     |     0.502647 |       1.0083   |   0.365096 |
| solution-1-flask   |     0.500463 |       1.00848  |   0.789509 |
| solution-2         |     0.500921 |       0.505277 |   5.77923  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499129 |       0.173566 |    1.04499 |
| solution-aron-mark |     0.498504 |       0.157157 |    1.04975 |
| solution-flask     |     0.502132 |       1.00851  |    1.55377 |
| solution-1-flask   |     0.505846 |       1.00851  |    5.38243 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496557 |       0.185947 |    3.16982 |
| solution-aron-mark |     0.495896 |       0.186079 |    3.17451 |
| solution-flask     |     0.499835 |       1.00833  |    5.01289 |