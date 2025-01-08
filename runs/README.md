# 2025-01-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.94446  |       1.0085   |   0.103701 |
| solution-pl        |     0.541466 |       0.111041 |   0.188965 |
| solution-aron-mark |     0.519909 |       0.108594 |   0.18971  |
| solution-1-flask   |     5.47544  |       1.06226  |   0.270172 |
| solution-1         |     7.75864  |       1e-06    |   0.783367 |
| solution-2         |     0.520071 |       0.65557  |   0.904628 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.524713 |       0.112079 |   0.317438 |
| solution-pl        |     0.526805 |       0.11229  |   0.317683 |
| solution-flask     |     0.521706 |       1.00883  |   0.477788 |
| solution-1-flask   |     0.533169 |       1.00865  |   0.798506 |
| solution-2         |     0.519557 |       0.487144 |   2.75091  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525845 |       0.11942  |    1.0729  |
| solution-aron-mark |     0.531076 |       0.118653 |    1.09125 |
| solution-flask     |     0.524517 |       1.00902  |    2.13275 |
| solution-1-flask   |     0.531557 |       1.0089   |    5.69694 |
| solution-2         |     0.524078 |       0.564194 |  169.724   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.524055 |       0.149238 |    4.34128 |
| solution-pl        |     0.532891 |       0.146128 |    4.36787 |
| solution-flask     |     0.527182 |       1.00901  |    8.50361 |