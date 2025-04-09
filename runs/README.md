# 2025-04-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.527229 |       1.00863  |   0.08486  |
| solution-aron-mark |     1.8276   |       0.124151 |   0.190302 |
| solution-pl        |     0.52637  |       0.124995 |   0.191485 |
| solution-1-flask   |     5.04511  |       1.06655  |   0.271384 |
| solution-1         |     7.62328  |       1e-06    |   0.875827 |
| solution-2         |     0.52878  |       0.685818 |   1.19037  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.52949  |       0.124794 |   0.297583 |
| solution-flask     |     0.533632 |       1.00879  |   0.303887 |
| solution-pl        |     0.534198 |       0.126302 |   0.305676 |
| solution-1-flask   |     0.533526 |       1.00913  |   0.803791 |
| solution-2         |     0.531772 |       0.536582 |   3.27219  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533274 |       0.131653 |   0.913693 |
| solution-pl        |     0.533264 |       0.133657 |   0.929714 |
| solution-flask     |     0.527421 |       1.0091   |   1.27637  |
| solution-1-flask   |     0.605881 |       1.00925  |   5.79663  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534353 |       0.162319 |    2.97893 |
| solution-pl        |     0.532671 |       0.161739 |    2.99137 |
| solution-flask     |     0.55023  |       1.00915  |    4.3394  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.5403   |       0.27031  |    18.3071 |
| solution-aron-mark |     0.531063 |       0.277144 |    18.5645 |