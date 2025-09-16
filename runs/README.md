# 2025-09-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.486639 |       1.0083   |   0.102345 |
| solution-aron-mark |     0.481532 |       0.160424 |   0.239121 |
| solution-pl        |     5.89185  |       0.1705   |   0.245347 |
| solution-1-flask   |     1.10924  |       1.06439  |   0.266057 |
| solution-1         |     7.69432  |       1e-06    |   0.629653 |
| solution-2         |     0.4891   |       0.562397 |   1.38824  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.487652 |       0.158883 |   0.36483  |
| solution-aron-mark |     0.492097 |       0.156097 |   0.382903 |
| solution-flask     |     0.491702 |       1.00856  |   0.386881 |
| solution-1-flask   |     0.523622 |       1.00882  |   0.804337 |
| solution-2         |     0.491875 |       0.535597 |   4.01389  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488729 |       0.162145 |    1.09244 |
| solution-aron-mark |     0.495271 |       0.166684 |    1.09545 |
| solution-flask     |     0.498877 |       1.00871  |    1.61756 |
| solution-1-flask   |     0.496662 |       1.00881  |    5.70244 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491612 |       0.196162 |    3.34361 |
| solution-aron-mark |     0.487038 |       0.193748 |    3.40998 |
| solution-flask     |     0.492413 |       1.00866  |    5.24151 |