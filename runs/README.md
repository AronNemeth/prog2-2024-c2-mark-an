# 2025-08-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.92091  |       1.03922  |   0.098281 |
| solution-pl        |     0.48921  |       0.152413 |   0.237455 |
| solution-aron-mark |     4.86252  |       0.152411 |   0.237511 |
| solution-1-flask   |     0.509805 |       1.00821  |   0.266628 |
| solution-2         |     0.486881 |       0.799731 |   0.853136 |
| solution-1         |     8.58476  |       1e-06    |   0.888224 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494537 |       0.162584 |   0.366103 |
| solution-flask     |     0.488338 |       1.00871  |   0.367189 |
| solution-aron-mark |     0.485612 |       0.152092 |   0.401677 |
| solution-1-flask   |     0.501573 |       1.00864  |   0.803516 |
| solution-2         |     0.488999 |       0.511239 |   3.79518  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489886 |       0.159004 |    1.0548  |
| solution-pl        |     0.481215 |       0.159629 |    1.05556 |
| solution-flask     |     0.482799 |       1.00849  |    1.57628 |
| solution-1-flask   |     0.492288 |       1.00861  |    5.75447 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482303 |        0.19266 |    3.19055 |
| solution-pl        |     0.478903 |        0.19366 |    3.27164 |
| solution-flask     |     0.492513 |        1.00831 |    5.07491 |