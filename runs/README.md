# 2026-08-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     4.03704  |       1.11868  |   0.111981 |
| solution-pl        |     0.450681 |       0.152359 |   0.238864 |
| solution-aron-mark |     4.56098  |       0.150429 |   0.239771 |
| solution-1-flask   |     0.43083  |       1.00821  |   0.26821  |
| solution-1         |     7.42029  |       1e-06    |   0.682333 |
| solution-2         |     0.429948 |       0.9033   |   0.748667 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.424729 |       0.151487 |   0.377633 |
| solution-aron-mark |     0.434022 |       0.153748 |   0.382878 |
| solution-flask     |     0.436795 |       1.00852  |   0.399151 |
| solution-1-flask   |     0.442345 |       1.0086   |   0.802096 |
| solution-2         |     0.429529 |       0.501966 |   5.45328  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442838 |       0.160002 |    1.13974 |
| solution-pl        |     0.447721 |       0.16294  |    1.15343 |
| solution-flask     |     0.451789 |       1.00875  |    1.67265 |
| solution-1-flask   |     0.43945  |       1.00854  |    5.70483 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.460607 |       0.187591 |    3.8383  |
| solution-aron-mark |     0.471833 |       0.191468 |    3.85453 |
| solution-flask     |     0.481972 |       1.00857  |    5.62773 |