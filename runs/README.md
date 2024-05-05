# 2024-05-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.65767  |       1.0086   |   0.075586 |
| solution-aron-mark |     0.658168 |       0.11434  |   0.175595 |
| solution-pl        |     5.91775  |       0.115625 |   0.17646  |
| solution-1-flask   |     1.5753   |       1.05317  |   0.263933 |
| solution-1         |     7.97652  |       1e-06    |   0.564178 |
| solution-2         |     0.658277 |       0.40958  |   0.871936 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.648987 |       1.00853  |   0.160857 |
| solution-aron-mark |     0.639961 |       0.124486 |   0.271829 |
| solution-pl        |     0.653099 |       0.122918 |   0.284201 |
| solution-1-flask   |     0.667682 |       1.00851  |   0.788617 |
| solution-2         |     0.663578 |       0.420709 |   2.29891  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.648798 |       1.00841  |   0.716482 |
| solution-aron-mark |     0.650296 |       0.128998 |   0.810814 |
| solution-pl        |     0.651013 |       0.129758 |   0.833243 |
| solution-1-flask   |     0.655784 |       1.00872  |   5.61138  |
| solution-2         |     0.659829 |       0.468744 | 163.497    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.649179 |       1.0085   |    2.4594  |
| solution-aron-mark |     0.654041 |       0.165178 |    2.57758 |
| solution-pl        |     0.639215 |       0.163024 |    2.59469 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.646215 |       1.00849  |    15.4598 |
| solution-aron-mark |     0.644895 |       0.291393 |    15.5215 |
| solution-pl        |     0.642806 |       0.29081  |    16.0938 |