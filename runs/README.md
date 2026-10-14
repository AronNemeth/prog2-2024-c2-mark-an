# 2026-10-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12488  |       1.04626  |   0.100378 |
| solution-pl        |     0.422475 |       0.165495 |   0.253756 |
| solution-aron-mark |     6.22993  |       0.183742 |   0.255789 |
| solution-1-flask   |     0.439541 |       1.00843  |   0.265515 |
| solution-1         |     7.75602  |       1e-06    |   0.654541 |
| solution-2         |     0.424981 |       0.675931 |   1.03182  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.440135 |       1.00856  |   0.242349 |
| solution-aron-mark |     0.438222 |       0.169268 |   0.408483 |
| solution-pl        |     0.446799 |       0.174143 |   0.425881 |
| solution-1-flask   |     0.442871 |       1.00865  |   0.808165 |
| solution-2         |     0.430411 |       0.52214  |   2.56836  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.443842 |       1.00876  |    1.05976 |
| solution-aron-mark |     0.442897 |       0.177191 |    1.18003 |
| solution-pl        |     0.439525 |       0.180419 |    1.18723 |
| solution-1-flask   |     0.45345  |       1.00871  |    5.59915 |
| solution-2         |     0.431418 |       0.576317 |  301.251   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451103 |       0.211282 |    3.72614 |
| solution-pl        |     0.448017 |       0.204501 |    3.76587 |
| solution-flask     |     0.441263 |       1.00903  |    4.41556 |