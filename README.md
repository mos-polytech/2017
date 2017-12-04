# mos-polytech

Year: 2017

![mos-polytech](https://raw.githubusercontent.com/mos-polytech/2017/master/media/logo.jpg)


## Purpose

This package contains all the source code and lecture files.


## Requirements

You will need:

- `python3` and `python2` for legacy purposes
- `postgresql` version `9.6`
- `pycharm`
- `sublime`


## Chat

Any questions? Ask them in our [`gitter room`](https://gitter.im/sobolevn/mos-polytech).


## Marks

We track our progress in [Google Forms](https://docs.google.com/spreadsheets/d/1Q5MXKvTVWPuJ9ulgnDX4LcAejXU34vp8auTyxmLKM-A/edit?usp=sharing).

### Deadline

We have a strict deadline for your homework: each Thursday at 18:00 UTC+03:00
Any submission after that time is not counted. But appreciated.

### Global dealbreakers

We use [`homework-template`](https://github.com/mos-polytech/homework-template) as a template for our homework progress.
See ['How to submit a homework'](https://github.com/mos-polytech/homework-template#how-to-submit-a-homework) section.

All our homeworks are submitted via Pull Requests.
This is very important, since we learn [how to maintain](https://opensource.guide/how-to-contribute/) an [Open Source Software](https://en.wikipedia.org/wiki/Open-source_software) repository.
There are a lot of tricky parts and manual labour, which we are mastering.

So, there are basic rule which are required (breaking any of them automatically cancels your current homework submission):

- Homework template differs from https://github.com/mos-polytech/homework-template
- Homework template is not in sync with the `upstream`'s `master`
- You have unmerged changes or Pull Requests in your repository
- You are working in a wrong branch
- You are not naming your branches properly ([why?](http://nvie.com/posts/a-successful-git-branching-model/))
- You don't have an opened [Pull Request](https://gist.github.com/MarcDiethelm/7303312#how-to-make-a-clean-pull-request) for your submission (because we are using [Code Reviews](https://github.com/features/code-review/), if you don't have a Pull Request opened, there's nothing to review)
- You have other (unrelated) changes in a Pull Request
- Your [Travis CI](https://docs.travis-ci.com/user/for-beginners) build fails or does not exist ([why?](https://blog.codeship.com/continuous-integration-important/))

### I am too smart for this!

I can automatically receive the highest score
by reaching 5000 reputation on [`SO`](https://stackoverflow.com/).

Testing criteria:

- Reputation should be presented in your profile with both charts
- Reputation should be presented in your status bar
- Reputation should be preserved after page reload
- There must be at least one your question or answer
- Total score on every question and answer should be almost equal to your final score + sum of accepted answers
- Domain should look like: `stackoverflow.com`
- You should be allowed to down vote and reputation should change

### Regular score

Final score is calculated by this formula:

> 0.6 for your homeworks and tests
>
> 0.4 for your final exam
>

Where your homeworks and tests are:

> 0.5 for tests
>
> 0.5 for homeworks
>

Homeworks and tests use percents to calculate how many tasks you have passed.

### Criteria

| Score  | Result |
|--------|--------|
| >= 40% |    3   |
| >= 60% |    4   |
| >= 80% |    5   |

### Final exam

Exam will be scored in percents as well.
Your work will be measured with 10 different criteria.
You can score 10% maximum for each of them.

You **won't receive any points** in three cases:

- you have not completed **any** of the functional tasks
- you have used some blacklisted software
- you have copied your work from someone else (even partly)

Criteria:

- 0 or 10 percents for code style (should match [these packages](https://github.com/wemake-services/wemake-django-template/blob/29ad5ec5482622def67d23c4d114f7af41430f3d/%7B%7Bcookiecutter.project_name%7D%7D/Pipfile)). Any style violations will result in 0%
- 0, 5 or 10 percents for tests. 10% is awarded if test coverage is equal to 100%, 5% is awarded if coverage is in range `[60%, 100%)`, 0% is awarded in all other cases
- 0 or 10 percents for [code quality](http://wemake-django-template.readthedocs.io/en/latest/_pages/template/qa.html). If your code passes `xenon --max-absolute B --max-modules A --max-average A .` you will be awarded with 10%
- 0 or 10 percents for requirements. If your requirements are present, [safe](https://docs.pipenv.org/advanced.html#detection-of-security-vulnerabilities), and valid you will receive 10% for this
- 0 or 10 percents for settings. If you have any issues with your settings you won't receive any points. See [settings validation](https://github.com/wemake-services/wemake-django-template/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/docker/django/gunicorn.sh#L11)
- 0, 5 or 10 percents for models. Everything looks good - 10%, something is not so good - 5%, cruel errors - 0%. There is no automation for this criteria
- 0, 5 or 10 percent for admin panel. Everything looks good - 10%, something is not so good - 5%, cruel errors - 0%. There is no automation for this criteria
- 0, 5 or 10 percents for `rest-framework`. Everything looks good - 10%, something is not so good - 5%, cruel errors - 0%. There is no automation for this criteria
- 0 or 10 percents for REST API documentation. It should be present and valid
- 0, 5 or 10 percents for business logic (everything else is business logic). Everything looks good - 10%, something is not so good - 5%, cruel errors - 0%. There is no automation for this criteria

Bonus points:

- you can receive bonus 5% for the great `README` and `travis` setup
- you can receive bonus 10% for deploying your project to `heroku`
- you can receive bonus 5% for automating deploy step (each successful `travis` build should deploy new version of software to `heroku`)

### Formula

```python
final_mark = 0.4 * final_exam + 0.6 * (0.5 * homework + 0.5 * tests)
```


## Timetable

|   | Start |  End  |
|---|:-----:|:-----:|
| 1 | 10:40 | 12:10 |
| 2 | 12:20 | 13:50 |
| 3 | 14:30 | 16:00 |
