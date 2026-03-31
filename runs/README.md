# 2026-03-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.98742  |       1.07605  |   0.102679 |
| solution-pl        |     4.77938  |       0.150523 |   0.228664 |
| solution-aron-mark |     0.544132 |       0.147454 |   0.235358 |
| solution-1-flask   |     0.425357 |       1.00823  |   0.262184 |
| solution-1         |     7.751    |       1e-06    |   0.699095 |
| solution-2         |     0.421363 |       0.652326 |   1.46006  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.41309  |       0.147763 |   0.36491  |
| solution-aron-mark |     0.4205   |       0.17853  |   0.376033 |
| solution-flask     |     0.418469 |       1.00841  |   0.396911 |
| solution-1-flask   |     0.418061 |       1.00835  |   0.791162 |
| solution-2         |     0.409535 |       0.507257 |   2.36463  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.413135 |       0.154663 |    1.11755 |
| solution-pl        |     0.417276 |       0.152638 |    1.12023 |
| solution-flask     |     0.414682 |       1.00836  |    1.6063  |
| solution-1-flask   |     0.433282 |       1.00881  |    5.70274 |
| solution-2         |     0.409422 |       0.578813 |  177.46    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432903 |       0.182196 |    3.95502 |
| solution-pl        |     0.435709 |       0.183506 |    4.06173 |
| solution-flask     |     0.432225 |       1.00846  |    5.37509 |