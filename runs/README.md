# 2025-02-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.31997  |       1.09055  |   0.082927 |
| solution-pl        |     4.91509  |       0.14124  |   0.201969 |
| solution-aron-mark |     0.527566 |       0.135499 |   0.202014 |
| solution-1-flask   |     0.531585 |       1.00872  |   0.287604 |
| solution-1         |     7.31686  |       1e-06    |   0.653578 |
| solution-2         |     0.524541 |       0.601665 |   0.814132 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.525734 |       1.00882  |   0.291729 |
| solution-pl        |     0.527516 |       0.138783 |   0.304747 |
| solution-aron-mark |     0.55669  |       0.140349 |   0.308692 |
| solution-1-flask   |     0.532871 |       1.00896  |   0.808462 |
| solution-2         |     0.525841 |       0.485178 |   2.43557  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.52925  |       0.144708 |   0.896602 |
| solution-pl        |     0.525337 |       0.144606 |   0.899648 |
| solution-flask     |     0.548814 |       1.00872  |   1.22861  |
| solution-1-flask   |     0.535123 |       1.00918  |   5.72255  |
| solution-2         |     0.526393 |       0.560724 |  42.9641   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.526576 |       0.172376 |    2.78962 |
| solution-aron-mark |     0.535869 |       0.176074 |    2.7976  |
| solution-flask     |     0.52579  |       1.01011  |    4.20941 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525823 |       0.282221 |     16.662 |
| solution-pl        |     0.530457 |       0.276405 |     17.1   |