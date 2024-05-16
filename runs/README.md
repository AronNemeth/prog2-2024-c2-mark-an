# 2024-05-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29144  |       1.10587  |   0.074257 |
| solution-aron-mark |     5.78572  |       0.150774 |   0.173071 |
| solution-pl        |     0.654036 |       0.119045 |   0.173365 |
| solution-1-flask   |     0.7031   |       1.00888  |   0.267133 |
| solution-1         |     7.95113  |       1e-06    |   0.872834 |
| solution-2         |     0.652636 |       0.417308 |   1.38929  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659693 |       1.00881  |   0.158923 |
| solution-pl        |     0.657449 |       0.12461  |   0.269916 |
| solution-aron-mark |     0.662572 |       0.124445 |   0.271509 |
| solution-1-flask   |     0.692582 |       1.00887  |   0.791184 |
| solution-2         |     0.660648 |       0.426022 |   2.99616  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660862 |       1.00887  |   0.708427 |
| solution-pl        |     0.661739 |       0.132431 |   0.816147 |
| solution-aron-mark |     0.6671   |       0.131284 |   0.830846 |
| solution-1-flask   |     0.671495 |       1.00889  |   5.5808   |
| solution-2         |     0.664521 |       0.49386  | 171.264    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657162 |       1.00897  |    2.48564 |
| solution-pl        |     0.661093 |       0.167825 |    2.62787 |
| solution-aron-mark |     0.662679 |       0.168132 |    2.62879 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656389 |       1.00921  |    15.7113 |
| solution-aron-mark |     0.66321  |       0.299284 |    15.9317 |
| solution-pl        |     0.660211 |       0.293624 |    16.0766 |