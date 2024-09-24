# 2024-09-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2791   |       1.09719  |   0.083561 |
| solution-aron-mark |     1.90501  |       0.102825 |   0.177848 |
| solution-pl        |     0.560156 |       0.103435 |   0.178816 |
| solution-1-flask   |     0.5797   |       1.00803  |   0.254598 |
| solution-1         |     7.77777  |       1e-06    |   0.583802 |
| solution-2         |     4.51969  |       0.637334 |   1.8472   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563959 |       1.00857  |   0.207978 |
| solution-aron-mark |     0.560554 |       0.103948 |   0.305477 |
| solution-pl        |     0.560257 |       0.104517 |   0.307989 |
| solution-1-flask   |     0.582724 |       1.00848  |   0.782663 |
| solution-2         |     0.568671 |       0.498646 |   5.01523  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.556534 |       1.00844  |   0.946887 |
| solution-aron-mark |     0.556066 |       0.111021 |   1.05628  |
| solution-pl        |     0.558241 |       0.111611 |   1.06528  |
| solution-1-flask   |     0.562915 |       1.00806  |   5.49085  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.580834 |       1.00884  |    4.67579 |
| solution-aron-mark |     0.567691 |       0.138328 |    4.78193 |
| solution-pl        |     0.564915 |       0.14073  |    4.82758 |