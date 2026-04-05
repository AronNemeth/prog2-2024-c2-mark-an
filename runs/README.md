# 2026-04-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.0017   |       1.05602  |   0.107544 |
| solution-pl        |     4.93015  |       0.152101 |   0.242133 |
| solution-aron-mark |     0.445763 |       0.156637 |   0.246377 |
| solution-1-flask   |     0.440055 |       1.00852  |   0.27049  |
| solution-1         |     8.00208  |       1e-06    |   0.710655 |
| solution-2         |     0.445185 |       0.699929 |   1.71503  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.440709 |       0.153313 |   0.3799   |
| solution-flask     |     0.435241 |       1.00869  |   0.389072 |
| solution-pl        |     0.417831 |       0.169467 |   0.397965 |
| solution-1-flask   |     0.448143 |       1.00906  |   0.82665  |
| solution-2         |     0.429462 |       0.567527 |   2.97826  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431392 |       0.167187 |    1.14551 |
| solution-aron-mark |     0.427368 |       0.160251 |    1.17382 |
| solution-flask     |     0.447716 |       1.00875  |    1.61094 |
| solution-1-flask   |     0.428167 |       1.00867  |    5.75884 |
| solution-2         |     0.420629 |       0.585693 |  164.948   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.417825 |       0.181115 |    4.2029  |
| solution-pl        |     0.417333 |       0.185609 |    4.23099 |
| solution-flask     |     0.432996 |       1.0084   |    5.31524 |