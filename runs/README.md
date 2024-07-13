# 2024-07-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29763  |       1.05171  |   0.073134 |
| solution-aron-mark |     0.470241 |       0.099824 |   0.160419 |
| solution-pl        |     5.80595  |       0.095824 |   0.162507 |
| solution-1-flask   |     0.496762 |       1.00891  |   0.253908 |
| solution-1         |     7.89798  |       1e-06    |   0.570821 |
| solution-2         |     0.484051 |       0.487516 |   0.721955 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.489522 |       1.00838  |   0.217147 |
| solution-aron-mark |     0.483808 |       0.120405 |   0.281838 |
| solution-pl        |     0.480379 |       0.10513  |   0.296751 |
| solution-1-flask   |     0.500141 |       1.00915  |   0.767086 |
| solution-2         |     0.490636 |       0.461054 |   3.52379  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.491961 |       1.00871  |   0.872484 |
| solution-aron-mark |     0.488712 |       0.108999 |   0.993362 |
| solution-pl        |     0.499731 |       0.110448 |   0.995332 |
| solution-1-flask   |     0.492066 |       1.0087   |   5.54618  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.490052 |       1.0088   |    3.97185 |
| solution-aron-mark |     0.491156 |       0.145597 |    4.04064 |
| solution-pl        |     0.491862 |       0.143545 |    4.09052 |