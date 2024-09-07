# 2024-09-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30419  |       1.07831  |   0.086853 |
| solution-aron-mark |     5.6561   |       0.096859 |   0.160127 |
| solution-pl        |     0.520031 |       0.097649 |   0.163264 |
| solution-1-flask   |     0.523381 |       1.0088   |   0.242985 |
| solution-1         |     7.53463  |       1e-06    |   0.5421   |
| solution-2         |     0.518022 |       0.538669 |   0.810989 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511963 |       1.00872  |   0.20318  |
| solution-aron-mark |     0.515083 |       0.098022 |   0.271657 |
| solution-pl        |     0.51937  |       0.099674 |   0.314424 |
| solution-1-flask   |     0.52737  |       1.00913  |   0.713082 |
| solution-2         |     0.531689 |       0.444875 |   3.51993  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.517241 |       1.00851  |   0.825321 |
| solution-aron-mark |     0.515426 |       0.109735 |   0.918554 |
| solution-pl        |     0.52292  |       0.107871 |   0.948256 |
| solution-1-flask   |     0.533059 |       1.00884  |   5.19155  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.529535 |       1.00899  |    3.84418 |
| solution-pl        |     0.514475 |       0.141904 |    3.89124 |
| solution-aron-mark |     0.517591 |       0.136013 |    3.9921  |