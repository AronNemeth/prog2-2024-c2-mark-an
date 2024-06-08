# 2024-06-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.5622   |       1.1126   |   0.06687  |
| solution-pl        |     0.713165 |       0.108877 |   0.163828 |
| solution-aron-mark |     6.53024  |       0.109029 |   0.16751  |
| solution-1-flask   |     0.707046 |       1.00911  |   0.254574 |
| solution-1         |     8.86303  |       1e-06    |   0.739523 |
| solution-2         |     0.724981 |       0.447838 |   1.72073  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671512 |       1.00897  |   0.165395 |
| solution-aron-mark |     0.686129 |       0.106905 |   0.259659 |
| solution-pl        |     0.684962 |       0.106164 |   0.266168 |
| solution-1-flask   |     0.695011 |       1.00996  |   0.795806 |
| solution-2         |     0.681153 |       0.436709 |   4.76321  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673034 |       1.00949  |   0.718429 |
| solution-pl        |     0.719528 |       0.114861 |   0.80782  |
| solution-aron-mark |     0.69778  |       0.121176 |   0.837645 |
| solution-1-flask   |     0.712941 |       1.00938  |   5.74287  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.693669 |       1.00913  |    2.6605  |
| solution-aron-mark |     0.70579  |       0.15565  |    2.7311  |
| solution-pl        |     0.679562 |       0.159458 |    2.77663 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.678303 |       1.00929  |    17.7319 |
| solution-pl        |     0.679237 |       0.282874 |    23.1758 |
| solution-aron-mark |     0.716527 |       0.281384 |    23.9554 |