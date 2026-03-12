# 2026-03-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.98674  |       1.06605  |   0.11482  |
| solution-aron-mark |     0.459581 |       0.155849 |   0.243785 |
| solution-pl        |     4.6376   |       0.156962 |   0.253308 |
| solution-1-flask   |     0.464818 |       1.00925  |   0.276069 |
| solution-2         |     0.456927 |       1.01601  |   0.961029 |
| solution-1         |     7.56738  |       1e-06    |   0.990792 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.454417 |       0.151377 |   0.376424 |
| solution-pl        |     0.451066 |       0.150461 |   0.388546 |
| solution-flask     |     0.449517 |       1.00917  |   0.394239 |
| solution-1-flask   |     0.464804 |       1.00888  |   0.807642 |
| solution-2         |     0.451075 |       0.511469 |   4.90158  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447947 |       0.157969 |    1.1469  |
| solution-pl        |     0.453679 |       0.156824 |    1.1632  |
| solution-flask     |     0.45017  |       1.00947  |    1.65867 |
| solution-1-flask   |     0.452769 |       1.00929  |    5.67215 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452541 |       0.182361 |    4.06175 |
| solution-aron-mark |     0.454165 |       0.182586 |    4.09378 |
| solution-flask     |     0.450732 |       1.00951  |    5.29665 |