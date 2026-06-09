# 2026-06-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.89579  |       1.07556  |   0.092175 |
| solution-pl        |     0.39025  |       0.136997 |   0.207792 |
| solution-aron-mark |     0.392185 |       0.142597 |   0.222816 |
| solution-1-flask   |     0.392612 |       1.00642  |   0.239533 |
| solution-1         |     7.53773  |       1e-06    |   0.584358 |
| solution-2         |     4.32238  |       0.546561 |   0.886579 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.390428 |       0.136813 |   0.316476 |
| solution-pl        |     0.385482 |       0.138124 |   0.325119 |
| solution-flask     |     0.389221 |       1.00665  |   0.407904 |
| solution-1-flask   |     0.389836 |       1.00683  |   0.722137 |
| solution-2         |     0.383388 |       0.477816 |   4.11074  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.384354 |       0.14168  |   0.978418 |
| solution-pl        |     0.391747 |       0.145359 |   0.994172 |
| solution-flask     |     0.383463 |       1.00697  |   1.72707  |
| solution-1-flask   |     0.388702 |       1.00676  |   5.36918  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.387298 |       0.172372 |    4.54645 |
| solution-pl        |     0.3834   |       0.171578 |    4.65956 |
| solution-flask     |     0.383394 |       1.00708  |    5.53824 |