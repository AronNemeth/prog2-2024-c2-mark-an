# 2024-11-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27743  |       1.11023  |   0.115482 |
| solution-pl        |     6.1208   |       0.113053 |   0.189402 |
| solution-aron-mark |     0.593285 |       0.120043 |   0.200867 |
| solution-1-flask   |     0.612139 |       1.00925  |   0.265352 |
| solution-2         |     0.592971 |       0.74533  |   0.888392 |
| solution-1         |     8.30611  |       1e-06    |   0.950753 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.597351 |       0.11342  |   0.308534 |
| solution-aron-mark |     0.598493 |       0.111566 |   0.310867 |
| solution-flask     |     0.596636 |       1.00948  |   0.500361 |
| solution-1-flask   |     0.612081 |       1.00979  |   0.808161 |
| solution-2         |     0.608682 |       0.536585 |   9.53239  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.595196 |       0.122999 |    1.03333 |
| solution-aron-mark |     0.605637 |       0.12519  |    1.03389 |
| solution-flask     |     0.639604 |       1.00992  |    2.21701 |
| solution-1-flask   |     0.612015 |       1.01017  |    5.67301 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.599325 |       0.144619 |    4.65398 |
| solution-pl        |     0.608731 |       0.153006 |    4.84344 |
| solution-flask     |     0.583436 |       1.00919  |    9.30194 |