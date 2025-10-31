# 2025-10-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.07522  |       1.05367  |   0.100421 |
| solution-pl        |     0.476166 |       0.160264 |   0.241859 |
| solution-aron-mark |     0.470539 |       0.157895 |   0.242335 |
| solution-1-flask   |     0.486631 |       1.00852  |   0.258669 |
| solution-1         |     8.75165  |       2e-06    |   0.8432   |
| solution-2         |     5.45094  |       0.713764 |   1.62072  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.477212 |       1.00861  |   0.368738 |
| solution-aron-mark |     0.472407 |       0.160249 |   0.369712 |
| solution-pl        |     0.511569 |       0.165265 |   0.376277 |
| solution-1-flask   |     0.479577 |       1.00869  |   0.789785 |
| solution-2         |     0.475637 |       0.530286 |   4.9238   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482236 |       0.170688 |    1.07628 |
| solution-pl        |     0.502891 |       0.179016 |    1.08092 |
| solution-flask     |     0.487085 |       1.00864  |    1.58655 |
| solution-1-flask   |     0.492544 |       1.00882  |    5.69509 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507751 |       0.208341 |    3.48928 |
| solution-pl        |     0.497063 |       0.210678 |    3.51245 |
| solution-flask     |     0.491092 |       1.00868  |    5.34518 |