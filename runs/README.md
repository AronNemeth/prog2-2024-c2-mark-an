# 2024-08-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553395 |       1.00887  |   0.092636 |
| solution-pl        |     0.551965 |       0.103467 |   0.171876 |
| solution-aron-mark |     1.77574  |       0.105556 |   0.175232 |
| solution-1-flask   |     1.34493  |       1.09675  |   0.255276 |
| solution-1         |     7.95043  |       1e-06    |   0.676569 |
| solution-2         |     4.7968   |       0.697556 |   0.945362 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555699 |       1.00927  |   0.223277 |
| solution-pl        |     0.554322 |       0.106495 |   0.293206 |
| solution-aron-mark |     0.554454 |       0.10738  |   0.295731 |
| solution-1-flask   |     0.555408 |       1.00915  |   0.780453 |
| solution-2         |     0.553922 |       0.475448 |   7.72345  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549437 |       1.00907  |    0.90871 |
| solution-aron-mark |     0.565658 |       0.111125 |    1.01253 |
| solution-pl        |     0.551123 |       0.112191 |    1.02285 |
| solution-1-flask   |     0.556944 |       1.00894  |    5.48384 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546509 |       1.00949  |    4.1066  |
| solution-pl        |     0.552087 |       0.14319  |    4.22843 |
| solution-aron-mark |     0.550568 |       0.143086 |    4.22901 |