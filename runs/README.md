# 2026-07-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.22416  |       1.04425  |   0.113134 |
| solution-aron-mark |     0.443818 |       0.150222 |   0.236107 |
| solution-pl        |     6.34262  |       0.187709 |   0.23826  |
| solution-1-flask   |     0.442661 |       1.00832  |   0.275009 |
| solution-1         |     7.82187  |       1e-06    |   0.711929 |
| solution-2         |     0.422296 |       0.679984 |   0.913771 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431342 |       0.151554 |   0.370566 |
| solution-aron-mark |     0.447826 |       0.158854 |   0.383542 |
| solution-flask     |     0.428395 |       1.00825  |   0.399012 |
| solution-1-flask   |     0.438969 |       1.00841  |   0.814399 |
| solution-2         |     0.43361  |       0.507024 |   4.99523  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432928 |       0.160703 |    1.12708 |
| solution-pl        |     0.439325 |       0.160737 |    1.16972 |
| solution-flask     |     0.427531 |       1.00834  |    1.71428 |
| solution-1-flask   |     0.436072 |       1.00863  |    5.94432 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432568 |       0.184235 |    3.97836 |
| solution-aron-mark |     0.424476 |       0.184589 |    4.01484 |
| solution-flask     |     0.431163 |       1.00849  |    5.40359 |