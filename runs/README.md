# 2024-07-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08299  |       1.20369  |   0.088378 |
| solution-pl        |     5.749    |       0.10566  |   0.16962  |
| solution-aron-mark |     0.508158 |       0.103724 |   0.169756 |
| solution-1-flask   |     0.518454 |       1.00895  |   0.26388  |
| solution-2         |     0.519202 |       0.549967 |   0.677897 |
| solution-1         |     7.74079  |       1e-06    |   0.742666 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.518192 |       1.00914  |   0.226207 |
| solution-pl        |     0.509154 |       0.105254 |   0.286725 |
| solution-aron-mark |     0.520923 |       0.106852 |   0.28923  |
| solution-1-flask   |     0.526897 |       1.00909  |   0.811695 |
| solution-2         |     0.515413 |       0.489077 |   5.30658  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510565 |       1.00916  |   0.902519 |
| solution-aron-mark |     0.527147 |       0.112625 |   0.997397 |
| solution-pl        |     0.518212 |       0.112831 |   1.00679  |
| solution-1-flask   |     0.523359 |       1.00957  |   5.65399  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506685 |       1.00908  |    4.44082 |
| solution-aron-mark |     0.510596 |       0.147581 |    4.45371 |
| solution-pl        |     0.521435 |       0.14801  |    4.51057 |