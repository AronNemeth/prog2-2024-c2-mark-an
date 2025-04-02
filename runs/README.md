# 2025-04-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.524775 |       1.00879  |   0.081192 |
| solution-pl        |     0.513376 |       0.119974 |   0.185278 |
| solution-aron-mark |     2.19974  |       0.12738  |   0.187759 |
| solution-1-flask   |     5.39362  |       1.14724  |   0.322324 |
| solution-1         |     8.02134  |       1e-06    |   0.944992 |
| solution-2         |     0.502017 |       0.752049 |   1.3095   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506297 |       0.120479 |   0.291579 |
| solution-pl        |     0.507794 |       0.120658 |   0.291852 |
| solution-flask     |     0.505844 |       1.00923  |   0.322985 |
| solution-1-flask   |     0.515779 |       1.00914  |   0.788031 |
| solution-2         |     0.505651 |       0.496892 |   4.38806  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504284 |       0.127913 |   0.895913 |
| solution-aron-mark |     0.503494 |       0.126234 |   0.896731 |
| solution-flask     |     0.519862 |       1.0089   |   1.25556  |
| solution-1-flask   |     0.521182 |       1.00914  |   5.61006  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.509713 |       0.158431 |    2.81169 |
| solution-aron-mark |     0.503211 |       0.157464 |    2.84502 |
| solution-flask     |     0.502894 |       1.00914  |    4.16463 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524618 |       0.267672 |    16.8346 |
| solution-aron-mark |     0.504167 |       0.265531 |    17.1357 |