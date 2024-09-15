# 2024-09-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19268  |       1.06493  |   0.076393 |
| solution-pl        |     0.553541 |       0.10189  |   0.167805 |
| solution-aron-mark |     5.62706  |       0.102159 |   0.17068  |
| solution-1-flask   |     0.556116 |       1.00888  |   0.25831  |
| solution-1         |     7.73939  |       1e-06    |   0.58087  |
| solution-2         |     0.557566 |       0.486137 |   1.47179  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551088 |       1.00895  |   0.224667 |
| solution-pl        |     0.56334  |       0.105267 |   0.291263 |
| solution-aron-mark |     0.558443 |       0.105704 |   0.292768 |
| solution-1-flask   |     0.555721 |       1.00919  |   0.786374 |
| solution-2         |     0.56999  |       0.469725 |   2.12116  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548646 |       1.0091   |   0.869766 |
| solution-pl        |     0.551843 |       0.110988 |   0.978197 |
| solution-aron-mark |     0.551578 |       0.111772 |   0.980743 |
| solution-1-flask   |     0.55681  |       1.00926  |   5.5652   |
| solution-2         |     0.551236 |       0.525668 | 310.054    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550029 |       1.00908  |    4.01193 |
| solution-aron-mark |     0.553691 |       0.143621 |    4.1102  |
| solution-pl        |     0.544623 |       0.142988 |    4.14074 |