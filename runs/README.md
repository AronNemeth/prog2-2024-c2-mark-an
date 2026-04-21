# 2026-04-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.02041  |       1.06095  |   0.105852 |
| solution-aron-mark |     4.778    |       0.146588 |   0.236664 |
| solution-pl        |     0.421147 |       0.147615 |   0.236884 |
| solution-1-flask   |     0.424742 |       1.00812  |   0.268872 |
| solution-1         |     8.16764  |       1e-06    |   0.747673 |
| solution-2         |     0.433529 |       0.684753 |   1.44193  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.41702  |       0.150802 |   0.366814 |
| solution-pl        |     0.41349  |       0.148458 |   0.368448 |
| solution-flask     |     0.420053 |       1.00856  |   0.396582 |
| solution-1-flask   |     0.430584 |       1.00852  |   0.830043 |
| solution-2         |     0.414898 |       0.519459 |   5.2987   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417604 |       0.155788 |    1.12018 |
| solution-aron-mark |     0.428349 |       0.156363 |    1.1234  |
| solution-flask     |     0.42569  |       1.00854  |    1.68254 |
| solution-1-flask   |     0.427778 |       1.00856  |    5.72846 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415534 |       0.180761 |    3.78732 |
| solution-aron-mark |     0.42811  |       0.183587 |    3.85402 |
| solution-flask     |     0.419106 |       1.00878  |    5.4353  |