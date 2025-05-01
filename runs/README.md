# 2025-05-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.04658  |       1.0826   |   0.094603 |
| solution-pl        |     5.65493  |       0.124032 |   0.191298 |
| solution-aron-mark |     0.476277 |       0.120446 |   0.194641 |
| solution-1-flask   |     0.478384 |       1.00889  |   0.258567 |
| solution-1         |     7.34857  |       1e-06    |   0.612756 |
| solution-2         |     0.465369 |       0.654264 |   1.4499   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478981 |       0.122637 |   0.298752 |
| solution-flask     |     0.470818 |       1.00901  |   0.305093 |
| solution-pl        |     0.47136  |       0.122407 |   0.310222 |
| solution-1-flask   |     0.479348 |       1.00917  |   0.7948   |
| solution-2         |     0.470037 |       0.510901 |   3.10695  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47913  |       0.131052 |   0.9037   |
| solution-pl        |     0.471139 |       0.136606 |   0.930717 |
| solution-flask     |     0.463991 |       1.00895  |   1.2519   |
| solution-1-flask   |     0.479153 |       1.00901  |   5.43631  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473767 |       0.159943 |    2.82214 |
| solution-pl        |     0.470194 |       0.165342 |    2.87543 |
| solution-flask     |     0.474227 |       1.00942  |    4.27181 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465675 |       0.266287 |    16.4009 |
| solution-pl        |     0.477908 |       0.271822 |    16.5922 |