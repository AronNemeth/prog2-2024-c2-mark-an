# 2025-08-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |    17.3806   |       1.13539  |   0.099555 |
| solution-pl        |     0.476024 |       0.153595 |   0.238853 |
| solution-aron-mark |     4.37613  |       0.154263 |   0.239727 |
| solution-1-flask   |     0.491609 |       1.00834  |   0.265713 |
| solution-1         |     7.15423  |       1e-06    |   0.595532 |
| solution-2         |     0.480262 |       0.799647 |   0.882239 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496382 |       1.00838  |   0.372411 |
| solution-aron-mark |     0.481668 |       0.153539 |   0.379041 |
| solution-pl        |     0.519487 |       0.166794 |   0.383334 |
| solution-1-flask   |     0.51836  |       1.00859  |   0.797547 |
| solution-2         |     0.481217 |       0.510876 |   4.0674   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529775 |       0.172805 |    1.09975 |
| solution-pl        |     0.52248  |       0.16922  |    1.10897 |
| solution-flask     |     0.483779 |       1.00869  |    1.61604 |
| solution-1-flask   |     0.527638 |       1.00876  |    5.81864 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495874 |       0.192218 |    3.25514 |
| solution-pl        |     0.490198 |       0.194553 |    3.35876 |
| solution-flask     |     0.487013 |       1.00883  |    5.28342 |