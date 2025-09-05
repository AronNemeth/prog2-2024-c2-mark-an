# 2025-09-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.503114 |       1.00838  |   0.102813 |
| solution-aron-mark |     0.958045 |       0.16679  |   0.246958 |
| solution-pl        |     6.27805  |       0.366249 |   0.247542 |
| solution-1-flask   |     1.27874  |       1.06491  |   0.272671 |
| solution-1         |     8.33144  |       1e-06    |   0.794322 |
| solution-2         |     0.500426 |       0.716641 |   0.947575 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.509127 |       0.160231 |   0.36632  |
| solution-pl        |     0.506631 |       0.156741 |   0.367224 |
| solution-flask     |     0.484977 |       1.00856  |   0.383431 |
| solution-1-flask   |     0.501335 |       1.00818  |   0.825192 |
| solution-2         |     0.495108 |       0.52425  |   1.9082   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492833 |       0.166111 |    1.05906 |
| solution-aron-mark |     0.496924 |       0.166484 |    1.06678 |
| solution-flask     |     0.502979 |       1.00872  |    1.56901 |
| solution-1-flask   |     0.503167 |       1.00845  |    5.6914  |
| solution-2         |     0.492637 |       0.583502 |  314.608   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499836 |       0.200301 |    3.32982 |
| solution-aron-mark |     0.489788 |       0.198573 |    3.37263 |
| solution-flask     |     0.489588 |       1.00818  |    5.26809 |