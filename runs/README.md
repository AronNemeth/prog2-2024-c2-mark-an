# 2024-09-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.38271  |       1.18952  |   0.100166 |
| solution-pl        |     0.61862  |       0.113645 |   0.18281  |
| solution-aron-mark |     5.96905  |       0.108717 |   0.188233 |
| solution-1-flask   |     0.630508 |       1.01001  |   0.268356 |
| solution-1         |     8.19926  |       1e-06    |   0.914599 |
| solution-2         |     0.616594 |       0.817189 |   1.49404  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.61113  |       1.00965  |   0.22857  |
| solution-pl        |     0.605781 |       0.109521 |   0.297877 |
| solution-aron-mark |     0.609488 |       0.109405 |   0.300226 |
| solution-1-flask   |     0.603894 |       1.00987  |   0.797851 |
| solution-2         |     0.619061 |       0.535096 |  12.7179   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.605379 |       1.00975  |   0.910545 |
| solution-aron-mark |     0.590852 |       0.118548 |   1.01384  |
| solution-pl        |     0.598614 |       0.120651 |   1.01863  |
| solution-1-flask   |     0.599281 |       1.00954  |   5.52868  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.587181 |       0.152732 |    4.51307 |
| solution-flask     |     0.58513  |       1.00929  |    4.58573 |
| solution-pl        |     0.598836 |       0.146579 |    4.70549 |