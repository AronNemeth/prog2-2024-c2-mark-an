# 2024-12-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.93858  |       1.00907  |   0.107261 |
| solution-aron-mark |     0.557869 |       0.11035  |   0.185135 |
| solution-pl        |     0.560338 |       0.111615 |   0.18767  |
| solution-1-flask   |     5.08522  |       1.16613  |   0.268838 |
| solution-1         |     7.504    |       1e-06    |   0.615242 |
| solution-2         |     0.584359 |       0.52756  |   1.25505  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.571178 |       0.120458 |   0.324901 |
| solution-pl        |     0.567209 |       0.116061 |   0.336766 |
| solution-flask     |     0.572593 |       1.00881  |   0.508856 |
| solution-1-flask   |     0.566519 |       1.00918  |   0.8209   |
| solution-2         |     0.595186 |       0.519842 |  14.5638   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.56009  |       0.123379 |    1.08826 |
| solution-aron-mark |     0.552362 |       0.122323 |    1.09003 |
| solution-flask     |     0.583758 |       1.00931  |    2.35129 |
| solution-1-flask   |     0.603876 |       1.00958  |    6.12019 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.552128 |       0.14605  |    4.68557 |
| solution-aron-mark |     0.571127 |       0.153396 |    4.92659 |
| solution-flask     |     0.56946  |       1.00921  |    9.50045 |