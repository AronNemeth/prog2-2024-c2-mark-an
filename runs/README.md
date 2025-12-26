# 2025-12-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8956   |       1.07676  |   0.095924 |
| solution-pl        |     0.468551 |       0.160388 |   0.241863 |
| solution-aron-mark |     0.481446 |       0.160501 |   0.242378 |
| solution-1-flask   |     0.47776  |       1.00836  |   0.264405 |
| solution-1         |     8.36574  |       1e-06    |   0.864935 |
| solution-2         |     5.29377  |       0.740072 |   1.45353  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478015 |       0.163262 |   0.367204 |
| solution-pl        |     0.468131 |       0.160395 |   0.367755 |
| solution-flask     |     0.462632 |       1.00842  |   0.380557 |
| solution-1-flask   |     0.474798 |       1.00831  |   0.777303 |
| solution-2         |     0.463094 |       0.501575 |  16.0028   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465178 |       0.166916 |    1.07013 |
| solution-aron-mark |     0.466979 |       0.170424 |    1.08652 |
| solution-flask     |     0.462971 |       1.00814  |    1.57436 |
| solution-1-flask   |     0.470501 |       1.00839  |    5.49784 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.468665 |       0.193168 |    3.5051  |
| solution-aron-mark |     0.46915  |       0.190037 |    3.50598 |
| solution-flask     |     0.470236 |       1.00884  |    5.05487 |