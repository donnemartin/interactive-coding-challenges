Contributing
============

Contributions are welcome!

**Please carefully read this page to make the code review process go as smoothly as possible and to maximize the likelihood of your contribution being merged.**

## Bug Reports

For bug reports or requests [submit an issue](https://github.com/donnemartin/interactive-coding-challenges/issues).

## Pull Requests

**Please follow the general [Repo Structure](https://github.com/donnemartin/interactive-coding-challenges#repo-structure) and [Notebook Structure](https://github.com/donnemartin/interactive-coding-challenges#notebook-structure) before submitting your pull request.**

The preferred way to contribute is to fork the
[main repository](https://github.com/donnemartin/interactive-coding-challenges) on GitHub.

1. Fork the [main repository](https://github.com/donnemartin/interactive-coding-challenges).  Click on the 'Fork' button near the top of the page.  This creates a copy of the code under your account on the GitHub server.

2. Clone this copy to your local disk:

        $ git clone git@github.com:YourLogin/interactive-coding-challenges.git
        $ cd interactive-coding-challenges

3. Create a branch to hold your changes and start making changes. Don't work in the ``master`` branch!

        $ git checkout -b my-feature

4. Work on this copy on your computer using Git to do the version control. When you're done editing, run the following to record your changes in Git:

        $ git add modified_files
        $ git commit

5. Push your changes to GitHub with:

        $ git push -u origin my-feature

6. Finally, go to the web page of your fork of the interactive-coding-challenges repo and click 'Pull request' to send your changes for review.

**Please submit one pull request per challenge.**

### GitHub Pull Requests Docs

If you are not familiar with pull requests, review the [pull request docs](https://help.github.com/articles/using-pull-requests/).

### Notebook Installation

Refer to [Accessing the Challenges](https://github.com/donnemartin/interactive-coding-challenges#accessing-the-challenges), [Notebook Installation](https://github.com/donnemartin/interactive-coding-challenges#notebook-installation), and [Nose Installation](https://github.com/donnemartin/interactive-coding-challenges#nose-installation) to set up your local environment.

### Adding New Solutions to Existing Challenges

Challenges have multiple solutions.  If adding new solutions to existing challenges:
* Add your algorithm discussion and code solution to the existing notebook
* Update the unit test to include your solution
* Verify your code passes the unit tests

### Adding New Challenges

The README contains several sample challenges that are not yet implemented.
* The sample challenges are only suggestions, please do not limit yourself to only these topics
* Feel free to send pull requests on different challenges or categories of challenges
* Try to keep the "Challenge" title relatively short and expand on the details within the notebook
* Review the [Repo Structure](https://github.com/donnemartin/interactive-coding-challenges#repo-structure) and [Notebook Structure](https://github.com/donnemartin/interactive-coding-challenges#notebook-structure) sections
* Check out the [template challenge and solution notebooks](https://github.com/donnemartin/interactive-coding-challenges/tree/master/templates) to help you get started

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Check if a number is prime | [Contribute](https://github.com/donnemartin/interactive-coding-challenges#contributing)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges#contributing) |
| Generate a list of primes | [Contribute](https://github.com/donnemartin/interactive-coding-challenges#contributing)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges#contributing) |

Update the list of challenges in the README so we can enjoy your challenge!

### Update Notebook Author(s)

When contributing to a notebook, update the notebook author(s):

<small><i>This notebook was prepared by [Joe](https://github.com/) and [Jane](https://github.com/). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).</i></small>

### Maintain Consistent Style

Please refer to the style of existing notebooks to help maintain consistency.  A consistently themed collection of notebooks will help users more seamlessly transition from challenge to challenge.

Review the following [style guide](https://google.github.io/styleguide/pyguide.html).

Review [PEP8](https://www.python.org/dev/peps/pep-0008/) and use a [validator](http://pep8online.com/).

*Note: IPython Notebook doesn't seem to properly handle a blank line at the end of a code cell when writing the cell's contents to a file, as referenced in this [issue](https://github.com/ipython/ipython/issues/8626).  Notebook cells currently do not have a blank line at the end of each code cell.*

### Contributions in Languages Other than Python

Feel free to share your thoughts on how we could best approach adding challenges in other [supported languages](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages):
* Repo structure
* README challenge list
* Installation instructions
* Etc

Share your thoughts in this [issue](https://github.com/donnemartin/interactive-coding-challenges/issues/3).