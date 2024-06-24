# 2024-06-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.739671 |       1.01067  |   0.080483 |
| solution-pl        |     0.743182 |       0.117747 |   0.178066 |
| solution-aron-mark |     6.49408  |       0.111913 |   0.186668 |
| solution-1-flask   |     1.47311  |       1.16329  |   0.280387 |
| solution-1         |     8.72287  |       1e-06    |   0.648027 |
| solution-2         |     0.736886 |       0.566592 |   1.1749   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.771226 |       1.0103   |   0.180102 |
| solution-pl        |     0.737058 |       0.112976 |   0.2718   |
| solution-aron-mark |     0.734198 |       0.123154 |   0.280664 |
| solution-1-flask   |     0.758261 |       1.01035  |   0.823408 |
| solution-2         |     0.753783 |       0.508302 |  13.8139   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.73258  |       1.01015  |   0.792972 |
| solution-pl        |     0.74463  |       0.130854 |   0.893656 |
| solution-aron-mark |     0.72945  |       0.13682  |   0.91253  |
| solution-1-flask   |     0.778358 |       1.01034  |   5.98076  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.749175 |       1.01054  |    2.85548 |
| solution-pl        |     0.734776 |       0.172856 |    2.95126 |
| solution-aron-mark |     0.72842  |       0.166198 |    3.00795 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.760393 |       1.01149  |    24.199  |
| solution-pl    |     0.716307 |       0.310667 |    31.6426 |