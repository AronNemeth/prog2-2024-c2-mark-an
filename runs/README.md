# 2025-06-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.8009   |       1.00806  |   0.096762 |
| solution-pl        |     0.489859 |       0.144066 |   0.226673 |
| solution-aron-mark |     0.491776 |       0.144838 |   0.228374 |
| solution-1-flask   |     5.02503  |       1.08902  |   0.261506 |
| solution-1         |     7.72145  |       1e-06    |   0.590865 |
| solution-2         |     0.492093 |       0.612705 |   0.753999 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488605 |       0.14692  |   0.351715 |
| solution-aron-mark |     0.487939 |       0.146448 |   0.354339 |
| solution-flask     |     0.493328 |       1.00816  |   0.367654 |
| solution-1-flask   |     0.496183 |       1.00803  |   0.781043 |
| solution-2         |     0.497582 |       0.492949 |   2.6738   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488129 |       0.152935 |    1.03106 |
| solution-aron-mark |     0.490148 |       0.152408 |    1.03658 |
| solution-flask     |     0.487952 |       1.00829  |    1.52855 |
| solution-1-flask   |     0.512008 |       1.00831  |    5.32704 |
| solution-2         |     0.487017 |       0.545293 |  162.851   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489326 |       0.183192 |    3.12055 |
| solution-pl        |     0.492083 |       0.184079 |    3.12785 |
| solution-flask     |     0.491825 |       1.00815  |    4.95668 |