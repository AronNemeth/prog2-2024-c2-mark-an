# 2024-08-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.58007  |       1.0094   |   0.080382 |
| solution-aron-mark |     1.8346   |       0.106307 |   0.178942 |
| solution-pl        |     0.581489 |       0.105973 |   0.19964  |
| solution-1-flask   |     1.11381  |       1.06547  |   0.271901 |
| solution-1         |     7.75993  |       1e-06    |   0.605423 |
| solution-2         |     4.49478  |       0.521574 |   0.884694 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.578714 |       1.00938  |   0.235325 |
| solution-aron-mark |     0.58656  |       0.110319 |   0.304866 |
| solution-pl        |     0.578502 |       0.11164  |   0.314544 |
| solution-1-flask   |     0.611311 |       1.00964  |   0.783736 |
| solution-2         |     0.577166 |       0.499596 |  12.2322   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.572044 |       1.00942  |   0.915941 |
| solution-pl        |     0.582136 |       0.11668  |   1.04033  |
| solution-aron-mark |     0.588224 |       0.113944 |   1.05483  |
| solution-1-flask   |     0.591633 |       1.00926  |   5.61151  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.582021 |       1.00904  |    4.48493 |
| solution-pl        |     0.574824 |       0.149138 |    4.56482 |
| solution-aron-mark |     0.592706 |       0.148551 |    4.60657 |