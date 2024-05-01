# 2024-05-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.721565 |       1.00917  |   0.078641 |
| solution-pl        |     6.57015  |       0.174688 |   0.1875   |
| solution-aron-mark |     0.710601 |       0.12501  |   0.187643 |
| solution-1-flask   |     1.64286  |       1.08157  |   0.274779 |
| solution-1         |     9.05528  |       2e-06    |   0.664559 |
| solution-2         |     0.715439 |       0.473516 |   0.769629 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.693192 |       1.00914  |   0.1686   |
| solution-pl        |     0.728185 |       0.135763 |   0.286307 |
| solution-aron-mark |     0.703162 |       0.129692 |   0.288033 |
| solution-1-flask   |     0.747443 |       1.00904  |   0.838024 |
| solution-2         |     0.738675 |       0.490259 |  12.3791   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685208 |       1.00906  |   0.718498 |
| solution-aron-mark |     0.703861 |       0.135271 |   0.827899 |
| solution-pl        |     0.674474 |       0.133234 |   0.839    |
| solution-1-flask   |     0.72313  |       1.0098   |   5.7994   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.694417 |       1.00957  |    2.67378 |
| solution-aron-mark |     0.717849 |       0.173892 |    2.77042 |
| solution-pl        |     0.683391 |       0.174547 |    2.7959  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.690143 |       1.0094   |    18.8244 |
| solution-aron-mark |     0.703916 |       0.328082 |    20.677  |
| solution-pl        |     0.689908 |       0.34021  |    21.8864 |