# 2024-11-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0908   |       1.12876  |   0.109845 |
| solution-aron-mark |     0.54724  |       0.106777 |   0.173392 |
| solution-pl        |     6.12239  |       0.108958 |   0.176151 |
| solution-1-flask   |     0.558535 |       1.00904  |   0.259694 |
| solution-1         |     7.91555  |       1e-06    |   0.814622 |
| solution-2         |     0.789004 |       0.716871 |   1.12866  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553653 |       0.10985  |   0.297953 |
| solution-aron-mark |     0.551401 |       0.107824 |   0.335491 |
| solution-flask     |     0.550585 |       1.00935  |   0.487132 |
| solution-1-flask   |     0.559899 |       1.009    |   0.779    |
| solution-2         |     0.551104 |       0.467349 |   2.08516  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.554512 |       0.115805 |    1.0139  |
| solution-pl        |     0.554008 |       0.115983 |    1.0511  |
| solution-flask     |     0.559042 |       1.00914  |    2.15493 |
| solution-1-flask   |     0.556637 |       1.00901  |    5.38436 |
| solution-2         |     0.558949 |       0.535764 |  164.478   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.551839 |       0.145528 |    4.29134 |
| solution-pl        |     0.559534 |       0.14341  |    4.34065 |
| solution-flask     |     0.555128 |       1.00925  |    8.53135 |