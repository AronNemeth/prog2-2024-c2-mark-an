# 2025-07-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.80133  |       1.07693  |   0.101608 |
| solution-aron-mark |     5.14216  |       0.153465 |   0.236104 |
| solution-pl        |     0.521728 |       0.154935 |   0.24059  |
| solution-1-flask   |     0.512744 |       1.00821  |   0.2747   |
| solution-1         |     8.11101  |       1e-06    |   0.745528 |
| solution-2         |     0.629406 |       0.626292 |   1.52463  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.504534 |       0.154518 |   0.365324 |
| solution-pl        |     0.514464 |       0.154287 |   0.368909 |
| solution-flask     |     0.519062 |       1.00845  |   0.387967 |
| solution-1-flask   |     0.524087 |       1.00835  |   0.801343 |
| solution-2         |     0.542175 |       0.54133  |   3.0492   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.526317 |       0.163271 |    1.07748 |
| solution-pl        |     0.536678 |       0.170163 |    1.10326 |
| solution-flask     |     0.519861 |       1.00873  |    1.63851 |
| solution-1-flask   |     0.511525 |       1.00871  |    5.89694 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.514881 |       0.190986 |    3.27405 |
| solution-aron-mark |     0.524777 |       0.192313 |    3.35247 |
| solution-flask     |     0.524596 |       1.00839  |    5.23361 |