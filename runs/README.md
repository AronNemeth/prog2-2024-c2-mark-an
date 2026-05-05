# 2026-05-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06164  |       1.04987  |   0.102836 |
| solution-aron-mark |     5.39489  |       0.146624 |   0.232109 |
| solution-pl        |     0.413173 |       0.146222 |   0.236611 |
| solution-1-flask   |     0.422056 |       1.00801  |   0.271242 |
| solution-1         |     8.53028  |       1e-06    |   0.850737 |
| solution-2         |     0.416173 |       0.716294 |   1.41652  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419357 |       0.146848 |   0.366911 |
| solution-aron-mark |     0.416157 |       0.147827 |   0.36829  |
| solution-flask     |     0.412748 |       1.00843  |   0.398031 |
| solution-1-flask   |     0.426908 |       1.00833  |   0.806652 |
| solution-2         |     0.411319 |       0.523998 |   3.26299  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.410706 |       0.153214 |    1.11917 |
| solution-aron-mark |     0.415321 |       0.154033 |    1.12015 |
| solution-flask     |     0.439203 |       1.00825  |    1.65505 |
| solution-1-flask   |     0.418065 |       1.00847  |    5.66173 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.411393 |       0.17877  |    3.86818 |
| solution-aron-mark |     0.411993 |       0.178022 |    3.88869 |
| solution-flask     |     0.413769 |       1.00833  |    5.33581 |