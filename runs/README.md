# 2024-04-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662061 |       1.00889  |   0.076347 |
| solution-aron-mark |     0.665361 |       0.111832 |   0.171287 |
| solution-pl        |    11.0534   |       0.114115 |   0.17573  |
| solution-1-flask   |     1.50852  |       1.05518  |   0.263673 |
| solution-1         |     8.17419  |       1e-06    |   0.809726 |
| solution-2         |     0.659258 |       0.418245 |   1.29204  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670618 |       1.009    |   0.159047 |
| solution-pl        |     0.668157 |       0.119455 |   0.262624 |
| solution-aron-mark |     0.664007 |       0.118535 |   0.26905  |
| solution-1-flask   |     0.682928 |       1.00947  |   0.789197 |
| solution-2         |     0.669777 |       0.434881 |  25.1376   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661837 |       1.00921  |   0.717786 |
| solution-aron-mark |     0.66704  |       0.126209 |   0.828248 |
| solution-pl        |     0.658626 |       0.127526 |   0.828959 |
| solution-1-flask   |     0.682281 |       1.00897  |   5.6048   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662134 |       1.00895  |    2.55284 |
| solution-pl        |     0.662869 |       0.163862 |    2.64287 |
| solution-aron-mark |     0.665323 |       0.164772 |    2.64779 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.665961 |       0.284536 |    16.0312 |
| solution-pl        |     0.663715 |       0.285681 |    16.5464 |
| solution-flask     |     0.663248 |       1.00905  |    16.9319 |