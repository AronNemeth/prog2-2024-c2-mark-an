# 2026-05-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12214  |       1.09371  |   0.103565 |
| solution-pl        |     0.428719 |       0.145994 |   0.223493 |
| solution-1-flask   |     0.427528 |       1.00873  |   0.225838 |
| solution-aron-mark |     6.09931  |       0.257287 |   0.226803 |
| solution-1         |     7.68867  |       1e-06    |   0.555273 |
| solution-2         |     0.421569 |       0.597315 |   1.03373  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422801 |       0.146784 |   0.349636 |
| solution-aron-mark |     0.42096  |       0.145597 |   0.382353 |
| solution-flask     |     0.424356 |       1.00863  |   0.403652 |
| solution-1-flask   |     0.426751 |       1.00869  |   0.718868 |
| solution-2         |     0.421368 |       0.49236  |   3.22856  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427841 |       0.152001 |    1.05182 |
| solution-aron-mark |     0.422623 |       0.151465 |    1.05556 |
| solution-flask     |     0.425448 |       1.00882  |    1.67927 |
| solution-1-flask   |     0.424709 |       1.00885  |    5.51476 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.419658 |       0.178916 |    3.7163  |
| solution-pl        |     0.421673 |       0.175724 |    3.7245  |
| solution-flask     |     0.423038 |       1.00875  |    5.22305 |