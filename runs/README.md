# 2025-01-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.98147  |       1.00925  |   0.088948 |
| solution-aron-mark |     0.580433 |       0.118419 |   0.186469 |
| solution-pl        |     0.581867 |       0.122022 |   0.189993 |
| solution-1-flask   |     5.66361  |       1.13616  |   0.29332  |
| solution-1         |     8.20569  |       1e-06    |   0.70449  |
| solution-2         |     0.58357  |       0.564119 |   0.954137 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.563566 |       0.118734 |   0.306657 |
| solution-pl        |     0.574518 |       0.12183  |   0.314332 |
| solution-flask     |     0.565346 |       1.00908  |   0.316797 |
| solution-1-flask   |     0.581769 |       1.00909  |   0.842656 |
| solution-2         |     0.564432 |       0.530465 |   3.80864  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.556456 |       0.12313  |   0.897542 |
| solution-pl        |     0.545182 |       0.123641 |   0.921419 |
| solution-flask     |     0.555852 |       1.00915  |   1.32757  |
| solution-1-flask   |     0.581378 |       1.0091   |   5.88626  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.554641 |       0.158592 |    3.00625 |
| solution-pl        |     0.560993 |       0.15896  |    3.01213 |
| solution-flask     |     0.554541 |       1.00929  |    4.54698 |