# 2026-05-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10177  |       1.1593   |   0.105502 |
| solution-aron-mark |     5.7891   |       0.172153 |   0.229616 |
| solution-pl        |     0.424439 |       0.149395 |   0.230217 |
| solution-1-flask   |     0.433975 |       1.00865  |   0.230412 |
| solution-1         |     7.28713  |       1e-06    |   0.61504  |
| solution-2         |     0.424304 |       0.747111 |   0.775833 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426052 |       0.151567 |   0.354335 |
| solution-aron-mark |     0.428943 |       0.15119  |   0.358125 |
| solution-flask     |     0.42709  |       1.00882  |   0.404748 |
| solution-1-flask   |     0.431323 |       1.00867  |   0.722178 |
| solution-2         |     0.42731  |       0.499448 |   5.55145  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42637  |       0.15869  |    1.05346 |
| solution-pl        |     0.428997 |       0.157365 |    1.05707 |
| solution-flask     |     0.425409 |       1.00849  |    1.67964 |
| solution-1-flask   |     0.425644 |       1.0089   |    5.51582 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42729  |       0.182978 |    3.72025 |
| solution-aron-mark |     0.423495 |       0.182673 |    3.76926 |
| solution-flask     |     0.424838 |       1.00885  |    5.31376 |