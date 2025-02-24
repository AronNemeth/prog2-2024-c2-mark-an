# 2025-02-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535866 |       1.00875  |   0.080648 |
| solution-aron-mark |     0.530828 |       0.140427 |   0.204137 |
| solution-pl        |     1.97906  |       0.191907 |   0.206019 |
| solution-1-flask   |     5.44152  |       1.03678  |   0.263155 |
| solution-1         |     7.58498  |       1e-06    |   0.731701 |
| solution-2         |     0.534806 |       0.675833 |   1.21492  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.533438 |       1.00917  |   0.298653 |
| solution-pl        |     0.537434 |       0.145242 |   0.309779 |
| solution-aron-mark |     0.545686 |       0.146037 |   0.310699 |
| solution-1-flask   |     0.541395 |       1.00895  |   0.811237 |
| solution-2         |     0.5427   |       0.501594 |   2.80917  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541136 |       0.14896  |   0.91083  |
| solution-aron-mark |     0.54231  |       0.148723 |   0.914661 |
| solution-flask     |     0.548342 |       1.00922  |   1.23551  |
| solution-1-flask   |     0.539334 |       1.009    |   5.7346   |
| solution-2         |     0.540529 |       0.557286 |  36.9818   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.583368 |       0.178985 |    2.83898 |
| solution-pl        |     0.539508 |       0.178795 |    2.86596 |
| solution-flask     |     0.535025 |       1.00904  |    4.22757 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.551229 |        0.27684 |    16.565  |
| solution-aron-mark |     0.5327   |        0.27614 |    16.8501 |