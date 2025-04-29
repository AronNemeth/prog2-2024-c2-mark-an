# 2025-04-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0562   |       1.0998   |   0.088145 |
| solution-pl        |     5.56448  |       0.120355 |   0.190888 |
| solution-aron-mark |     0.510516 |       0.119834 |   0.192963 |
| solution-1-flask   |     0.524145 |       1.00881  |   0.261824 |
| solution-1         |     7.22521  |       1e-06    |   0.626574 |
| solution-2         |     0.511952 |       0.641161 |   1.28155  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521381 |       1.00902  |   0.297856 |
| solution-pl        |     0.511688 |       0.122785 |   0.299085 |
| solution-aron-mark |     0.510353 |       0.12244  |   0.300467 |
| solution-1-flask   |     0.536282 |       1.00932  |   0.771689 |
| solution-2         |     0.520302 |       0.511949 |   4.5317   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.513516 |       0.129466 |   0.897867 |
| solution-aron-mark |     0.503777 |       0.137493 |   0.901499 |
| solution-flask     |     0.504712 |       1.00882  |   1.28708  |
| solution-1-flask   |     0.513775 |       1.00888  |   5.33835  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507168 |       0.159529 |    2.83283 |
| solution-pl        |     0.510468 |       0.159837 |    2.83313 |
| solution-flask     |     0.503176 |       1.00907  |    4.28054 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50246  |       0.272721 |    15.9231 |
| solution-aron-mark |     0.502336 |       0.269474 |    16.0013 |