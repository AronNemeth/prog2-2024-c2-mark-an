# 2026-10-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.74085  |       1.07376  |   0.073378 |
| solution-1-flask   |     0.355197 |       1.00737  |   0.174984 |
| solution-aron-mark |     5.8014   |       0.228931 |   0.193601 |
| solution-pl        |     0.335545 |       0.135557 |   0.195488 |
| solution-1         |     7.20119  |       1e-06    |   0.564091 |
| solution-2         |     0.358178 |       0.599748 |   0.764913 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.373977 |       1.00774  |   0.1689   |
| solution-aron-mark |     0.348974 |       0.139679 |   0.299066 |
| solution-pl        |     0.348362 |       0.137352 |   0.309785 |
| solution-1-flask   |     0.349943 |       1.0075   |   0.59846  |
| solution-2         |     0.342247 |       0.417143 |   2.26386  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.364857 |       0.140861 |   0.850509 |
| solution-flask     |     0.480496 |       1.00846  |   0.891778 |
| solution-pl        |     0.369688 |       0.153824 |   0.914286 |
| solution-1-flask   |     0.510835 |       1.00878  |   4.42554  |
| solution-2         |     0.352075 |       0.470073 | 145.699    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.354833 |       0.190855 |    2.96695 |
| solution-pl        |     0.371372 |       0.169325 |    2.97499 |
| solution-flask     |     0.350714 |       1.00767  |    3.53238 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.359826 |       0.235956 |    18.2045 |
| solution-pl        |     0.354353 |       0.233942 |    18.6526 |