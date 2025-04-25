# 2025-04-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.18481  |       1.05172  |   0.083806 |
| solution-pl        |     5.88532  |       0.121137 |   0.18395  |
| solution-aron-mark |     0.505515 |       0.121696 |   0.187349 |
| solution-1-flask   |     0.512614 |       1.00846  |   0.262223 |
| solution-1         |     7.75943  |       1e-06    |   0.595912 |
| solution-2         |     0.505028 |       0.53481  |   1.01049  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.508241 |       0.123585 |   0.291132 |
| solution-flask     |     0.507779 |       1.00855  |   0.293145 |
| solution-pl        |     0.512503 |       0.129956 |   0.302709 |
| solution-1-flask   |     0.509571 |       1.00879  |   0.782272 |
| solution-2         |     0.503128 |       0.500031 |   3.30706  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.514129 |       0.128817 |   0.91249  |
| solution-pl        |     0.501889 |       0.127563 |   0.920921 |
| solution-flask     |     0.506174 |       1.0086   |   1.23791  |
| solution-1-flask   |     0.512202 |       1.00869  |   5.41521  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505972 |       0.161221 |    2.83706 |
| solution-pl        |     0.508546 |       0.15955  |    2.84794 |
| solution-flask     |     0.499256 |       1.00928  |    4.25102 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51174  |       0.268865 |    16.6367 |
| solution-pl        |     0.509685 |       0.266591 |    16.7056 |