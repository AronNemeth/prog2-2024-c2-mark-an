# 2026-09-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23295  |       1.04957  |   0.101752 |
| solution-pl        |     2.30491  |       0.166995 |   0.231614 |
| solution-aron-mark |     0.417633 |       0.155604 |   0.233868 |
| solution-1-flask   |     0.436489 |       1.00884  |   0.237811 |
| solution-1         |     8.69504  |       1e-06    |   0.673852 |
| solution-2         |     4.6896   |       0.704757 |   0.923549 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.419481 |       0.153871 |   0.3521   |
| solution-pl        |     0.425804 |       0.155088 |   0.357065 |
| solution-flask     |     0.425685 |       1.00897  |   0.395478 |
| solution-1-flask   |     0.427609 |       1.00892  |   0.735927 |
| solution-2         |     0.423778 |       0.49709  |   2.41511  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.421255 |       0.160484 |    1.02463 |
| solution-aron-mark |     0.420393 |       0.159387 |    1.03438 |
| solution-flask     |     0.421025 |       1.00902  |    1.61669 |
| solution-1-flask   |     0.429634 |       1.00934  |    5.60481 |
| solution-2         |     0.42739  |       0.592372 |  191.441   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420046 |       0.184637 |    3.43557 |
| solution-pl        |     0.424132 |       0.184626 |    3.44344 |
| solution-flask     |     0.417954 |       1.00916  |    5.07432 |