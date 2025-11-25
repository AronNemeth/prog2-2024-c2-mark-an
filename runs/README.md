# 2025-11-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.76128  |       1.13862  |   0.102162 |
| solution-aron-mark |     0.49314  |       0.162252 |   0.248689 |
| solution-pl        |     0.478078 |       0.161014 |   0.251568 |
| solution-1-flask   |     0.480995 |       1.00849  |   0.267303 |
| solution-1         |     9.47757  |       1e-06    |   0.745102 |
| solution-2         |     5.34369  |       0.699804 |   1.08386  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.490287 |       0.165236 |   0.380676 |
| solution-flask     |     0.483305 |       1.0088   |   0.385307 |
| solution-pl        |     0.504416 |       0.169797 |   0.391296 |
| solution-1-flask   |     0.514277 |       1.00928  |   0.799781 |
| solution-2         |     0.4768   |       0.51582  |   4.16493  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.483961 |       0.178886 |    1.11678 |
| solution-aron-mark |     0.487139 |       0.183953 |    1.12688 |
| solution-flask     |     0.494505 |       1.00909  |    1.62195 |
| solution-1-flask   |     0.513668 |       1.009    |    5.73946 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473014 |       0.194947 |    3.39142 |
| solution-aron-mark |     0.481637 |       0.206641 |    3.39223 |
| solution-flask     |     0.484314 |       1.00923  |    5.21887 |