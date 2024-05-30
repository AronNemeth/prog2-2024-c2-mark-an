# 2024-05-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31728  |       1.11804  |   0.075276 |
| solution-aron-mark |     5.76267  |       0.101593 |   0.160007 |
| solution-pl        |     0.653608 |       0.102999 |   0.16469  |
| solution-1-flask   |     0.682981 |       1.01117  |   0.463303 |
| solution-1         |     7.92047  |       1e-06    |   0.591246 |
| solution-2         |     0.652081 |       0.418921 |   0.699619 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661523 |       1.00892  |   0.160608 |
| solution-pl        |     0.663414 |       0.103787 |   0.255261 |
| solution-aron-mark |     0.817838 |       0.103852 |   0.263092 |
| solution-1-flask   |     0.678178 |       1.00886  |   0.787695 |
| solution-2         |     0.672482 |       0.429254 |   2.66295  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671073 |       1.00893  |   0.697714 |
| solution-aron-mark |     0.66707  |       0.110499 |   0.782796 |
| solution-pl        |     0.675407 |       0.113352 |   0.910001 |
| solution-1-flask   |     0.689015 |       1.00927  |   5.5659   |
| solution-2         |     0.659772 |       0.481516 |  35.7294   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.681779 |       1.00918  |    2.50907 |
| solution-pl        |     0.664414 |       0.150072 |    2.62559 |
| solution-aron-mark |     0.670078 |       0.153151 |    2.64183 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666203 |       1.00917  |    16.9543 |
| solution-aron-mark |     0.657565 |       0.283264 |    20.1783 |
| solution-pl        |     0.663064 |       0.277952 |    21.7799 |