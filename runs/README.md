# 2026-11-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.286938 |       1.00944  |   0.04649  |
| solution-1-flask   |     1.01795  |       1.04813  |   0.136792 |
| solution-pl        |     4.46414  |       0.111771 |   0.143651 |
| solution-aron-mark |     0.284769 |       0.108478 |   0.145165 |
| solution-1         |     5.05894  |       1e-06    |   0.370119 |
| solution-2         |     0.285744 |       0.391591 |   0.691069 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.283551 |       1.00925  |   0.108001 |
| solution-pl        |     0.298436 |       0.11187  |   0.205894 |
| solution-aron-mark |     0.295399 |       0.116563 |   0.209869 |
| solution-1-flask   |     0.283847 |       1.00922  |   0.371236 |
| solution-2         |     0.291842 |       0.371331 |   1.24153  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.328883 |       1.00975  |   0.469942 |
| solution-aron-mark |     0.300209 |       0.122793 |   0.554765 |
| solution-pl        |     0.29196  |       0.124754 |   0.555183 |
| solution-1-flask   |     0.307795 |       1.00973  |   2.83728  |
| solution-2         |     0.292482 |       0.382865 | 157.049    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.31274  |       0.144176 |    1.90428 |
| solution-aron-mark |     0.285563 |       0.183595 |    1.92707 |
| solution-flask     |     0.295216 |       1.0185   |    2.35593 |
| solution-1-flask   |     0.292121 |       1.00923  |   26.3476  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.296069 |       0.204082 |    13.1597 |
| solution-pl        |     0.302533 |       0.206629 |    14.5774 |
| solution-flask     |     0.265981 |       1.00901  |    16.0061 |