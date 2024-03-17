# 2024-03-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.6828   |       1.19261  |   0.064406 |
| solution-pl        |     0.662899 |       0.108378 |   0.159627 |
| solution-aron-mark |     0.65986  |       0.106525 |   0.160213 |
| solution-1-flask   |     0.668254 |       1.00847  |   0.26738  |
| solution-1         |     8.29719  |       1e-06    |   0.634874 |
| solution-2         |     4.68756  |       0.457523 |   1.00291  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658033 |       1.00859  |   0.164832 |
| solution-aron-mark |     0.662041 |       0.112525 |   0.250462 |
| solution-pl        |     0.666149 |       0.113283 |   0.251609 |
| solution-1-flask   |     0.671146 |       1.00851  |   0.770879 |
| solution-2         |     0.661824 |       0.441619 |  13.0224   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.665302 |       0.119901 |   0.80165  |
| solution-aron-mark |     0.664812 |       0.121857 |   0.814322 |
| solution-flask     |     0.659272 |       1.0085   |   0.923448 |
| solution-1-flask   |     0.681182 |       1.00841  |   5.47398  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.662778 |       0.153951 |    3.29268 |
| solution-pl        |     0.673922 |       0.154896 |    3.31847 |
| solution-flask     |     0.667409 |       1.00912  |    5.36711 |