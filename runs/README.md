# 2025-06-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.81454  |       1.00837  |   0.100141 |
| solution-pl        |     0.520322 |       0.154763 |   0.237104 |
| solution-aron-mark |     0.515446 |       0.154765 |   0.239053 |
| solution-1-flask   |     5.03893  |       1.05031  |   0.268682 |
| solution-1         |     7.61949  |       1e-06    |   0.685104 |
| solution-2         |     0.503314 |       0.66224  |   1.06514  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.519512 |       0.157743 |   0.361989 |
| solution-pl        |     0.524267 |       0.154501 |   0.368463 |
| solution-flask     |     0.520185 |       1.00872  |   0.378222 |
| solution-1-flask   |     0.523714 |       1.00852  |   0.793113 |
| solution-2         |     0.522141 |       0.539576 |   4.22477  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51419  |       0.161607 |    1.06664 |
| solution-pl        |     0.515663 |       0.161003 |    1.07302 |
| solution-flask     |     0.524999 |       1.00892  |    1.58236 |
| solution-1-flask   |     0.528287 |       1.00909  |    5.36902 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.522356 |       0.191113 |    3.29959 |
| solution-pl        |     0.513726 |       0.194734 |    3.30038 |
| solution-flask     |     0.514541 |       1.00882  |    5.12992 |