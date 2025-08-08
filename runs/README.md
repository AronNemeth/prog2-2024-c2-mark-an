# 2025-08-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4912   |       1.06898  |   0.100302 |
| solution-aron-mark |     4.70129  |       0.152359 |   0.240015 |
| solution-pl        |     0.505937 |       0.152633 |   0.241828 |
| solution-1-flask   |     0.515041 |       1.00817  |   0.260107 |
| solution-1         |     7.46644  |       1e-06    |   0.680759 |
| solution-2         |     0.498955 |       0.595542 |   1.00994  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.501342 |       0.153572 |   0.360218 |
| solution-pl        |     0.505084 |       0.153737 |   0.364354 |
| solution-flask     |     0.499785 |       1.00837  |   0.377383 |
| solution-1-flask   |     0.509677 |       1.00845  |   0.803794 |
| solution-2         |     0.493177 |       0.506591 |   6.08202  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502933 |       0.162625 |    1.05951 |
| solution-aron-mark |     0.499876 |       0.161827 |    1.06394 |
| solution-flask     |     0.506683 |       1.00852  |    1.58748 |
| solution-1-flask   |     0.509787 |       1.0085   |    5.61475 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500919 |       0.19795  |    3.20446 |
| solution-pl        |     0.511321 |       0.193433 |    3.22205 |
| solution-flask     |     0.500317 |       1.00842  |    5.08376 |