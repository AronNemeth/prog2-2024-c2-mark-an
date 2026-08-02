# 2026-08-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.99902  |       1.00897  |   0.099994 |
| solution-1-flask   |     1.3339   |       1.05735  |   0.230276 |
| solution-aron-mark |     0.42638  |       0.152917 |   0.231927 |
| solution-pl        |     0.431761 |       0.153553 |   0.234052 |
| solution-1         |    10.0844   |       1e-06    |   0.622024 |
| solution-2         |     5.09178  |       0.696393 |   0.865187 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430406 |       0.154446 |   0.359272 |
| solution-pl        |     0.429435 |       0.156962 |   0.362875 |
| solution-flask     |     0.427636 |       1.00918  |   0.404483 |
| solution-1-flask   |     0.428381 |       1.00898  |   0.720962 |
| solution-2         |     0.42573  |       0.493535 |   4.79967  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422714 |       0.159043 |    1.05019 |
| solution-aron-mark |     0.443087 |       0.160186 |    1.05548 |
| solution-flask     |     0.434059 |       1.00921  |    1.63614 |
| solution-1-flask   |     0.434082 |       1.00917  |    5.6216  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426334 |       0.184414 |    3.4895  |
| solution-aron-mark |     0.425613 |       0.186917 |    3.51621 |
| solution-flask     |     0.424446 |       1.00922  |    5.20397 |