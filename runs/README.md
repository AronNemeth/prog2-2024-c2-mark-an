# 2024-07-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496145 |       1.00871  |   0.086874 |
| solution-aron-mark |     0.511831 |       0.100613 |   0.166977 |
| solution-pl        |     5.66309  |       0.102445 |   0.168594 |
| solution-1-flask   |     1.07949  |       1.06002  |   0.257322 |
| solution-1         |     7.68437  |       1e-06    |   0.579005 |
| solution-2         |     0.514981 |       0.542971 |   0.865849 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500905 |       1.00927  |   0.225288 |
| solution-aron-mark |     0.50951  |       0.103225 |   0.286875 |
| solution-pl        |     0.499211 |       0.102927 |   0.287091 |
| solution-1-flask   |     0.50301  |       1.00921  |   0.782958 |
| solution-2         |     0.500192 |       0.47529  |   3.31126  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501328 |       1.00942  |   0.888033 |
| solution-pl        |     0.501781 |       0.112782 |   0.98357  |
| solution-aron-mark |     0.500565 |       0.111748 |   0.994505 |
| solution-1-flask   |     0.504486 |       1.00945  |   5.49804  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.49759  |       1.00906  |    4.30569 |
| solution-aron-mark |     0.501485 |       0.146326 |    4.33368 |
| solution-pl        |     0.495985 |       0.147194 |    4.40593 |