# 2025-06-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.545692 |       1.0092   |   0.101614 |
| solution-pl        |     0.523093 |       0.157931 |   0.24374  |
| solution-aron-mark |     6.30197  |       0.172869 |   0.246041 |
| solution-1-flask   |     1.15006  |       1.06866  |   0.275416 |
| solution-1         |     7.85447  |       1e-06    |   0.6507   |
| solution-2         |     0.532842 |       0.580749 |   1.03945  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.526347 |       0.156083 |   0.365287 |
| solution-pl        |     0.515083 |       0.154398 |   0.365793 |
| solution-flask     |     0.536079 |       1.0084   |   0.378479 |
| solution-1-flask   |     0.544075 |       1.0089   |   0.81829  |
| solution-2         |     0.546593 |       0.571496 |   2.77876  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.533592 |       0.163491 |    1.06706 |
| solution-aron-mark |     0.543174 |       0.167157 |    1.0676  |
| solution-flask     |     0.52049  |       1.00858  |    1.57704 |
| solution-1-flask   |     0.545707 |       1.00845  |    5.62875 |
| solution-2         |     0.536045 |       0.609634 |   37.672   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.546249 |       0.194674 |    3.34809 |
| solution-pl        |     0.521698 |       0.193212 |    3.36626 |
| solution-flask     |     0.530973 |       1.00912  |    5.29159 |