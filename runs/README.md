# 2024-12-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.07557  |       1.16283  |   0.108113 |
| solution-aron-mark |     0.551213 |       0.106907 |   0.172882 |
| solution-pl        |     5.6909   |       0.107566 |   0.193344 |
| solution-1-flask   |     0.558268 |       1.00876  |   0.252057 |
| solution-1         |     7.493    |       1e-06    |   0.568336 |
| solution-2         |     0.54855  |       0.483423 |   1.1132   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.555997 |       0.124571 |   0.298475 |
| solution-pl        |     0.560335 |       0.111937 |   0.323697 |
| solution-flask     |     0.551621 |       1.0088   |   0.492997 |
| solution-1-flask   |     0.55512  |       1.00871  |   0.754823 |
| solution-2         |     0.553133 |       0.469791 |   3.33978  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.549685 |       0.114976 |   0.999924 |
| solution-pl        |     0.552705 |       0.114979 |   1.00528  |
| solution-flask     |     0.55429  |       1.00873  |   2.16509  |
| solution-1-flask   |     0.556692 |       1.00923  |   5.27793  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550776 |       0.147926 |    4.15119 |
| solution-aron-mark |     0.548661 |       0.144509 |    4.24899 |
| solution-flask     |     0.543735 |       1.00875  |    8.47983 |