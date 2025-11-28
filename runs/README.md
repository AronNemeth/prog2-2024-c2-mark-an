# 2025-11-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.55885  |       1.0569   |   0.104635 |
| solution-pl        |     0.496109 |       0.164218 |   0.252113 |
| solution-aron-mark |     0.487361 |       0.165727 |   0.252225 |
| solution-1-flask   |     0.492477 |       1.00815  |   0.293073 |
| solution-1         |     8.7669   |       1e-06    |   0.62473  |
| solution-2         |     4.54485  |       0.762645 |   0.872363 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478135 |       0.164685 |   0.374721 |
| solution-pl        |     0.484762 |       0.161492 |   0.376307 |
| solution-flask     |     0.490024 |       1.00873  |   0.382479 |
| solution-1-flask   |     0.485275 |       1.00845  |   0.794338 |
| solution-2         |     0.487574 |       0.541316 |   5.53     |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48174  |       0.168547 |    1.08788 |
| solution-aron-mark |     0.480859 |       0.167372 |    1.09191 |
| solution-flask     |     0.486792 |       1.00879  |    1.59128 |
| solution-1-flask   |     0.487624 |       1.00864  |    5.65139 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475679 |       0.197314 |    3.34967 |
| solution-aron-mark |     0.477366 |       0.202194 |    3.37605 |
| solution-flask     |     0.481868 |       1.00853  |    5.1912  |