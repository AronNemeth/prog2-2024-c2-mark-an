# 2024-09-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.562732 |       1.00908  |   0.093541 |
| solution-aron-mark |     1.85946  |       0.104032 |   0.171925 |
| solution-pl        |     0.565779 |       0.10486  |   0.178452 |
| solution-1-flask   |     1.1861   |       1.09537  |   0.264479 |
| solution-1         |     7.56196  |       1e-06    |   0.599081 |
| solution-2         |     4.45772  |       0.571895 |   0.973489 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554907 |       1.0092   |   0.225577 |
| solution-aron-mark |     0.55763  |       0.105546 |   0.300706 |
| solution-pl        |     0.556586 |       0.107228 |   0.328814 |
| solution-1-flask   |     0.567549 |       1.00897  |   0.796108 |
| solution-2         |     0.563876 |       0.497586 |   1.78301  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557306 |       1.00914  |   0.895797 |
| solution-pl        |     0.559058 |       0.113315 |   0.997324 |
| solution-aron-mark |     0.562909 |       0.113475 |   1.0024   |
| solution-1-flask   |     0.563422 |       1.00909  |   5.55903  |
| solution-2         |     0.549621 |       0.529526 |  42.1802   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559911 |       1.0095   |    4.11877 |
| solution-aron-mark |     0.557215 |       0.144476 |    4.24896 |
| solution-pl        |     0.55988  |       0.141739 |    4.25467 |