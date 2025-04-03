# 2025-04-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554268 |       1.00881  |   0.093659 |
| solution-aron-mark |     1.86524  |       0.128165 |   0.194087 |
| solution-pl        |     0.541713 |       0.129921 |   0.19782  |
| solution-1-flask   |     5.1784   |       1.11909  |   0.26581  |
| solution-1         |     7.59317  |       1e-06    |   0.639097 |
| solution-2         |     0.557689 |       0.64045  |   0.942094 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.559357 |       0.128162 |   0.29926  |
| solution-flask     |     0.535437 |       1.00912  |   0.3054   |
| solution-aron-mark |     0.561394 |       0.130199 |   0.308844 |
| solution-1-flask   |     0.573437 |       1.00927  |   0.827475 |
| solution-2         |     0.554971 |       0.561008 |   2.82054  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.541229 |       0.134339 |   0.904237 |
| solution-pl        |     0.543057 |       0.134661 |   0.917649 |
| solution-flask     |     0.534289 |       1.0093   |   1.26654  |
| solution-1-flask   |     0.557408 |       1.00967  |   5.95693  |
| solution-2         |     0.5538   |       0.583055 |  31.6774   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.540165 |       0.164453 |    3.01351 |
| solution-pl        |     0.539528 |       0.165585 |    3.0812  |
| solution-flask     |     0.530514 |       1.0093   |    4.49099 |