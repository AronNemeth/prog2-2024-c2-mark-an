# 2026-09-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12034  |       1.11451  |   0.111272 |
| solution-pl        |     2.22454  |       0.155522 |   0.237994 |
| solution-aron-mark |     0.418785 |       0.152163 |   0.240899 |
| solution-1-flask   |     0.429899 |       1.00872  |   0.272443 |
| solution-1         |     7.31527  |       1e-06    |   0.639091 |
| solution-2         |     4.57268  |       0.551975 |   0.930859 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42434  |       0.153885 |   0.372895 |
| solution-aron-mark |     0.427994 |       0.153809 |   0.374528 |
| solution-flask     |     0.429229 |       1.00838  |   0.416334 |
| solution-1-flask   |     0.432763 |       1.00951  |   0.817279 |
| solution-2         |     0.420725 |       0.49748  |   2.33854  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423419 |       0.162199 |    1.13692 |
| solution-aron-mark |     0.422123 |       0.158226 |    1.13826 |
| solution-flask     |     0.423605 |       1.00823  |    1.66289 |
| solution-1-flask   |     0.430512 |       1.0084   |    5.73655 |
| solution-2         |     0.426239 |       0.554893 |  161.345   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422381 |       0.184368 |    3.50856 |
| solution-pl        |     0.423609 |       0.185616 |    3.5272  |
| solution-flask     |     0.425306 |       1.00908  |    5.28313 |