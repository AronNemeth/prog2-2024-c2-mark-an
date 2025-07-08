# 2025-07-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19888  |       1.10771  |   0.102071 |
| solution-pl        |     0.49376  |       0.150397 |   0.233818 |
| solution-aron-mark |     5.54708  |       0.181058 |   0.236423 |
| solution-1-flask   |     0.499419 |       1.00813  |   0.27002  |
| solution-1         |     7.38492  |       1e-06    |   0.709896 |
| solution-2         |     0.493895 |       0.695223 |   1.12926  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.500961 |       0.152736 |   0.365595 |
| solution-aron-mark |     0.496742 |       0.149772 |   0.379354 |
| solution-flask     |     0.502107 |       1.00835  |   0.386023 |
| solution-1-flask   |     0.506349 |       1.00821  |   0.809539 |
| solution-2         |     0.495227 |       0.495883 |   4.74351  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497799 |       0.156456 |    1.07157 |
| solution-aron-mark |     0.49754  |       0.15743  |    1.07921 |
| solution-flask     |     0.502344 |       1.00851  |    1.59743 |
| solution-1-flask   |     0.502504 |       1.00853  |    5.65465 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497406 |       0.189184 |    3.21932 |
| solution-aron-mark |     0.497476 |       0.187294 |    3.23379 |
| solution-flask     |     0.495414 |       1.00834  |    5.07244 |