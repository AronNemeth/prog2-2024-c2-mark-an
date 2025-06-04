# 2025-06-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.77737  |       1.00817  |   0.098836 |
| solution-aron-mark |     0.494493 |       0.146389 |   0.227784 |
| solution-pl        |     0.496684 |       0.148228 |   0.230906 |
| solution-1-flask   |     5.01712  |       1.05509  |   0.26541  |
| solution-1         |     7.62806  |       1e-06    |   0.695631 |
| solution-2         |     0.49351  |       0.644918 |   0.706311 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501453 |       0.151498 |   0.351236 |
| solution-pl        |     0.5567   |       0.151887 |   0.352312 |
| solution-flask     |     0.499123 |       1.00826  |   0.369376 |
| solution-1-flask   |     0.501076 |       1.00831  |   0.796713 |
| solution-2         |     0.496613 |       0.509279 |   3.33925  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500702 |       0.161764 |    1.04595 |
| solution-pl        |     0.493112 |       0.162446 |    1.05835 |
| solution-flask     |     0.50726  |       1.00849  |    1.53793 |
| solution-1-flask   |     0.498471 |       1.0085   |    5.40948 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.503125 |       0.185263 |    3.14464 |
| solution-aron-mark |     0.493412 |       0.187076 |    3.15882 |
| solution-flask     |     0.492424 |       1.00844  |    5.0612  |