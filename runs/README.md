# 2025-07-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.24505  |       1.22211  |   0.098901 |
| solution-aron-mark |     4.35155  |       0.146866 |   0.237962 |
| solution-pl        |     0.498623 |       0.153602 |   0.238026 |
| solution-1-flask   |     0.506625 |       1.00843  |   0.262678 |
| solution-1         |     7.25648  |       1e-06    |   0.668558 |
| solution-2         |     0.495228 |       0.613412 |   1.28276  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495765 |       0.150532 |   0.360172 |
| solution-pl        |     0.49466  |       0.1498   |   0.363983 |
| solution-flask     |     0.498681 |       1.00838  |   0.386602 |
| solution-1-flask   |     0.515319 |       1.00836  |   0.806686 |
| solution-2         |     0.499211 |       0.503052 |   2.17469  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500264 |       0.159009 |    1.08231 |
| solution-pl        |     0.505358 |       0.157214 |    1.08329 |
| solution-flask     |     0.497485 |       1.00836  |    1.62014 |
| solution-1-flask   |     0.51268  |       1.00861  |    5.60144 |
| solution-2         |     0.494902 |       0.557381 |   38.9939  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511023 |       0.187066 |    3.19807 |
| solution-aron-mark |     0.511889 |       0.19006  |    3.24695 |
| solution-flask     |     0.49893  |       1.00868  |    5.16242 |