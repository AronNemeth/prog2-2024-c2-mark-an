# 2025-04-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12238  |       1.18748  |   0.102352 |
| solution-aron-mark |     0.53601  |       0.120108 |   0.187607 |
| solution-pl        |     5.57603  |       0.122594 |   0.187942 |
| solution-1-flask   |     0.523412 |       1.0087   |   0.265754 |
| solution-1         |     7.36002  |       1e-06    |   0.596229 |
| solution-2         |     0.509249 |       0.566038 |   0.990559 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.52215  |       0.122342 |   0.295164 |
| solution-aron-mark |     0.51313  |       0.124633 |   0.296736 |
| solution-flask     |     0.52676  |       1.00865  |   0.304588 |
| solution-1-flask   |     0.512249 |       1.00894  |   0.781147 |
| solution-2         |     0.508106 |       0.504221 |   3.18858  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.508536 |       0.128399 |   0.89926  |
| solution-aron-mark |     0.511382 |       0.128024 |   0.903981 |
| solution-flask     |     0.517913 |       1.009    |   1.21668  |
| solution-1-flask   |     0.51089  |       1.0085   |   5.46029  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.508622 |       0.160754 |    2.80767 |
| solution-aron-mark |     0.504063 |       0.161397 |    2.82415 |
| solution-flask     |     0.506053 |       1.00882  |    4.25247 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505661 |       0.267027 |    16.0539 |
| solution-pl        |     0.509259 |       0.271385 |    16.324  |