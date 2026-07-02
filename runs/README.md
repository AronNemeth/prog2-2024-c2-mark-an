# 2026-07-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23138  |       1.04761  |   0.108077 |
| solution-1-flask   |     0.437255 |       1.00923  |   0.231766 |
| solution-aron-mark |     0.430541 |       0.151154 |   0.232746 |
| solution-pl        |     6.26784  |       0.263531 |   0.233373 |
| solution-1         |     7.84539  |       1e-06    |   0.818549 |
| solution-2         |     0.418303 |       0.668599 |   1.0705   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432755 |       0.155765 |   0.360361 |
| solution-aron-mark |     0.440852 |       0.154462 |   0.363554 |
| solution-flask     |     0.428511 |       1.00937  |   0.39852  |
| solution-1-flask   |     0.436762 |       1.00921  |   0.733824 |
| solution-2         |     0.431999 |       0.510478 |   2.28315  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.440984 |       0.164511 |    1.03936 |
| solution-aron-mark |     0.429826 |       0.161632 |    1.04523 |
| solution-flask     |     0.429458 |       1.00926  |    1.65088 |
| solution-1-flask   |     0.438376 |       1.00921  |    5.69531 |
| solution-2         |     0.436397 |       0.574628 |  321.702   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429888 |       0.188616 |    3.89341 |
| solution-aron-mark |     0.424667 |       0.185663 |    3.93257 |
| solution-flask     |     0.42899  |       1.00927  |    5.29018 |