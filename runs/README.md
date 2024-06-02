# 2024-06-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.4808   |       1.09797  |   0.076501 |
| solution-pl        |     0.65684  |       0.102654 |   0.160132 |
| solution-aron-mark |     6.01293  |       0.101255 |   0.161139 |
| solution-1-flask   |     0.699478 |       1.0088   |   0.267692 |
| solution-1         |     8.19364  |       1e-06    |   0.587718 |
| solution-2         |     0.65538  |       0.418955 |   1.02185  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668983 |       1.00897  |   0.163644 |
| solution-aron-mark |     0.664412 |       0.10439  |   0.255574 |
| solution-pl        |     0.669442 |       0.105258 |   0.256544 |
| solution-1-flask   |     0.675397 |       1.00889  |   0.807639 |
| solution-2         |     0.65728  |       0.429364 |   2.48217  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.669805 |       1.00974  |   0.730599 |
| solution-pl        |     0.676063 |       0.11441  |   0.81137  |
| solution-aron-mark |     0.667389 |       0.113329 |   0.813524 |
| solution-1-flask   |     0.693379 |       1.00924  |   5.61318  |
| solution-2         |     0.671535 |       0.482432 | 184.386    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.6763   |       1.00967  |    2.51498 |
| solution-aron-mark |     0.680889 |       0.150725 |    2.64676 |
| solution-pl        |     0.68107  |       0.151018 |    2.65621 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664006 |       1.00892  |    16.1609 |
| solution-pl        |     0.673375 |       0.280937 |    21.7813 |
| solution-aron-mark |     0.666188 |       0.275331 |    22.2156 |