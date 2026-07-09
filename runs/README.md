# 2026-07-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.33118  |       1.0861   |   0.107708 |
| solution-pl        |     6.57295  |       0.154346 |   0.235796 |
| solution-aron-mark |     0.474786 |       0.158135 |   0.246871 |
| solution-1-flask   |     0.440096 |       1.00836  |   0.272475 |
| solution-1         |     9.60371  |       1e-06    |   0.744486 |
| solution-2         |     0.412947 |       0.646143 |   1.17255  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427172 |       0.149294 |   0.371737 |
| solution-pl        |     0.46214  |       0.160141 |   0.376506 |
| solution-flask     |     0.443154 |       1.00873  |   0.402477 |
| solution-1-flask   |     0.426514 |       1.00857  |   0.800253 |
| solution-2         |     0.446678 |       0.518128 |   4.26783  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422542 |       0.164561 |    1.12885 |
| solution-pl        |     0.430949 |       0.160102 |    1.13438 |
| solution-flask     |     0.432344 |       1.00853  |    1.68416 |
| solution-1-flask   |     0.427669 |       1.00845  |    5.71765 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42134  |       0.186679 |    3.97158 |
| solution-aron-mark |     0.422695 |       0.180522 |    4.01532 |
| solution-flask     |     0.428755 |       1.00872  |    5.34152 |