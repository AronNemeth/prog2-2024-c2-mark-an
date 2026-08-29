# 2026-08-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.10508  |       1.04438  |   0.097344 |
| solution-1-flask   |     0.429807 |       1.00891  |   0.22955  |
| solution-pl        |     0.426634 |       0.153814 |   0.230842 |
| solution-aron-mark |     4.76563  |       0.15513  |   0.234111 |
| solution-1         |     7.99655  |       1e-06    |   0.605726 |
| solution-2         |     0.428156 |       0.596785 |   0.985385 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.458092 |       0.159042 |   0.35382  |
| solution-aron-mark |     0.425766 |       0.157924 |   0.355094 |
| solution-flask     |     0.427459 |       1.00907  |   0.376362 |
| solution-1-flask   |     0.427241 |       1.00913  |   0.712387 |
| solution-2         |     0.425328 |       0.50476  |  12.9411   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424429 |       0.164376 |    1.026   |
| solution-pl        |     0.426213 |       0.165304 |    1.03862 |
| solution-flask     |     0.424008 |       1.00918  |    1.60295 |
| solution-1-flask   |     0.428487 |       1.00923  |    5.64355 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422244 |       0.186878 |    3.42584 |
| solution-aron-mark |     0.425838 |       0.190008 |    3.43151 |
| solution-flask     |     0.424904 |       1.00911  |    5.14842 |