# 2026-07-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.95335  |       1.00849  |   0.11084  |
| solution-aron-mark |     0.436562 |       0.155915 |   0.247306 |
| solution-pl        |     0.432879 |       0.152839 |   0.247939 |
| solution-1-flask   |     1.43825  |       1.11938  |   0.27731  |
| solution-1         |     8.77132  |       1e-06    |   0.669172 |
| solution-2         |     4.82069  |       0.63262  |   0.976213 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.439315 |       0.154449 |   0.380183 |
| solution-pl        |     0.432851 |       0.158224 |   0.383647 |
| solution-flask     |     0.437506 |       1.00863  |   0.40638  |
| solution-1-flask   |     0.438954 |       1.00877  |   0.824745 |
| solution-2         |     0.432722 |       0.520014 |   5.31429  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430741 |       0.158321 |    1.16964 |
| solution-aron-mark |     0.431349 |       0.163193 |    1.17063 |
| solution-flask     |     0.507026 |       1.00852  |    1.69712 |
| solution-1-flask   |     0.435256 |       1.00859  |    5.82612 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438004 |       0.184088 |    3.63173 |
| solution-pl        |     0.433214 |       0.183579 |    3.64875 |
| solution-flask     |     0.433303 |       1.00872  |    5.5001  |