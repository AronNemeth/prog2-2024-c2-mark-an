# 2024-12-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.26593  |       1.00866  |   0.105168 |
| solution-pl        |     0.546077 |       0.108405 |   0.185104 |
| solution-aron-mark |     0.560821 |       0.123523 |   0.209433 |
| solution-1-flask   |     4.97609  |       1.2397   |   0.263813 |
| solution-1         |     8.02158  |       1e-06    |   0.590698 |
| solution-2         |     0.553337 |       0.496174 |   1.42377  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539467 |       0.109732 |   0.317271 |
| solution-aron-mark |     0.534954 |       0.110747 |   0.318085 |
| solution-flask     |     0.530508 |       1.0087   |   0.503577 |
| solution-1-flask   |     0.536563 |       1.00917  |   0.801767 |
| solution-2         |     0.540407 |       0.480183 |   4.21181  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.540113 |       0.118052 |    1.06544 |
| solution-aron-mark |     0.548734 |       0.116663 |    1.09339 |
| solution-flask     |     0.541235 |       1.00883  |    2.27323 |
| solution-1-flask   |     0.548984 |       1.00921  |    5.85237 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534298 |       0.143314 |    4.39152 |
| solution-aron-mark |     0.536411 |       0.143595 |    4.41392 |
| solution-flask     |     0.540645 |       1.01014  |    8.94297 |