# 2026-04-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.42176  |       1.06605  |   0.124587 |
| solution-pl        |     4.36687  |       0.145237 |   0.229246 |
| solution-aron-mark |     0.409277 |       0.143673 |   0.230097 |
| solution-1-flask   |     0.416051 |       1.00812  |   0.268022 |
| solution-1         |     7.63976  |       2e-06    |   0.761172 |
| solution-2         |     0.409397 |       0.594618 |   1.10318  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.404979 |       0.152406 |   0.364969 |
| solution-pl        |     0.408096 |       0.149126 |   0.368442 |
| solution-flask     |     0.408188 |       1.00787  |   0.38518  |
| solution-1-flask   |     0.419169 |       1.00846  |   0.79102  |
| solution-2         |     0.405331 |       0.502762 |   2.67644  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.409831 |       0.151534 |    1.12318 |
| solution-aron-mark |     0.411301 |       0.151055 |    1.12546 |
| solution-flask     |     0.409121 |       1.00828  |    1.62559 |
| solution-1-flask   |     0.411898 |       1.00815  |    5.61299 |
| solution-2         |     0.411704 |       0.559762 |   42.0884  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.412415 |       0.176053 |    3.87697 |
| solution-pl        |     0.410459 |       0.176587 |    3.99558 |
| solution-flask     |     0.418705 |       1.0089   |    5.22587 |