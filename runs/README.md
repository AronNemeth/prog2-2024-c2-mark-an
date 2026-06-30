# 2026-06-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08808  |       1.10016  |   0.101553 |
| solution-1-flask   |     0.425681 |       1.00864  |   0.225404 |
| solution-aron-mark |     0.42342  |       0.151623 |   0.226593 |
| solution-pl        |     6.15848  |       0.166577 |   0.22662  |
| solution-1         |     7.29581  |       1e-06    |   0.616433 |
| solution-2         |     0.408874 |       0.662687 |   1.0766   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422895 |       0.151284 |   0.350316 |
| solution-pl        |     0.418497 |       0.150254 |   0.356003 |
| solution-flask     |     0.44357  |       1.00962  |   0.395127 |
| solution-1-flask   |     0.42536  |       1.00871  |   0.719913 |
| solution-2         |     0.417155 |       0.499373 |   4.65549  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419501 |       0.157847 |    1.02737 |
| solution-aron-mark |     0.429555 |       0.159436 |    1.03727 |
| solution-flask     |     0.420157 |       1.00876  |    1.64003 |
| solution-1-flask   |     0.423811 |       1.00893  |    5.59761 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423212 |       0.182143 |    3.74415 |
| solution-aron-mark |     0.423177 |       0.180711 |    3.90878 |
| solution-flask     |     0.425373 |       1.00884  |    5.1509  |