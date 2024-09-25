# 2024-09-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11753  |       1.09402  |   0.099367 |
| solution-pl        |     0.594945 |       0.105512 |   0.181877 |
| solution-aron-mark |     1.8375   |       0.103128 |   0.182161 |
| solution-1-flask   |     0.58946  |       1.00816  |   0.258684 |
| solution-1         |     7.51668  |       1e-06    |   0.606799 |
| solution-2         |     4.36686  |       0.557104 |   1.26704  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.577681 |       1.00812  |   0.205984 |
| solution-aron-mark |     0.572108 |       0.104603 |   0.311317 |
| solution-pl        |     0.558881 |       0.104418 |   0.312877 |
| solution-1-flask   |     0.584155 |       1.00823  |   0.770436 |
| solution-2         |     0.569317 |       0.488288 |  12.549    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566289 |       1.0084   |   0.947462 |
| solution-aron-mark |     0.555274 |       0.110573 |   1.08708  |
| solution-pl        |     0.557548 |       0.110183 |   1.09072  |
| solution-1-flask   |     0.574098 |       1.0082   |   5.52428  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.567551 |       0.139124 |    4.63011 |
| solution-aron-mark |     0.559802 |       0.138607 |    4.70002 |
| solution-flask     |     0.580392 |       1.00854  |    4.92982 |