# 2025-03-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.533109 |       1.00861  |   0.083704 |
| solution-pl        |     0.517733 |       0.124655 |   0.191159 |
| solution-aron-mark |     1.87223  |       0.125342 |   0.192818 |
| solution-1-flask   |     5.68377  |       1.09601  |   0.269902 |
| solution-1         |     8.02477  |       1e-06    |   0.605057 |
| solution-2         |     0.544434 |       0.558589 |   0.901632 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511886 |       0.122422 |   0.292703 |
| solution-aron-mark |     0.517237 |       0.121149 |   0.292811 |
| solution-flask     |     0.518444 |       1.00888  |   0.298335 |
| solution-1-flask   |     0.521896 |       1.00897  |   0.81458  |
| solution-2         |     0.52133  |       0.512569 |   2.7983   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.537696 |       0.132524 |   0.897815 |
| solution-aron-mark |     0.539787 |       0.131603 |   0.92675  |
| solution-flask     |     0.525965 |       1.00904  |   1.26836  |
| solution-1-flask   |     0.514491 |       1.00897  |   5.7063   |
| solution-2         |     0.516873 |       0.570086 | 176.6      |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.523391 |       0.161779 |    2.90318 |
| solution-aron-mark |     0.535979 |       0.167018 |    2.95888 |
| solution-flask     |     0.543934 |       1.0092   |    4.35452 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535064 |       0.276445 |    18.464  |
| solution-aron-mark |     0.52584  |       0.275908 |    18.5402 |