# 2024-06-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.45002  |       1.11196  |   0.06654  |
| solution-pl        |     0.664031 |       0.105921 |   0.163428 |
| solution-aron-mark |     5.99812  |       0.105734 |   0.163558 |
| solution-1-flask   |     0.679394 |       1.00882  |   0.261674 |
| solution-1         |     8.45746  |       2e-06    |   0.668586 |
| solution-2         |     0.673262 |       0.430166 |   1.42341  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.690809 |       1.00903  |   0.161247 |
| solution-aron-mark |     0.74809  |       0.106997 |   0.258528 |
| solution-pl        |     0.685399 |       0.105409 |   0.261973 |
| solution-1-flask   |     0.702826 |       1.00898  |   0.796806 |
| solution-2         |     0.681465 |       0.448599 |   3.37242  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.680654 |       1.00921  |   0.713596 |
| solution-aron-mark |     0.671021 |       0.116409 |   0.814211 |
| solution-pl        |     0.672993 |       0.122054 |   0.815839 |
| solution-1-flask   |     0.675921 |       1.00922  |   5.70871  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.686887 |       1.00919  |    2.5538  |
| solution-pl        |     0.682562 |       0.149448 |    2.72053 |
| solution-aron-mark |     0.676604 |       0.182826 |    2.75078 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674306 |       1.00941  |    16.8823 |
| solution-pl        |     0.66787  |       0.285554 |    21.1344 |
| solution-aron-mark |     0.679565 |       0.284036 |    21.7114 |