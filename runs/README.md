# 2025-03-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.533169 |       1.00893  |   0.080597 |
| solution-pl        |     0.529803 |       0.145659 |   0.20792  |
| solution-aron-mark |     1.77982  |       0.15259  |   0.210314 |
| solution-1-flask   |     5.37966  |       1.07427  |   0.270218 |
| solution-1         |     7.97902  |       1e-06    |   0.649864 |
| solution-2         |     0.521484 |       0.566072 |   1.36751  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.545052 |       1.00907  |   0.294917 |
| solution-aron-mark |     0.531226 |       0.146935 |   0.311546 |
| solution-pl        |     0.53507  |       0.151321 |   0.330746 |
| solution-1-flask   |     0.539856 |       1.00912  |   0.806512 |
| solution-2         |     0.526182 |       0.519625 |   2.46437  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.551593 |       0.157622 |   0.909103 |
| solution-pl        |     0.550412 |       0.163608 |   0.909517 |
| solution-flask     |     0.54847  |       1.00935  |   1.24191  |
| solution-1-flask   |     0.546453 |       1.00893  |   5.81662  |
| solution-2         |     0.554466 |       0.593302 |  27.8325   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524582 |       0.182813 |    2.82058 |
| solution-aron-mark |     0.541292 |       0.186009 |    3.02193 |
| solution-flask     |     0.538592 |       1.00924  |    4.2292  |

## Inputs: 1000000, Queries 1000

| solution    |   setup_time |   preproc_time |   run_time |
|:------------|-------------:|---------------:|-----------:|
| solution-pl |     0.513826 |       0.283096 |    17.4216 |