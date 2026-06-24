# 2026-06-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10316  |       1.0555   |   0.110497 |
| solution-pl        |     5.86233  |       0.172067 |   0.238039 |
| solution-aron-mark |     0.436743 |       0.152292 |   0.245111 |
| solution-1-flask   |     0.441138 |       1.0084   |   0.272524 |
| solution-1         |     7.18316  |       1e-06    |   0.659086 |
| solution-2         |     0.414686 |       0.699291 |   1.27724  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432987 |       0.153036 |   0.376673 |
| solution-pl        |     0.437978 |       0.154459 |   0.380301 |
| solution-flask     |     0.429546 |       1.00861  |   0.402854 |
| solution-1-flask   |     0.432163 |       1.00855  |   0.823665 |
| solution-2         |     0.429597 |       0.516434 |   3.24432  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426894 |       0.157367 |    1.13822 |
| solution-aron-mark |     0.43678  |       0.159358 |    1.15571 |
| solution-flask     |     0.429028 |       1.00853  |    1.67921 |
| solution-1-flask   |     0.437383 |       1.00854  |    5.68784 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.437511 |       0.183929 |    4.10207 |
| solution-aron-mark |     0.437237 |       0.182437 |    4.12206 |
| solution-flask     |     0.431826 |       1.00901  |    5.52265 |