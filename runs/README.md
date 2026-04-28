# 2026-04-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.91001  |       1.08299  |   0.093492 |
| solution-aron-mark |     4.30855  |       0.133348 |   0.208004 |
| solution-pl        |     0.377759 |       0.133308 |   0.20912  |
| solution-1-flask   |     0.375515 |       1.00687  |   0.238412 |
| solution-2         |     0.38453  |       0.734926 |   0.636783 |
| solution-1         |     6.92837  |       1e-06    |   0.836504 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.38195  |       0.135408 |   0.320942 |
| solution-aron-mark |     0.382404 |       0.137176 |   0.337949 |
| solution-flask     |     0.384938 |       1.00613  |   0.409557 |
| solution-1-flask   |     0.388728 |       1.00707  |   0.725531 |
| solution-2         |     0.379256 |       0.498496 |   8.90766  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.379783 |       0.139802 |    1.01157 |
| solution-aron-mark |     0.379112 |       0.141758 |    1.02998 |
| solution-flask     |     0.380349 |       1.00629  |    1.75322 |
| solution-1-flask   |     0.387931 |       1.00704  |    5.49595 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.378839 |       0.168346 |    4.76497 |
| solution-pl        |     0.393366 |       0.169441 |    4.87034 |
| solution-flask     |     0.376827 |       1.00629  |    5.79285 |