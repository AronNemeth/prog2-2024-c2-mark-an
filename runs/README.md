# 2025-12-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.7184   |       1.05404  |   0.098375 |
| solution-pl        |     0.466603 |       0.162146 |   0.243231 |
| solution-aron-mark |     0.471683 |       0.158596 |   0.245379 |
| solution-1-flask   |     0.474497 |       1.00813  |   0.262515 |
| solution-1         |     7.62217  |       1e-06    |   0.659836 |
| solution-2         |     5.46158  |       0.622824 |   1.16929  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465882 |       0.160243 |   0.364049 |
| solution-aron-mark |     0.469266 |       0.161672 |   0.367687 |
| solution-flask     |     0.466133 |       1.00832  |   0.379758 |
| solution-1-flask   |     0.474196 |       1.00821  |   0.796841 |
| solution-2         |     0.463289 |       0.499063 |   3.87188  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469262 |       0.167351 |    1.06184 |
| solution-pl        |     0.46706  |       0.167458 |    1.06394 |
| solution-flask     |     0.468421 |       1.00835  |    1.54718 |
| solution-1-flask   |     0.472465 |       1.00841  |    5.54551 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465724 |       0.190118 |    3.41815 |
| solution-pl        |     0.465856 |       0.19128  |    3.45143 |
| solution-flask     |     0.463753 |       1.00837  |    5.01169 |