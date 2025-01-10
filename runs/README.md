# 2025-01-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.83235  |       1.00858  |   0.101334 |
| solution-aron-mark |     0.52141  |       0.111043 |   0.185317 |
| solution-pl        |     0.521434 |       0.11077  |   0.195216 |
| solution-1-flask   |     5.19265  |       1.09941  |   0.265886 |
| solution-1         |     7.56408  |       1e-06    |   0.58838  |
| solution-2         |     0.523503 |       0.513468 |   2.02328  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525427 |       0.112709 |   0.315174 |
| solution-pl        |     0.525472 |       0.111842 |   0.321758 |
| solution-flask     |     0.525794 |       1.0088   |   0.483966 |
| solution-1-flask   |     0.531694 |       1.00869  |   0.789869 |
| solution-2         |     0.524704 |       0.484422 |   7.0314   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521494 |       0.117925 |    1.07251 |
| solution-pl        |     0.523973 |       0.11883  |    1.07349 |
| solution-flask     |     0.52207  |       1.00861  |    2.15546 |
| solution-1-flask   |     0.530442 |       1.00897  |    5.66404 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524445 |       0.147367 |    4.18575 |
| solution-aron-mark |     0.522326 |       0.145914 |    4.21447 |
| solution-flask     |     0.524509 |       1.00902  |    8.24852 |