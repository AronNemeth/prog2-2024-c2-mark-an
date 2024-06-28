# 2024-06-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.519193 |       1.00905  |   0.073972 |
| solution-pl        |     0.515195 |       0.104547 |   0.163733 |
| solution-aron-mark |     5.9166   |       0.106664 |   0.164142 |
| solution-1-flask   |     1.25982  |       1.12909  |   0.255588 |
| solution-1         |     8.07144  |       1e-06    |   0.591382 |
| solution-2         |     0.49701  |       0.531383 |   1.90436  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.513245 |       1.00896  |   0.160104 |
| solution-pl        |     0.530754 |       0.106204 |   0.260657 |
| solution-aron-mark |     0.509751 |       0.105812 |   0.263085 |
| solution-1-flask   |     0.531404 |       1.00966  |   0.797141 |
| solution-2         |     0.509351 |       0.487606 |   5.26058  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.527115 |       1.0088   |   0.716719 |
| solution-aron-mark |     0.519144 |       0.116385 |   0.806066 |
| solution-pl        |     0.526952 |       0.117737 |   0.813702 |
| solution-1-flask   |     0.534024 |       1.00956  |   5.67056  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.510094 |       1.00928  |    2.55608 |
| solution-pl        |     0.506574 |       0.150734 |    2.69842 |
| solution-aron-mark |     0.536787 |       0.149904 |    2.70366 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.516119 |       1.00917  |    17.1315 |
| solution-aron-mark |     0.510381 |       0.277294 |    22.2418 |
| solution-pl        |     0.500156 |       0.2778   |    23.7312 |