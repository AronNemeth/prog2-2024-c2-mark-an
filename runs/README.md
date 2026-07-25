# 2026-07-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48672  |       1.00635  |   0.076803 |
| solution-1-flask   |     2.62482  |       1.23912  |   0.155994 |
| solution-aron-mark |     0.300536 |       0.106318 |   0.159632 |
| solution-pl        |     0.296714 |       0.107789 |   0.162179 |
| solution-2         |     3.41209  |       0.599715 |   0.601948 |
| solution-1         |     6.98709  |       1e-06    |   0.636524 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.300008 |       0.109627 |   0.242883 |
| solution-aron-mark |     0.303459 |       0.110309 |   0.246568 |
| solution-flask     |     0.295515 |       1.00617  |   0.293168 |
| solution-1-flask   |     0.300322 |       1.0062   |   0.488142 |
| solution-2         |     0.295221 |       0.361432 |   2.03164  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.290116 |       0.109818 |   0.790281 |
| solution-aron-mark |     0.29223  |       0.111495 |   0.801035 |
| solution-flask     |     0.295892 |       1.00729  |   1.30947  |
| solution-1-flask   |     0.29212  |       1.0063   |   4.05544  |
| solution-2         |     0.293561 |       0.396051 | 116.387    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.29466  |       0.149031 |    3.32907 |
| solution-pl        |     0.292525 |       0.128168 |    3.33493 |
| solution-flask     |     0.281604 |       1.00709  |    4.15377 |