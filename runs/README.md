# 2024-08-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.602736 |       1.01006  |   0.097217 |
| solution-aron-mark |     2.26045  |       0.110622 |   0.182325 |
| solution-pl        |     0.607321 |       0.111488 |   0.184871 |
| solution-1-flask   |     1.47011  |       1.08525  |   0.271851 |
| solution-1         |     8.75739  |       1e-06    |   0.766501 |
| solution-2         |     5.51208  |       0.696584 |   0.777492 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.619237 |       1.00967  |   0.234629 |
| solution-pl        |     0.597937 |       0.114256 |   0.301306 |
| solution-aron-mark |     0.614354 |       0.113385 |   0.340174 |
| solution-1-flask   |     0.623735 |       1.0097   |   0.80276  |
| solution-2         |     0.609685 |       0.529059 |  11.8854   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.614007 |       1.00971  |   0.917677 |
| solution-pl        |     0.601446 |       0.120459 |   1.02466  |
| solution-aron-mark |     0.625052 |       0.12362  |   1.03542  |
| solution-1-flask   |     0.619582 |       1.00953  |   5.93722  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.617689 |       1.00945  |    5.2305  |
| solution-pl        |     0.628927 |       0.150948 |    5.37079 |
| solution-aron-mark |     0.606813 |       0.155584 |    5.49956 |