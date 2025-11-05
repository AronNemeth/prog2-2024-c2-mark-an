# 2025-11-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.6115   |       1.06404  |   0.093282 |
| solution-pl        |     0.437696 |       0.150001 |   0.22755  |
| solution-aron-mark |     0.441513 |       0.150099 |   0.228584 |
| solution-1-flask   |     0.449288 |       1.00693  |   0.239992 |
| solution-2         |     4.54854  |       0.690001 |   0.905918 |
| solution-1         |     7.41843  |       2e-06    |   0.945331 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442036 |       0.15611  |   0.33636  |
| solution-pl        |     0.445523 |       0.150853 |   0.339436 |
| solution-flask     |     0.442744 |       1.00693  |   0.401012 |
| solution-1-flask   |     0.460982 |       1.0069   |   0.718791 |
| solution-2         |     0.437061 |       0.501835 |  10.7967   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.450614 |       0.159071 |   0.956537 |
| solution-aron-mark |     0.446236 |       0.160473 |   0.97668  |
| solution-flask     |     0.445248 |       1.00745  |   1.69413  |
| solution-1-flask   |     0.446832 |       1.00688  |   5.46897  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444416 |       0.188753 |    3.94916 |
| solution-aron-mark |     0.438826 |       0.197205 |    3.95595 |
| solution-flask     |     0.441167 |       1.00683  |    5.68981 |