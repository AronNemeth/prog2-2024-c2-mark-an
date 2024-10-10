# 2024-10-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06364  |       1.04809  |   0.089243 |
| solution-aron-mark |     0.543845 |       0.101153 |   0.171908 |
| solution-pl        |     5.57469  |       0.103141 |   0.178184 |
| solution-1-flask   |     0.554688 |       1.00891  |   0.257178 |
| solution-1         |     7.77607  |       1e-06    |   0.662757 |
| solution-2         |     0.55399  |       0.539832 |   0.769366 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553818 |       1.00929  |   0.225052 |
| solution-aron-mark |     0.549397 |       0.102773 |   0.288737 |
| solution-pl        |     0.549204 |       0.103356 |   0.289284 |
| solution-1-flask   |     0.558792 |       1.00919  |   0.760408 |
| solution-2         |     0.544031 |       0.464388 |   2.97056  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555512 |       1.00894  |   0.888531 |
| solution-pl        |     0.556246 |       0.110237 |   0.986892 |
| solution-aron-mark |     0.553546 |       0.11136  |   0.992959 |
| solution-1-flask   |     0.62716  |       1.01052  |   6.60414  |
| solution-2         |     0.54768  |       0.514752 | 171.165    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688349 |       1.01042  |    6.11886 |
| solution-aron-mark |     0.669182 |       0.1525   |    6.85337 |
| solution-pl        |     0.707399 |       0.172381 |    6.88401 |