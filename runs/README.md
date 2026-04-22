# 2026-04-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68261  |       1.06074  |   0.102424 |
| solution-pl        |     4.77392  |       0.146303 |   0.228276 |
| solution-aron-mark |     0.422206 |       0.148819 |   0.229092 |
| solution-1-flask   |     0.432464 |       1.00813  |   0.262701 |
| solution-1         |     7.93778  |       1e-06    |   0.882889 |
| solution-2         |     0.413391 |       0.647532 |   1.17496  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.418256 |       0.147399 |   0.35918  |
| solution-aron-mark |     0.416029 |       0.147724 |   0.36001  |
| solution-flask     |     0.423028 |       1.00955  |   0.388458 |
| solution-1-flask   |     0.433002 |       1.00809  |   0.804415 |
| solution-2         |     0.411937 |       0.523394 |  13.7102   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415929 |       0.155307 |    1.07013 |
| solution-aron-mark |     0.421913 |       0.156024 |    1.08424 |
| solution-flask     |     0.415722 |       1.00822  |    1.6401  |
| solution-1-flask   |     0.425533 |       1.0087   |    5.61235 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42474  |       0.178206 |    3.87492 |
| solution-pl        |     0.426159 |       0.179033 |    3.88074 |
| solution-flask     |     0.429728 |       1.00823  |    5.30407 |