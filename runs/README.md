# 2024-10-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.529979 |       1.0092   |   0.086349 |
| solution-aron-mark |     1.77385  |       0.104289 |   0.179185 |
| solution-pl        |     0.533378 |       0.102222 |   0.179377 |
| solution-1-flask   |     4.83152  |       1.07304  |   0.271455 |
| solution-1         |     7.46901  |       1e-06    |   0.610489 |
| solution-2         |     0.53099  |       0.594089 |   1.1665   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.54019  |       1.00915  |   0.213996 |
| solution-aron-mark |     0.552743 |       0.109552 |   0.311017 |
| solution-pl        |     0.557135 |       0.106863 |   0.311413 |
| solution-1-flask   |     0.555975 |       1.00917  |   0.825881 |
| solution-2         |     0.556909 |       0.513286 |   2.21998  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.54809  |       1.009    |   0.953953 |
| solution-pl        |     0.552373 |       0.116154 |   1.05552  |
| solution-aron-mark |     0.55084  |       0.116112 |   1.0608   |
| solution-1-flask   |     0.55424  |       1.01055  |   5.98607  |
| solution-2         |     0.548364 |       0.549019 |  40.7285   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530199 |       0.140983 |    4.65387 |
| solution-pl        |     0.517625 |       0.141124 |    4.67026 |
| solution-flask     |     0.526852 |       1.00876  |    4.73388 |