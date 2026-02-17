# 2026-02-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.72131  |       1.06315  |   0.107042 |
| solution-aron-mark |     0.449786 |       0.149144 |   0.238597 |
| solution-pl        |     4.9119   |       0.160524 |   0.269786 |
| solution-1-flask   |     0.452721 |       1.00869  |   0.273367 |
| solution-1         |     7.87281  |       1e-06    |   0.637059 |
| solution-2         |     0.44454  |       0.567302 |   0.936148 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.448968 |       0.147609 |   0.374736 |
| solution-pl        |     0.452182 |       0.146504 |   0.375597 |
| solution-flask     |     0.450316 |       1.00882  |   0.396609 |
| solution-1-flask   |     0.468348 |       1.00884  |   0.803497 |
| solution-2         |     0.447238 |       0.516944 |   4.93643  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.450755 |       0.154103 |    1.1563  |
| solution-pl        |     0.454231 |       0.155901 |    1.17325 |
| solution-flask     |     0.450592 |       1.00909  |    1.64408 |
| solution-1-flask   |     0.449468 |       1.0089   |    5.57367 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451787 |       0.179595 |    4.00651 |
| solution-pl        |     0.449845 |       0.180114 |    4.03252 |
| solution-flask     |     0.443601 |       1.00895  |    5.34246 |