# 2025-07-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.72524  |       1.06292  |   0.102839 |
| solution-aron-mark |     4.85904  |       0.153466 |   0.241123 |
| solution-pl        |     0.529073 |       0.155322 |   0.243073 |
| solution-1-flask   |     0.530995 |       1.00854  |   0.26899  |
| solution-1         |     8.08402  |       1e-06    |   0.729219 |
| solution-2         |     0.520307 |       0.74526  |   1.25619  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.519824 |       0.156509 |   0.366391 |
| solution-aron-mark |     0.524131 |       0.155019 |   0.37087  |
| solution-flask     |     0.520406 |       1.00857  |   0.384606 |
| solution-1-flask   |     0.524918 |       1.00883  |   0.814957 |
| solution-2         |     0.527894 |       0.530078 |   2.7185   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521268 |       0.16127  |    1.08742 |
| solution-pl        |     0.516902 |       0.161932 |    1.12101 |
| solution-flask     |     0.526172 |       1.00872  |    1.64094 |
| solution-1-flask   |     0.525103 |       1.00849  |    5.68149 |
| solution-2         |     0.519283 |       0.597967 |   44.7715  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521586 |       0.196483 |    3.28069 |
| solution-aron-mark |     0.516235 |       0.19208  |    3.29639 |
| solution-flask     |     0.514985 |       1.00845  |    5.20333 |