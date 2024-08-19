# 2024-08-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566243 |       1.00926  |   0.09521  |
| solution-aron-mark |     1.91479  |       0.104501 |   0.174649 |
| solution-pl        |     0.561583 |       0.104364 |   0.176405 |
| solution-1-flask   |     1.29727  |       1.0487   |   0.263968 |
| solution-1         |     7.85223  |       1e-06    |   0.637823 |
| solution-2         |     4.5403   |       0.553084 |   1.11041  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.572172 |       1.00939  |   0.232611 |
| solution-aron-mark |     0.582035 |       0.106696 |   0.298059 |
| solution-pl        |     0.566738 |       0.10679  |   0.338026 |
| solution-1-flask   |     0.570041 |       1.00915  |   0.788101 |
| solution-2         |     0.56512  |       0.481109 |   4.22403  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563061 |       1.00902  |   0.924397 |
| solution-pl        |     0.563786 |       0.113595 |   1.01983  |
| solution-aron-mark |     0.565795 |       0.115359 |   1.02279  |
| solution-1-flask   |     0.578937 |       1.00932  |   5.52719  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56131  |       1.00926  |    4.29838 |
| solution-pl        |     0.559227 |       0.143881 |    4.41874 |
| solution-aron-mark |     0.569009 |       0.142702 |    4.44289 |