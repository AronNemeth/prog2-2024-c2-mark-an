# 2026-10-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.432172 |       1.00842  |   0.090976 |
| solution-pl        |     0.426451 |       0.166785 |   0.248646 |
| solution-aron-mark |     2.88646  |       0.170646 |   0.253993 |
| solution-1-flask   |     1.44636  |       1.15533  |   0.264699 |
| solution-1         |     8.03374  |       1e-06    |   0.576555 |
| solution-2         |     5.2364   |       0.544108 |   1.7761   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.433586 |       1.00863  |   0.230857 |
| solution-aron-mark |     0.441956 |       0.166037 |   0.383249 |
| solution-pl        |     0.438969 |       0.173756 |   0.383397 |
| solution-1-flask   |     0.436781 |       1.00876  |   0.799812 |
| solution-2         |     0.427465 |       0.50997  |   3.24799  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.424771 |       1.00877  |    1.00425 |
| solution-pl        |     0.440706 |       0.177545 |    1.12327 |
| solution-aron-mark |     0.427742 |       0.177183 |    1.12455 |
| solution-1-flask   |     0.439684 |       1.00909  |    5.53614 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429821 |       0.210495 |    3.58846 |
| solution-pl        |     0.439693 |       0.208054 |    3.65161 |
| solution-flask     |     0.451418 |       1.00904  |    4.40542 |