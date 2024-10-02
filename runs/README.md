# 2024-10-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19336  |       1.10941  |   0.085409 |
| solution-aron-mark |     1.92458  |       0.103417 |   0.177099 |
| solution-pl        |     0.556628 |       0.10165  |   0.17788  |
| solution-1-flask   |     0.576447 |       1.00845  |   0.265119 |
| solution-1         |     7.4801   |       1e-06    |   0.590984 |
| solution-2         |     4.40458  |       0.57673  |   0.925956 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566089 |       1.00819  |   0.205347 |
| solution-aron-mark |     0.565276 |       0.103898 |   0.30692  |
| solution-pl        |     0.575459 |       0.104507 |   0.309913 |
| solution-1-flask   |     0.570173 |       1.00833  |   0.788538 |
| solution-2         |     0.571569 |       0.485572 |   5.14439  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552553 |       1.00866  |   0.953973 |
| solution-pl        |     0.561625 |       0.110701 |   1.05937  |
| solution-aron-mark |     0.566198 |       0.110697 |   1.11424  |
| solution-1-flask   |     0.583384 |       1.00835  |   5.5227   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559582 |       1.00889  |    4.21293 |
| solution-aron-mark |     0.554408 |       0.137364 |    4.31593 |
| solution-pl        |     0.558856 |       0.13957  |    4.34547 |